# The IoT Cookbook

**Quick access by device:** [[Raspberry Pi]] | [[Arduino Yun]] | [[Tessel]] | [[Intel Edison]]

The **IoT Cookbook** provides a collection of ready-to-build recipes for connected IoT components to create your next IoT application.

Building on tested and documented components, makers and developers get a head start and can focus on creating their actual application functionality.

---

> NEWS, 2015/08/08: We've streamlined the Getting Started pages for all devices, in particular the Yun is now much simpler to setup. And we've released first pages for the Intel Edison.

**CONTRIBUTING: This is work in progress. If you find errors, bugs or other issues in above, or if you have new contributions (awesome!!), we would be happy to receive your [feedback or PRs on GitHub](https://github.com/crossbario/crossbarwww)!**

<!--
<iframe allowtransparency="true" frameborder="0" scrolling="no" src="https://platform.twitter.com/widgets/tweet_button.html?url=http://crossbar.io/iotcookbook/&via=crossbario&count=none&hashtags=iot,wamp,crossbar&text=IoT Cookbook: ready-to-build, open-source recipes for connected IoT components" style="width:70px; height:20px;"></iframe>
-->

## Overview

**You want to solve a problem and focus your efforts at the application level**, not fiddle around to get some basic IoT sensor or actuator component built and connected to your application backends.

With the component collection and all the recipes and tutorials, the IoT Cookbook wants to **free you from having to reinvent the wheels all over again**.

Components are connected using **Crossbar.io**, which allows you to **communicate with WAMP-enabled IoT devices** from more than **[9 programming languages](http://wamp.ws/implementations/#libraries)**. The IoT Cookbook has material for different languages as well. And we show how to build your own, reusable components, giving you the ultimate control:

* All components come with **built-in connectivity**. They can connect from anywhere, and you can easily build distributed applications.
* All components can **communicate freely with each other** - including calling procedures. The components connect via a Crossbar.io application router. Client libraries for WAMP, the protocol used, are available for [9 programming languages](http://wamp.ws/implementations/#libraries) (and growing). You can also integrate services with REST APIs, so your applications can talk to pretty much anything on the internet.
* All recipes include **step-by-step instructions**to get things working. Just follow the instructions - no need to worry about the technological background details. If you want to dive deeper into the technology, we provide links to get your started.
* The software used in these recipes is **open-source**, and part of a growing ecosystem around the WAMP protocol.
* A **variety of microcontrollers**, including the Raspberry Pi and Arduino Yun, are used as part of components.

## Running things

All the code and examples from the IoT Cookbook is on GitHub **[here](https://github.com/crossbario/crossbarexamples/iotcookbook)**. Clone this locally or [download](https://github.com/crossbario/crossbarexamples/archive/master.zip) it as a ZIP archive.

Most of the examples in the IoT Cookbook **require a WAMP router** for communication between WAMP-enabled IoT devices and other application components. While you can use [any WAMP router](http://wamp.ws/implementations/#routers), we recommend Crossbar.io.

Here are your options:

* **Option 1**: Use our hosted [Crossbar.io demo instance](../docs/Demo-Instance) for testing and light development
* **Option 2**: Spin up your own VM with [Crossbar.io on Microsoft Azure](../docs/Setup-on-Microsoft-Azure)
* **Option 3**: Spin up your own VM with [Crossbar.io on Amazon EC2](../docs/Setup-on-Amazon-EC2)
* **Option 4**: Install and [run Crossbar.io locally](../docs/Local-Installation)

## Devices

All recipes and documentation in the IoT Cookbook can be accessed starting from one of the covered devices. The devices we currently cover in the IoT Cookbook are:

* [[Raspberry Pi]]
* [[Arduino Yun]]
* [[Tessel]]
* [[Intel Edison]]

## Components

IoT building blocks, ready to use in your application:

* Sensors
   * Accelerometer - [Tessel](Tessel Accelerometer)/[Yun](Arduino Yun Accelerometer)
   * Ambient Light - [Yun](Arduino Yun Ambient Light Sensor)
   * Camera - [Tessel](Tessel Camera)/[Raspberry Pi](Raspberry Pi Camera)
   * Tilt Sensor - [Yun](Arduino Yun Tilt Sensor)
   * [Raspberry Pi Temperature Monitor](Raspberry Pi Temperature Monitor)
   * Weighing Pad - [Yun](Arduino Yun Weighing Pad)
* Inputs
   * X-Box Controller -[Raspberry Pi](Raspberry Pi Xbox Controller)
   * Buttons - [Yun](Arduino Yun Buttons)
   * Potentiometer - [Yun](Arduino Yun Potentiometer)
   * Novation Launchpad - [Raspberry Pi](Raspberry Pi Novation Launchpad) (**under construction**)
* Outputs
   * Speech Synthesis - [Raspberry Pi](Raspberry Pi Speech Synthesis)
   * Sample Playback -[Raspberry Pi](Raspberry Pi Sample Player)
   * Lights - [Yun](Arduino Yun Lights)
   * [LED Matrix Display](Arduino Yun LED Matrix Display)
   + [Browser Remote Control](Browser Remote Control)
   + [Reveal.js Remote Control](Reveal.js Remote Control)
   + [WAMP widgets](WAMP Browser Widgets) (**under construction**)

plus generic remote access & control of GPIO pins on the

* [Arduino Yun](Arduino Yun Serial to WAMP Bridge)
* [Raspberry Pi](Raspberry Pi Remote GPIO) (**under construction**)

## Applications

Applications which use the components. Get an idea for how combining things works, find code to re-use, be inspired - and maybe already find a solution which fits your needs!

* [Alarm Application](Apps Alarm)
* [Digital Signage](Digital Signage)
* [Euro Pallet Load](Euro Pallet Load)
* [Real-time charting with the Arduino Yun](Arduino Yun Real-time Charting) (**under construction**)
