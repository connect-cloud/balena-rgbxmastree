# balena-rgbxmastree

## Required hardware
* Raspberry Pi (tested with Zero W, Pi 2 model B, Pi 4 model B)
* [3D RGB Xmas Tree for Raspberry Pi](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi)
* 8GB SD Card (Sandisk Extreme Pro recommended)
* Power supply

## Setup and configuration

Running this project is as simple as deploying it to a balenaCloud application. You can do it in just one click by using the button below:

[![deploy button](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/connect-cloud/balena-rgbxmastree&defaultDeviceType=raspberry-pi)

## Customization
With the environment variables below you can customize your 3D RGB Xmas Tree

### Delay
You can change the delay between updates of led's with the `DELAY` variable (seconds); set it anywhere from `0` to `~`, the default is 0.5 seconds.

### Brightness
You can change the brightness of the led's with the `BRIGHTNESS` variable; set it anywhere from `1` to `100`, the default is 8.
You'll find that 100 is _extremely bright_ and even 8 (default) is bright enough if the tree is on your desk :)

### Start time and stop time
If you want the Xmas Tree only to blink during the day (or other time range) you can configure at what time it starts and stops blinking with the
`STARTTIME` and `STOPTIME` variable; set these variables anywhere from `0000` to `2359`. The default are 0000 and 2359

### Philips Hue integration
Wouldn't it be nice if the xmas tree goes on and off at the same time as the lights in the room it's standing. If you are using Philips Hue lights and the tree is able to reach the Hue bridge you can connect it so the tree will go on when a specific light is turned on.
To turn this feature on set `USE_HUE_LIGHT_STATUS` to True and configure the following params:

`USE_HUE_LIGHT_STATUS` True

`HUE_IP` Set the IP address of the Hue bridge

`HUE_USERNAME` Set the username for the Hue bridge see following link to get a username https://developers.meethue.com/develop/get-started-2/

`HUE_LIGHT_NAME` Set the name of the Hue light you want to sync with the xmas tree

`HUE_USE_SSL` Set to True if you want to use HTTPS else it will be HTTP

