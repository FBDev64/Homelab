# The Raspberry Pi Zero W
This SBC is the core of the homelab. It's a Raspberry Pi Zero W, as the title intends.

It is in the last layer of the [tower](../Documentation/HARDWARE.md#tower).

## Power
It is powered by a [Power Bank](../Documentation/HARDWARE.md#material) of 2600 mAh.

## Tasks
It runs a CUPS print server, and in some caases, it will be a test environment for my projects.
You can access the site from [here](http://zerolab.gotdns.ch), provided by [noip.com](https://noip.com)

## Specifications
This informations are from Neofetch.
```bash
OS: Raspbian GNU/Linux 11 (bullseye) armv6l
Host: Raspberry Pi Zero W Rev 1.1
Shell: bash 5.1.4
CPU: BCM2835 (1) @ 1.000GHz
```

## Operating System
I recommend using Raspberry PI OS lite bullseye. A very minimal OS(command line only) and it receives security updates.

To download the OS, just grab the [Raspberry PI Imager](https://www.raspberrypi.com/software/) and choose your PI, OS and the MicroSD Card

## Remote Control
I use SSH access with Termius and Raspcontrol

## Containers and VMs
One thing I don't recommend is using containers on the Pi Zero. It will make it buggy and slow.
Prefer to run your Servers directly on the Pi Istelf, without a VM or containers.<br>
<br>Run it only if you manage to upgrade the Pi with a Waveshare adapter and a heatsink.