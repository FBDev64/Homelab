# The Raspberry Pi Zero W

This SBC is the core of the homelab. It's a Raspberry Pi Zero W, as the title intends.

## Power

It is powered by a [Power Bank](../Documentation/HARDWARE.md#material) of 2600 mAh.

## Tasks
I plan to do a Pico-8 physical console.

It only runs a webpage, that's it. I am
 currently searching ideas.
It also has no-ip.

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

## Tools

I use SSH access with [Termius](https://termius.com/) and [Raspcontroller](https://play.google.com/store/apps/details?id=it.Ettore.raspcontroller&hl=en&referrer=utm_source%3Dgoogle%26utm_medium%3Dorganic%26utm_term%3Draspcontroller&pcampaignid=APPU_1_kVuSZorHNpv-7_UP9q-c2AM). It helps shutdown the Pi fastly.

## No-IP

To setup no-ip, I followed [this tutorial](https://youtu.be/jvKKL18zt64?si=9yuTh3B-ke4FY1dQ)

## Containers and VMs

One thing I don't recommend is using containers on the Pi Zero. It will make it buggy and slow.
Prefer to run your Servers directly on the Pi Istelf, without a VM or containers.

Run it only if you manage to upgrade the Pi with a Waveshare adapter and a heatsink.
