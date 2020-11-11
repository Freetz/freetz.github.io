ziproxy
=======

"*Ziproxy is a forwarding (non-caching) compressing HTTP proxy server.
Basically, it squeezes images by converting them to lower quality JPEGs
or JPEG 2000 and compresses (gzip) HTML and other text-like data. It
also provides other features such as: HTML/JS/CSS optimization,
preemptive hostname resolution, transparent proxying, IP ToS marking
(QoS), Ad-Blocker, detailed logging and more.*"

Useful when bandwidth is limited, for example on slow GPRS connections
or on slow or heavily shared internet connections in developing
countries (typical in internet cafes).

It is possible to use ziproxy as normal proxy by disabling the options
*GZip compression* and *Compress images*.

Ziproxy supports inet.

.. _CPUusage:

CPU usage
---------

Relatively heavy.

It may be necessary to disable the watchdog by adding this line to for
example *rc.custom*:

.. code:: bash

   echo "disable">/dev/watchdog

.. _Memoryusage:

Memory usage
------------

After a fresh start:

| *VmSize*: ~1800 kB
| *VmRSS*: ~375 kB

.. _URLnoprocessinglist:

URL no processing list
----------------------

You want probably at least:

.. code:: bash

   http://mt*.google.com/*
   http://khm*.google.com/*
   http://maps.gstatic.com/*

.. _URLdenylist:

URL deny list
-------------

.. figure:: /screenshots/218.png
   :alt: 

Something like:

.. code:: bash

   http://*.doubleclick.net/*
   http://*.googleadservices.com/*
   http://*.google-analytics.com/*
   http://*.googlesyndication.com/*
   http://adserver.*/*
   http://ads.*/*
   http://ad.*/*
   http://*.facebook.com/plugins*
   http://*.facebook.com/widgets*
   http://*.fbcdn.net/ads*/*

and maybe:

.. code:: bash

   http://*/*.swf

.. _Links:

Links
-----

-  `​Homepage <http://ziproxy.sourceforge.net/>`__
-  `​Readme <http://ziproxy.cvs.sourceforge.net/viewvc/ziproxy/ziproxy-default/README?view=markup>`__
-  `Ticket with patch </ticket/1356>`__
-  `​Using ziproxy <http://blog.mudy.info/2010/06/using-ziproxy/>`__
   (includes statistics)
-  `​Security note <https://www.kb.cert.org/vuls/id/MAPG-7N9GN8>`__
-  `​Linux.com <http://www.linux.com/archive/feature/148438>`__
