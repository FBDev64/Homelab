# The Raspberry Pi Zero W

This SBC is the core of the homelab. It's a Raspberry Pi Zero W, as the title intends.

## Power

It is powered by a the Hub, in the second Micro-USB port, the USB connector.

## Job

Actually, the Pi is running a Git server using `apache2` and [gitweb](https://github.com/AdamOnAir/gitweb-pi) as a backup for my repositories.

## Operating System

I recommend using Raspberry PI OS lite bullseye. A very minimal OS (command line only) but still receives security updates.

To download the OS, just grab the [Raspberry PI Imager](https://www.raspberrypi.com/software/) and choose your PI version, desired OS and the MicroSD Card.

## Tools

- Phone : [Raspcontroller](https://play.google.com/store/apps/details?id=it.Ettore.raspcontroller&hl=en&referrer=utm_source%3Dgoogle%26utm_medium%3Dorganic%26utm_term%3Draspcontroller&pcampaignid=APPU_1_kVuSZorHNpv-7_UP9q-c2AM)
- SSH : OpenSSH and PuTTY
- UART : `minicom`

## Containers and VMs

One thing I don't recommend is using containers on the Pi Zero. It will make it buggy and slow.
Prefer to run your Servers directly on the Pi istelf, without a VM or containers.

Run it only if you manage to upgrade the Pi with a heatsink and somehow more RAM.
