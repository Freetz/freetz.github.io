.. _FreetzgetsmorefromtheBox:

Freetz gets more from the Box!
==============================

.. figure:: /screenshots/52.png
   :alt: 

The fritzbox firmware developers can't foresee all the functions that
you might wish for. Freetz changes this. The functionality of the box
can be adapted to individual needs. With Freetz, functionality can be:

-  **added.**
   That could, for example, be a web server or special VPN. The `list of
   packeges <packages.html>`__ provides an overview of what is possible.
-  **changed.**
   Sometimes, functionality exists but in it's original form it can't be
   configured or there are limits on what can be configured. (e.g. the
   integrated firewall). In this case, the `list of
   enhancements <packages.html#CGI-Erweiterungen>`__ gives an overview
   of the possibilities.
-  **removed.**
   This can be useful when a particular feature isn't needed or when
   additional space is needed to make way for additional packages (the
   box's memory is quite limited). There is also an overview of the
   options here in the `list of patches <patches.html>`__.

.. _HowdoesFreetzwork:

How does Freetz work?
---------------------

The Fritzbox firmware consists of many individual components. They are
developed by various people and organisations and built together to form
the Firmware. Freetz removes individual components, changes their
configuration or puts new components in place. In this way, a new
firmware can be built to match individual requirements. This new
firmware can be installed using the normal firmware update function.

.. _HowdoIobtainmyownFirmware:

How do I obtain my own Firmware?
--------------------------------

For legal reasons you have to build your own firmware yourself. More on
this later.

.. _Prerequisites:

Prerequisites
-------------

You will need:

-  A Linux-System. Either directly installed on the PC or in a virtual
   machine under Windows (e.g.
   `​Freetz-Linux <http://www.ip-phone-forum.de/showthread.php?t=194433>`__).
-  The Linux installation may need some additional packages to be
   installed. See `einige
   Werkzeuge <help/howtos/common/install.html#Linux>`__
-  `download <Download.html>`__ the current release of Freetz.

.. _TheProcess:

The Process
-----------

Once the prerequisites are in place, you are ready to go. You need to
take the following steps:

.. figure:: /screenshots/53.png
   :alt: Freetz menuconfig

   Freetz menuconfig

-  **Gather Parts.**
   The process is menu-driven. You can define define exactly what goes
   on the box and what features it will have. Freetz understands the
   dependencies between the components and ensures that it will put
   together a working combination.
-  **Produce.**
   This part takes a while, depending on the performance of the PC but
   it will normal proceed without requiring any interaction. In
   accordance with the selected components, source files will be
   downloaded from the Internet. At the end, a complete firmware file
   will exist.
-  **Install** using the normal Firmware-Update on the Box.
-  **Configure** and **use** the new features of the box. In the
   configuration you will find a Freetz link. Under here, the packages
   can be configured.

Detailed information regarding the
`FREETZ-Installation <help/howtos/common/install.html>`__ can be found
on the `corresponding wiki-Site <help/howtos/common/install.html>`__.
There's also special `instructions for
newbies <help/howtos/common/newbie.html>`__ which you should read if
you're new to Freetz.

.. _LegalBackground:

Legal Background
----------------

A large proportion of the Firmware components are Open Source software.
Their authors have explicity allowed the software to be used by anyone,
modified and distributed. Freetz makes good use of this.

Other parts of the Firmware are developed by AVM (or by other firms and
then licenced to AVM). These components are protected and not made
publicly available. In order to have a functioning box both these and
the free components are required.

For as long as this is the case, no complete firmware can be made
available for download. Freetz, therefore, is limited to providing the
tools with which anyone can build their own individual firmware.

The self-built firmware should not be made available publicly. In this
way we avoid upsetting AVM.

.. _Support:

Support
-------

When a self-built (and not the original) firmware is installed on the
box, you can't expect any support from AVM if you have any questions or
problems. You may, however, be able to get help in the
`​IP-Phone-Forum <http://www.ip-phone-forum.de/forumdisplay.php?f=525>`__.

.. _DonationsSupportfortheProject:

Donations / Support for the Project
-----------------------------------

| If you like Freetz and would like to support its further development,
  the developers would gladly receive any donation
  (`​Details <http://www.ip-phone-forum.de/showthread.php?p=959253#poststop>`__).
| Donate directly with
  `​Paypal <https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=paypal%40freetz%2eorg&item_name=Freetz%20Entwickler%2dTeam&no_shipping=1&return=http%3a%2f%2fwww%2efreetz%2eorg&cn=Name%20oder%20IPPF%2dPseudonym&tax=0&currency_code=EUR&lc=DE&bn=PP%2dDonationsBF&charset=UTF%2d8>`__.

.. _FurtherLinks:

Further Links
-------------

-  `Available Packages <packages.html>`__
-  `Available Patches <patches.html>`__
-  `​Support - Help and
   Support <http://www.ip-phone-forum.de/forumdisplay.php?f=525>`__
-  `Download Current Release <Download.html>`__
-  `FAQ - Frequently Asked Questions <FAQ.html>`__
-  `How To ... - Documentation of freetz
   Modifications <help/howtos.html>`__
-  `Developer
   Information <help/howtos/development/developer_information.html>`__
