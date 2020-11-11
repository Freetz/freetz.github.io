.. _Tinyproxy:

Tinyproxy
=========

Das `​tinyproxy <http://tinyproxy.sourceforge.net/>`__ Paket stellt
einen kleinen HTTP Proxy mit Filterfunktionen bereit.

.. _Proxyauto-configpac:

Proxy auto-config (pac)
-----------------------

The complete URL for the default settings is:
`​http://fritz.box:88/cgi-bin/proxy.cgi <http://fritz.box:88/cgi-bin/proxy.cgi>`__

See also
`​wikipedia <http://en.wikipedia.org/wiki/Proxy_auto-config>`__.

.. _URLblocking:

URL blocking
------------

.. figure:: /screenshots/217.png
   :alt: tinyproxy filtered

   tinyproxy filtered

-  Clear option *ConnectPort*
-  Check option *FilterURLs*
-  Add URL's to text box *content of filter file*

.. code:: bash

   doubleclick\.net
   googleadservices\.com
   google-analytics\.com
   googlesyndication\.com
   facebook\.com\/plugins

Setup Firefox:

-  *Edit > Preferences > Advanced > Settings*
-  Check *Manual proxy configuration*
-  *HTTP Proxy:* fritz.box
-  *Port:* 3128 (assuming tinyproxy default)
-  Check *Use this proxy for all protocols*
-  *No proxy for:* localhost, 127.0.0.1, fritz.box, 192.168.178.0/24

.. _Memoryusage:

Memory usage
------------

After some use:

-  VmSize: 1068 kB
-  VmRSS: 508 kB

Privoxy will use twice as much.

-  Tags
-  `network </tags/network>`__
-  `packages <../packages.html>`__
-  `proxy </tags/proxy>`__
-  `web </tags/web>`__
