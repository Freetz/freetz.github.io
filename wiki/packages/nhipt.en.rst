.. _NHIPT-iptablesfirewallGUI:

NHIPT - iptables firewall GUI
=============================

.. _MOTIVATION:

MOTIVATION
----------

   iptables is a command-line interface for configuring the high -
   sophisticated
   `​netfilter <http://de.wikipedia.org/wiki/Netfilter/iptables>`__
   Linux kernel firewall. The nhipt web front-end exposes the whole
   potential of iptables in a user-friendly UI of your FritzBox and
   leverages this consumer device to the level of a professional
   firewall, supporting both IPv4 & IPv6 Layer-3 protocols. The UI can
   be either integrated in your firmware image or run stand-alone
   externally from an attached device (e.g. USB-Stick).

.. _PREREQUISITES::

PREREQUISITES:
--------------

-  iptables have to be **installed and running**.
   It is recommended to build at least the following kernel modules in
   your firmware image (the more you choose, the more fun you'll have):

..

   +-------------------+----------------------+----------------+-----------------+
   | \* ip_tables      | \* ip_conntrack      | \* ipt_log     | \* xt_state     |
   | \* x_tables       | \* ip_conntrack_ftp  | \* ipt_REJECT  | \* xt_conntrack |
   | \* iptable_filter | \* ip_conntrack_tftp | \* ipt_iprange | \* xt_multiport |
   |                   |                      |                | \* xt_tcpudp    |
   +-------------------+----------------------+----------------+-----------------+

   **!!! Please don't forget to include the according shared libraries
   too in your firmware image !!!**

..

   | The ideal build includes a replaced kernel with autoload kernel
     modules enabled (**make kernel-menuconfig** → **L**\ oadable
     modules support → **A**\ utomatic kernel module loading).
   | Prior to first use you must start iptables either by : **iptables
     -S** *(if you have a replaced kernel with automatic kernel modules
     loading)*
   | or (whithout autoload) by using **modprobe <modulname>** for each
     module.

.. _YOUHAVETHECHOICEOF3INSTALLOPTIONS::

YOU HAVE THE CHOICE OF 3 INSTALL OPTIONS:
-----------------------------------------

nhipt.cgi.(version).tar.gz
~~~~~~~~~~~~~~~~~~~~~~~~~~

   This is the naked GUI - you can run it directly from an USB stick,
   without the integration in freetz.

**Installation:**

-  copy the file **nhipt.cgi** to your stick (e.g. to:
   /var/media/ftp/uStor01/**ipt/cgi-bin**)
-  set execute permissions to the file.
-  set up the httpd deamon for the UI on the folder above of the cgi-bin
   (e.g. to\ **/ipt**) and use a free tcp port (e.g. 83).

.. code:: bash

   chmod +x /var/media/ftp/uStor01/ipt/cgi-bin/nhipt.cgi
   httpd -P /var/run/nhipt.pid -p 83 -h /var/media/ftp/uStor01/ipt

..

      Now you can access the UI via
      `​http://fritz.box:83/cgi-bin/nhipt.cgi <http://fritz.box:83/cgi-bin/nhipt.cgi>`__

ipt.(version).tar.gz
~~~~~~~~~~~~~~~~~~~~

   The external comfort package with freetz integration

**Installation:**

-  unpack to **/var/media/ftp/uStor01/**.
-  set execute permissions to **register.sh**
-  run **register.sh**

.. code:: bash

   chmod +x /var/media/ftp/uStor01/ipt/register.sh
   . /var/media/ftp/uStor01/ipt/register.sh

..

      Now you should have a brand-new package in the freetz UI, where
      you can configure all the installation options.

.. _usemakemenuconfig:

use *make menuconfig*
~~~~~~~~~~~~~~~~~~~~~

   Install the UI permanent in your firmware using the recent trunk.

**Installation:**

   | start with **make menuconfig**, go to **P**\ ackage Selection →
     **W**\ eb Interface → select option **NHIPT Iptables CGI**.
   | Now you get all iptables modules listed for your convenience. Make
     your selections and create your firmware the usual way.

.. _BEHINDTHESCENES::

BEHIND THE SCENES:
------------------

.. _Furtherinformation::

Further information:
~~~~~~~~~~~~~~~~~~~~

-  `iptables Wiki for beginners <iptables.en.html>`__
-  `​Windows Ports &
   Services <http://technet.microsoft.com/en-us/library/cc959833%28printer%29.aspx>`__

..

   The interface reads interactively the current rule set of your
   firewall and enables you to edit all rules, tables, chains, policies
   etc. online and life! This means, after submitting your changes the
   new rule immediately takes effect. The bad news are: You can
   accidentally lock out yourself - the good news are: it does not
   matter - the rule is not persistently saved - just reboot your box to
   the last known good rule set. When you have finished playing around
   with your rules and everything works as you like it you can click on
   **[Persist rules]** to save your work permanently and
   reboot-resistant either to the flash memory of the box or to the
   attached USB device **[BOOT FROM FLASH / USB] + [SET BOOT
   DIRECTORY]**. You can either use the guided UI to alter / add your
   rules for each chain or you can enter your rules using the command
   line expert interface on top. To add additional tables and modules
   use the selection checkboxes or modprobe them by hand in the expert
   UI. If you have ipv6 enabled and loaded, the UI also shows you the
   filter tables for ipv6.

   For security reason you can limit the access to the UI to a dedicated
   Admin-IP or Admin-IP-Range using: **[SET / CHANGE ADMIN IP]**.

..

   For the DECT boxes there is an option to set up an internal log
   deamon to catch the deviated kernel messages and present them in the
   UI. The log directory can be set up to any writeable destination.

   Error and system messages are shown in the bottom lines of the UI for
   your information, status 0 means OK.

.. _Bootprocess:

Boot process
~~~~~~~~~~~~

-  **debug.cfg** can be used to bootstrap the iptables rulset.
-  **rc.nhipt load** is called by **rc.mod** / **run level 20** and
   checks, if debug.cfg has startet the firewall, otherwise
   */tmp/flash/nhiptboot.cfg* is called to initialize the firewall
-  **debug.cfg** and **nhiptboot.cfg** use the same script settings and

   -  wait - if configured for USB ready or time-out
   -  copy the settings file **nhipt.par** as configured from the source
      (flash / USB) to the RAM disc
   -  copy the start script **nhipt.cfg** to the RAM disc
   -  run the start script **nhipt.cfg** detached in the background.

-  **nhipt.cfg**:

   -  stop dsld if configured for security reason
   -  wait for delay timer (if configured to prevent mistakenly
      lock-out)
   -  start dsld if configured
   -  start Web-Server for the UI
   -  start internal log-deamon if configured
   -  load all saved rules

..

      **Scenario 1:** stand-alone CGI - boots always from *debug.cfg*,
      rules can be saved either to the flash or to the usb stick.

      **Scenario 2:** dynamic freetz - boots either from *debug.cfg* or
      delayed from *freetz rc.custom* (rc.custom is used to re-integrate
      the dynamic modules in freetz after reboot)

..

      **Scenario 3:** *Runlevel of Freetz* - integrated start-up,
      optional *debug.cfg* can be used for early protection.

.. _configfile:

config file
~~~~~~~~~~~

| At run-time you'll find it here: */var/tmp/nhipt.par*, persistently
  stored at BOOTDIR along with the *nhipt.cfg*

.. code:: bash

   BACK=/var/media/ftp/uStor01/save
   CHANGED=0
   DELAY=0
   LOGTARGET=internal
   DSLDOFF=0
   ADMINIP=
   LOGD=/var/media/ftp/uStor01/log
   AIRBAG=0
   MYIP=
   BOOTSTRAP=freetz
   PORT=83
   BOOT=flash
   BOOTDIR=/tmp/flash
   ROOT=/usr/ipt

.. _filescontainedinthefreetzpackage:

files contained in the freetz package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   /etc/default.nhipt/nhipt.cfg       rwxrwxrwx    # config for freetz UI
   /etc/init.d/rc.nhipt               r-xr-xr-x    # call-back for freetz UI, boot loader
   /usr/ipt/index.html                r--r--r--    # frameset for UI
   /usr/ipt/cgi-bin/nhipt.cgi         r-xr-xr-x    # the CGI for iptables
   /lib/cgi-bin/nhipt.cgi             r-xr-xr-x    # the CGI for freetz settings

.. _RECOMMENDATIONS::

RECOMMENDATIONS:
----------------

Unexperianced users should read this carefully to prevent permanent
lock-outs.

Firewalls protect systems from intruders based on rules and policies.
They are obeyed by the system - the system cannot guess who is good and
who's bad. Eventually even experienced firewall admin's can lock
themselves out. It is good to know, how to recover from this in advance.

   The following hints can make your life easier:

-  you can look at all scripts - but don't change them manually, if you
   are not certain what they do exactly.
-  save rule sets permanently only if everything works as it should -
   test at least your admin access to the box. Use the BackUp Option so
   you can start over from a known-good set-up.
-  Use in the beginning the usb stick as boot target. If you lock-out
   yourself - just pull out the stick and reboot. No iptables will be
   loaded!
-  For Newbees there is a **[safe]** Mode. The firewall automatically
   takes care, that under all circumstances the Admin-IP will not be
   locked-out from the box (IPv4 only).
-  switching back to **[advanced]** lets you remove this safety rules
   later.
-  use the **[Boot-Delay]** option - this gives you some time to login
   and kill your naughty rule-set.
-  if you enter a wrong Admin-IP and lock yourself out from the UI - no
   problem. Use freetz UI to fix or edit **/var/tmp/nhipt.par** - Delete
   the ADMINIP= Entry.
-  if you ignore all this hints and finally lock yourself - the last
   chance is to flash a brand new image without iptables and delete the
   rules manually.

.. _DOWNLOAD:

DOWNLOAD
--------

   The latest version can be downloaded here: `​IPPF
   Forum <http://www.ip-phone-forum.de/showpost.php?p=1420252&postcount=1>`__,
   there are also tons of information to read in the forum.
