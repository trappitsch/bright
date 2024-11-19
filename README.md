# `bright`ness controller for your screen

Simple tool to control the brightness of your screen using ddcutil.

## Installation

Install with `uv`, `pipx`, ...:

```bash
uv tool install git+https://github.com/trappitsch/bright
```

## Usage

Set the brightness from terminal with, e.g.,:

```bash
bright 50  # set to 50%
```

You can also read back the brightness by calling `bright` without arguments.

## Pre-requisites

You need to have `ddcutil` installed on your system. 
In addition, check what your monitor is connected to.
For my system, it's an `/dev/i2c*` device.
These belong to the `i2c` group, you might need to add your user to that group.

```bash
sudo usermod USERMOD -aG i2c
```

See [here](https://github.com/daitj/gnome-display-brightness-ddcutil/blob/master/README.md#setup-ddcutil)
for more information.

