Welcome
=======

Please download packages: LNcommon, LNdigitalIO, LN_Digital_Emulator, 
LN_Digital_Scratch_Handler, LN-Installer, unzip in your home folder::

    /home/bananapi/Documents

Install by Once
===============

You can install the packages: LNcommon, LNdigitalIO, LN_Digital_Emulator, 
LN_Digital_Scratch_Handler at once with the following command::

    $ sudo python3 Installer.py

unInstall by Once
=================

You can remove the packages: LNcommon, LNdigitalIO, LN_Digital_Emulator, 
LN_Digital_Scratch_Handler at once with the following command::

    $ sudo python3 unInstaller.py

If you wish to use independent installation instead of Install by Once, 
you can check it out in each package folder. In addition, Please do the 
following system setup to ensure that the packages will work on your Pi. 

Enable the SPI module
=====================

LN Digitals boards communicate with the Banana Pi through the SPI interface.
The SPI interface driver is included in the latest Banana Pi distributions
but is not enabled by default. You can load the SPI driver manually by running::

    $ sudo modprobe spi-sun7i

And you can permanently enable it by commenting out the
``blacklist spi-sun7i`` line in ``/etc/modprobe.d/bpi-blacklist.conf``.

    $ sudo nano /etc/modprobe.d/bpi-blacklist.conf

Then enable spi modules by adding ``spi-sun7i`` and ``spidev`` to ``/etc/modules``
    $ sudo nano /etc/modules

The /dev/spidev* devices should now appear but they require special privileges
for the user *bananapi* to access them. You can set these up by adding the following
`udev rule <https://wiki.debian.org/udev>`_ to
``/etc/udev/rules.d/50-spi.rules`` 

    KERNEL=="spidev*", GROUP="spi", MODE="0660"

with the following command::

    $ sudo nano /etc/udev/rules.d/50-spi.rules

Then create the spi group and add the user *bananapi*::

    $ sudo groupadd spi
    $ sudo gpasswd -a bananapi spi

.. note:: To enable other users to access SPI devices, you can add them to the
 ``spi`` group with ``gpasswd -a otheruser spi``.


Enable GPIO access
==================
Interrupts work by monitoring the GPIO pins. You'll need to give the user *bananapi*
access to these by adding the following udev rule (all on one line) to
``/etc/udev/rules.d/51-gpio.rules``::

    SUBSYSTEM=="gpio*", PROGRAM="
    /bin/sh -c 'chown -R root:gpio /sys/class/gpio &&
    chmod -R 770 /sys/class/gpio;
    chown -R root:gpio /sys/devices/platform/gpio-sunxi/gpio &&
    chmod -R 770 /sys/devices/platform/gpio-sunxi/gpio'"

with the following command::

    $ sudo nano /etc/udev/rules.d/51-gpio.rules

Then create the gpio group and add the user *bananapi*::

    $ sudo groupadd gpio
    $ sudo gpasswd -a bananapi gpio

You will have to reboot after setting up SPI and GPIO permissions.
