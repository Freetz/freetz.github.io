dnsd
====

Small static DNS server daemon (BusyBox applet)

.. _Links:

Links
-----

-  `​Man page <http://www.busybox.net/downloads/BusyBox.html#dnsd>`__
-  `​DNS <http://en.wikipedia.org/wiki/Domain_Name_System>`__
   (wikipedia)

.. _Exampleusecase:

Example use case
----------------

I forward port 53 from outside to 10053, using `AVM firewall
CGI <avm-firewall.html>`__, where `iodine <iodine.html>`__ runs.
*iodine* forwards requests for unknown domains to port 5353 where *dnsd*
runs. *dnsd* answers requests for just a few sub-domains I want to use
too.

-  Tags
-  `network </tags/network>`__
-  `packages <../packages.html>`__
