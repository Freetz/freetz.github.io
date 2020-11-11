.. _WelcometoFreetz:

Welcome to Freetz
=================

**Freetz** (more about the name and history in the
`FAQs <FAQ.en.html>`__) is a firmware-extension (modification) for the
`​AVM Fritz!Box <http://www.avm.de/en/Produkte/FRITZBox/index.html>`__
and devices with identical hardware. The original firmware from the
manufacturer is extended with new functions and programs which may be
selected by the user. *Freetz* is `​free
software <http://www.germany.fsfeurope.org/documents/freesoftware.en.html>`__
and is developed by Oliver Metz, Alexander Kriegisch and others.

**Warning: the installation of a modified firmware invalidates the
manufacturer's warranty!**

Since most of the development team and users are German, most of this
website is written in the German language.

.. _Download:

Download
--------

The current stable release of Freetz is version 2.0. Please follow the
description under `Source Code <common/source_code.en.html>`__ to
download it.

.. _Firststeps:

First steps
-----------

If you are not familiar with Freetz and have no plan where to start,
follow the guidelines in this tutorial to build your first basic image.

-  `Freetz for beginners <help/howtos/common/newbie.en.html>`__

.. _Websitefordevelopers:

Website for developers
----------------------

This website is intended for developers and experienced users who wish
to be actively involved in the development of *Freetz*. The complete
source-code can be viewed and changes followed. Bugs and feature
requests can be entered using the ticket-system.

-  `Timeline </timeline>`__ — chronology of changes
-  `Roadmap </roadmap>`__ — current state and planned work (in progress)
-  `Source Browser <https://github.com/Freetz/freetz/commits/master>`__
   — browse the SVN repository
-  `Ticket System </report>`__ — problems, bugs and feature requests
   **(please**\ `read this <ticket.html>`__\ **and if necessary ask in
   the IP-Phone-Forum, before opening a ticket!)**
-  `Developer
   Information <help/howtos/development/developer_information.html>`__ —
   information for developers and howtos

In order to open tickets you will need to `register </register>`__.

.. _WikiandForum:

Wiki and Forum
--------------

Information and discussion about *Freetz* is available:

-  `Wiki <freetz.html>`__ - background,
   `Installation <help/howtos/common/install.html>`__,
   `packages <packages.html>`__, `libraries <libs.html>`__,
   `FAQ <FAQ.html>`__, `Howtos <help/howtos.html>`__
-  `​Forum <http://www.ip-phone-forum.de/forumdisplay.php?f=525>`__ —
   Discussion, questions, announcements (German and English language)
-  `IRC channel <help/irc.html>`__ about FritzBox and (inofficially)
   Freetz

Further information about Fritz and friends can be found here:

-  `​Fritz!Box Wiki <http://www.wehavemorefun.de/fritzbox>`__ — Tips &
   tricks, background info and more (German language)

See also the `FAQs <FAQ.en.html>`__.

.. _Freetzinpublicpressweb:

Freetz in public press & web
----------------------------

-  `List of public press, web & blog reports about
   Freetz <Press.en.html>`__

.. _Sourcecode:

Source code
-----------

How to `check out and update source code <common/source_code.html>`__
from the Freetz repository

.. _Buildingandusing:

Building and using
------------------

*Freetz* can only be built using Linux. See the README file in the root
directory of the checked-out source-code, as well as the `​IPPF
Wiki <http://wiki.ip-phone-forum.de/software:ds-mod:installation#linux>`__
(in German) for the list of tools/packages required to successfully
build *Freetz*. If you're really in a hurry make sure you've got all the
required tools installed and then do

.. code:: bash

   make menuconfig
   make

This gives you first a menu-based configuration and then builds your
custom firmware. Enjoy!
