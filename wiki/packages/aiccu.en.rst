.. _AICCU:

AICCU
-----

AICCU (Automatic IPv6 Connectivity Client Utility) makes it easy for
users to get IPv6 connectivity. More info about AICCU can be found via:
`​http://www.sixxs.net/tools/aiccu/ <http://www.sixxs.net/tools/aiccu/>`__

.. _SixXSaccount:

SixXS account
~~~~~~~~~~~~~

To able to use AICCU you need an Sixxs account, and Tunnel. You can
request and account and tunnel by following the steps on the following
link:
`​http://www.sixxs.net/faq/account/?faq=10steps <http://www.sixxs.net/faq/account/?faq=10steps>`__
The request are handeled by SixXS staff. This means that it takes a
number of days before your request is granted. But also that you should
make sure all questions are properly filled. The type of tunnel you
probably need to request is an `​Anything In Anything
(AYIYA) <http://www.sixxs.net/tools/ayiya/>`__.

.. _CreatingaFeetzImagewithAICCU:

Creating a Feetz Image with AICCU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Follow the directions from the `Wiki <../index.en.html#>`__
| After the following step you can configure the packages you want to
  have included in your image.

.. code:: bash

   make menuconfig

Make sure the following is selected:

.. code:: bash

   [*] Show advanced options
   [*]   Enable IPv6 support

.. code:: bash

   Package selection  --->  Standard packages  --->  [*] aiccu - aiccu - ipv6 connectivity from sixxs

I also advice to add the following for easier troubleshooting:

.. code:: bash

   Advanced options  ---> BusyBox options  --->    IPv6 Options  --->   [*] ping6 command
   Advanced options  --->   BusyBox options  --->    IPv6 Options  --->   [*] traceroute6 command

.. _SetupinFreetzweb-interface:

Setup in Freetz web-interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| AICCU requires a that the time and date to be correct.
| So you need to give NTP some time at bootup of the router to obtain
  the current date and time.
| To have this behavior you can configure the 'Maximal time waiting for
  time-synchronisation (seconds)' under the Advanced section.

.. figure:: /screenshots/237.jpg
   :alt: Howto AICCU Setup

   Howto AICCU Setup

.. _CPUusage:

CPU usage
~~~~~~~~~

When IPv6 package are routed though the IPv6 tunnel over IPv4 towards
Sixxs, the router is using more CPU power than it just forwards IPv4
packets out over its default route. Every IPv6 package going into the
AYIYA tunnel will be signed with a sha1 hash. This additonal hashing
processing takes up our precious and limited CPU resources. Some
additional explanation of why AICCU takes so much CPU resources can be
found `​here <https://www.sixxs.net/forum/?msg=devel-778530>`__. If you
have more than a 15Mbit/s download link on a 7270v3 you will probably
see that you cannot use the full bandwidth, and that the web-inteface is
becoming slower to respond if you get near the 10Mbit/s. This is because
you are running out of CPU resources.

You can verify this with the following command:

.. code:: bash

    uptime

Or:

.. code:: bash

    cat /proc/loadavg

| If you see an avarage load value of higher than 1:00 you know that it
  is the CPU limitation you are running into.
| A good explanantion of how to interpret the values can be found
  `​here <http://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages>`__.

You can also use the following command:

.. code:: bash

   top

This will give you more than the load avarages, and refreshes the values
every 5 seconds.

.. _Other:

Other
~~~~~

| **Note** Be aware that Windows Vista and Windows 7 by default prefer
  IPv6 over IPv4. This will unnecessary stress the limited CPU power of
  the router.
| Look `​here <http://support.microsoft.com/kb/2533454/en-us>`__ for a
  option to make IPv4 more prefered than IPv6.
