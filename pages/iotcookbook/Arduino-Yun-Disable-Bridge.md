# Disabling the Yun Serial bridge

We are using the serial connection between the MCU and the CPU. By default, there is a console attached on the Linux side to the serial, and we need to disable that.

> Note that doing so will disable the [Arduino Yun Bridge](https://www.arduino.cc/en/Reference/YunBridgeLibrary)

Edit the file `/etc/inittab` and comment the following line (by preceding it with `#`):

```shell
# ttyATH0::askfirst:/bin/ash --login
```

and reboot

    reboot

> Be patient, a reboot (either via the `reboot` command like above, or by doing a cold boot via power cycling or pressing the "Yun RST" button) can take 60-90s.
>

## Background

The Linux SoC (CPU) and the Atmel MCU are connected via a UART (a serial connection) which maps to the device `/dev/ttyATH0` on the Linux side and the [serial stream](http://arduino.cc/en/Reference/Serial) class `Serial1` on the Arduino side.

The default `inittab` entry on the Linux side will start a shell connected to that serial port when Linux boots. Then, when your sketch starts the Arduino Yun bridge library (by doing `Bridge.begin()`), the bridge library writes a command to the serial that will in turn start a script on the Linux side which then connects to the serial port.

Above Linux script is essentially the Linux-side part of the Yun bridge library and will keep on running regardless of wether you reload a new sketch to the MCU or reset the MCU. It will keep on running until you reset the CPU or reboot Linux (or manually kill the script).

However, as long as there is a script running and using the serial port, we cannot use the serial for our purposes. The commenting of the `inittab` line will disable starting a shell on the serial port altogether in the first place. **This means we can use the serial port for our stuff, but it also means you won't be able to use the Yun brigde library anymore.**


## Serial Terminal

You can attach a terminal to the Linux part of the Yun, e.g. to watch the Linux boot process and track down issues.

The way this works on the Yun involved multiple parts:

* a special sketch on the Yun's microcontroller ("YunSerialTerminal")
* a Linux console attached to the serial on the Yun's Linux part
* a terminal program on your PC

First, make sure the console on the Yun's Linux side is NOT disabled:

```console
root@Arduino:~# cat /etc/inittab 
::sysinit:/etc/init.d/rcS S boot
::shutdown:/etc/init.d/rcS K shutdown
ttyATH0::askfirst:/bin/ash --login
```

Then, upload this sketch to the Yun's microcontroller part:

![Arduino Yun Serial Terminal Sketch](/static/img/iotcookbook/yun/yun_sketch_serial_terminal.png)

> Above sketch is preinstalled when you buy a brand new Yun.

On the PC side, install a terminal program. On Ubuntu, you can use `screen`:

    sudo apt-get install screen

Then connect the micro USB of the Yun to your PC and start the terminal:

    screen /dev/ttyACM3 115200

> You might need to adjust the serial port `/dev/ttyACM3` to your system.


## How the bridge works

Here is how the bridge works.

The Yun has 2 USB ports

- a micro USB port connected to the microcontroller part of the Yun
- a USB host port connected to the MIPS SoC / Linux part of the Yun

and a serial connection between the microcontroller and MIPS SoC

![Arduino Yun System Architecture](/static/img/iotcookbook/yun/yun_diagram.png)

By default, there is a Linux shell (`/bin/ash`) listening on the serial port. This is configured in `/etc/inittab` via this line:

```text
ttyATH0::askfirst:/bin/ash --login
```

Now, the software of the bridge consists of 2 parts:

- C code running on the microcontroller (`~/arduino-1.6.5/libraries/Bridge/src/*`)
- Python code running on the SoC (`/usr/lib/python2.7/bridge/*`)

When the microcontroller C code of the bridge is starting, it'll talk to the shell (`/bin/ash`) attached to the serial on the SoC part, and the first thing it does is starting the Python part of the bridge by running `/usr/bin/run-bridge`:

```shell
#!/bin/sh

cd /usr/lib/python2.7/bridge

exec python -u bridge.py 2> /tmp/bridge.py-stderr.log
```

The Unix `exec` command will replace the `/bin/ash` shell process attached to the serial with the Python program `/usr/lib/python2.7/bridge/bridge.py`.
