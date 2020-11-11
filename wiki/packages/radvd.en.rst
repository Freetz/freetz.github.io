.. _RADVD:

RADVD
-----

| The router advertisement daemon (RADVD) allows to both Linux and
  Windonws clients to obtain an IPv6 IP address, without any changes on
  the clients.
| More info about RADVD can be found via:
  `​http://www.litech.org/radvd/ <http://www.litech.org/radvd/>`__

.. _RequestasubnetfromSixXS:

Request a subnet from SixXS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| I hope you have enough points left to request a subnet from SixSX.
| If not, make sure you have Aiccu up for a few weeks, see the
  `​creadits FAQ <http://www.sixxs.net/faq/account/?faq=credits>`__.

| You can request a subnet from your SixXS `​home
  page <https://www.sixxs.net/home/>`__
| At the left on your home page you should find a list of options from
  which you should select `​Request
  subnet <https://www.sixxs.net/home/requestsubnet/>`__.

.. _CreatingaFeetzImagewithRadvd:

Creating a Feetz Image with Radvd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Follow the directions from the `/wiki/WikiStart.en#
  Wiki <../index.en.html#%20Wiki>`__
| After the following step you can configure the packages you want to
  have included in your image.

.. code:: bash

   make menuconfig

Make sure the following is selected:

.. code:: bash

   [*] Show advanced options
   [*]   Enable IPv6 support

.. code:: bash

   Package selection  --->  Standard packages  --->  [*] radvd (router advertisement daemon)

I also advice to add the following for easier troubleshooting:

.. code:: bash

   Advanced options  ---> BusyBox options  --->    IPv6 Options  --->   [*] ping6 command
   Advanced options  --->   BusyBox options  --->    IPv6 Options  --->   [*] traceroute6 command

.. _PatchingFreetz-1.2withClientconfigoption:

'Patching' Freetz-1.2 with Client config option
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Due to an application that is not supported on later versions, I
  prever to stay on Freetz-1.2.
| But due to issues with other IPv6 enabled devices, I would like to
  include enhancement `1921 </ticket/1921>`__ also in Freetz-1.2.

With the following commands executed before make you can have this
enhancement included also:

.. code:: bash

   cd ~/freetz-1.2/make/radvd/files/root/etc/default.radvd/
   wget "/browser/trunk/make/radvd/files/root/etc/default.radvd/radvd.cfg?rev=9419&format=txt" -O radvd.cfg
   cd ~/freetz-1.2/make/radvd/files/root/etc/default.radvd/
   wget "/browser/trunk/make/radvd/files/root/etc/default.radvd/radvd_conf?rev=9453&format=txt" -O radvd_conf
   cd ~/freetz-1.2/make/radvd/files/root/usr/lib/cgi-bin/
   wget "/browser/trunk/make/radvd/files/root/usr/lib/cgi-bin/radvd.cgi?rev=9444&format=txt" -O radvd.cgi

.. _SetupinFreetzweb-interface:

Setup in Freetz web-interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the setup it is 'sufficient' to just configure a /64 from your /48
you received from SixXS. E.g. you can pick the first possilbe /64 range
2001:aaaa:bbbb:0000::/64

Network range - 2001:aaaa:bbbb:0000:0000:0000:0000:0000 -
2001:aaaa:bbbb:0000:ffff:ffff:ffff:ffff

**Note** In below screenshot enhancement `1921 </ticket/1921>`__ is
included.

.. figure:: /screenshots/236.jpg
   :alt: Howto setup radvd

   Howto setup radvd

| To prevent unexpected reboots I had to unselect the 'Activate on start
  resp. deactivate on stop the IPv6 forwarding' on my FB-7270v3.

.. _LinuxClients:

Linux Clients
~~~~~~~~~~~~~

Not much to tell here. The output of ifconfig should show that it
recieved an IPv6 address, starting with your configured subnet and
ending with part of your MAC address in there.

There should also be a default IPv6 route pointing to the IPv6 gateway
(the router).

.. _WinXPClients:

WinXP Clients
~~~~~~~~~~~~~

| With my WinXP system I had no problems to obtain an IPv6. All I had to
  do was to was to enable IPv6 with:

.. code:: bash

   netsh interface ipv6 install

| Then you should see that you get two IPv6 addresses. One public and a
  temporary one.
| You can also see them with:

.. code:: bash

   netsh interface ipv6 show address

.. _Win7Clients:

Win7 Clients
~~~~~~~~~~~~

| I have two Win7 systems. One that was not mutch used with IPv6, and
  one where I used AICCU locally as a service at startup.
| The one that was not mutch used with IPv6 obtained an IPv6 address
  immediately. With the other one it took more effort.
| After modifying the service to only startup manually I didn't obtain
  an IPv6 address from RADVD, even after a reboot.

| If you have a similar problem you can try the following:

-  firt make sure you create a restore point.
-  | next use the following commands (note I used both commands without
     verifying correctly which one was needed):

   .. code:: bash

        netsh int ipv6 reset c:\ipv6_reset.log
        netsh interface isatap set state enabled
