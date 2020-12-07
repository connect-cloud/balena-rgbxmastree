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
You can change the brightness of the led's with the `BRIGHTNESS` variable; set it anywhere from `0.01` to `1`, the default is 0.08.
You'll find that 1 is _extremely bright_ and even 0.08 (default) is bright enough if the tree is on your desk :)
