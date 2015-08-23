# Remoting the Yun GPIOs

This page describes how to install the necessary software on a Yun to enable remote control of the Yun's Arduino pins via WAMP.  For an overview of all materials we have concerning the Yun, see

* [Arduino Yun - Links](Arduino Yun)

![Arduino Yun with GPIOs](/static/img/iotcookbook/remote_gpio_arduino_yun.jpg)

## The big picture

The GPIO pins are managed by the Arduino MCU part of the Yun, while all network communcation is managed by the MIPS part.
To get remote control, we need to pass data from the MUC to the MIPS/Linux part, and the send this over the network. We use WAMP for the remote communication. For the MCU-MIPS bridge we use the [Firmata](https://github.com/firmata/protocol) protocol.

There is an Arduino implementation of Firmata, which the MCU part runs. There are various implementations which we could run on the Linux side. In the end, using Node.js with `arduino-firmata` and Autobahn|JS to provide WAMP connectivity proved easiest.

This does not mean that you have to use JavaScript for your application: we provide access via WAMP to all the pins, so that you can write your actual control code in any language with a WAMP implementation. (You may at some point move control code onto the Yun itself, at which point the implementation languages become important again.)

## Preparation

Please follow the [quick setup](Arduino-Yun-Quick-Setup) for setting up the Linux side of the Yun, and the [Firmata installation](Arduino-Yun-Installing-Firmata) for the microcontroller part.

## The remote control code

We can now control the Arduino GPIO pins from Node.js - and the Node.js code in turn can communicate with any WAMP component.

This is fine, but we really want to be able to develop on our own machines and in more comfort - and in our language of choice.

This is made possible by the serial-to-WAMP-bridge code which we offer for running in Node.js. With this, input and output is run via standardized WAMP publishes and subscriptions, so that you can just set up the bridge once on the Yun and then develop components which use the pins whereever you want.

The code for this can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

From this you need to get `remote_gpio_yun.js` (in `crossbarexamples/iotcookbook/device/yun/remote_gpio`) onto the Yun.

First modify this so that it connects to your Crossbar.io instance, then do

    scp remote_gpio_yun.js root@<IP_of_your_Yun>:~/

from a shell open to the above directory.

Then run this

    nodejs remote_gpio_yun.js

## The API

The API exposes procedures in the format

    io.crossbar.examples.yun.<device_ID>.firmata.<procedure_name>

The procedures are:

* `set_mode`: set the mode for a pin, with the possible values `in` (you actively read from the pin), `out` (you write to the pin) and `watch` (monitor in value of the pin)
* `digital_read`: Read the state of a pin connected to digitial input device. Returns a Boolean.
* `digital_write`: Write the state of a pin connected to a digital output device. Takes a Boolean.
* `analog_read`: Read the state of a pin connected to an analog input device. Returns a numeric value, where the range depends on the input device .
* `analog_write`:  Write the state of a pin connected to an analog output device. Takes a numeric value, where the range depends on the output device.
* `servo_write`
* `reset`: reset the state of the arduino part

For pins which have been set to `watch`, value changes are published to the topics

    io.crossbar.examples.yun.<device_ID>.firmata.on_analog_changed

and (*presently unimplemented*)

    io.crossbar.examples.yun.<device_ID>.firmata.on_digital_changed

## Next

For examples of how remote GPIO can be used see e.g.

* [Alarm App](Apps Alarm)
* [Buttons](Arduino Yun Buttons)
* [Lights](Arduino Yun Lights)
