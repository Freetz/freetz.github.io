.. _UsingwithTor:

Using with Tor
--------------

#. Add *socksParentProxy=localhost:9050* to *Additional options*
#. Point your browser http proxy to 192.168.178.1:8123
#. Set *No proxy for* to *localhost, 127.0.0.1, 192.168.178.0/24*

(assuming default configuration)

If you use Firefox, use `​Tor
Button <https://addons.mozilla.org/nl/firefox/addon/2275/>`__ to prevent
DNS leakage (and other privacy problems with cookies, plugins, etc).

.. _Usingatyouroffice:

Using at your office
--------------------

Maybe your internet access at your office (school, internet café, etc)
is restricted, filtered and/or monitored and you don't want that. In my
case Trend Micro OfficeScan blocks a lot of web-sites as false positives
(including `​www.ip-phone-forum.de <http://www.ip-phone-forum.de/>`__).
A solution is this:

#. Install Polipo and `dropbear <dropbear.html>`__ (or another tunnel
   package)
#. Forward port 22 (and/or 80 if port 22 is blocked) to localhost:22
   using `AVM-firewall <avm-firewall.html>`__
#. Create an `​SSH
   tunnel <http://oldsite.precedence.co.uk/nc/putty.html>`__ from your
   office to your FritzBox, for example using
   `​putty <http://www.chiark.greenend.org.uk/~sgtatham/putty/>`__
#. Configure your browser at your office to use the http proxy
   localhost:8123 (assuming default Polipo configuration)

It is not an bad idea to restrict the memory Polipo will use with the
following additional option:

.. code:: bash

   chunkHighMark=1048576

.. _Security:

Security
--------

Unless you restrict the IP addresses that can access dropbear, my advice
is to disable password login and to use `host-based
authentication <dropbear.html#ZugangmitPutty1>`__.

It is also possible to encapsulate SSH traffic using
`STunnel <stunnel.html>`__, for cases where only http/https traffic is
allowed.

Beware that DNS requests could still be monitored, see the section about
Tor about how to prevent this. (it is possible to use Tor Button without
Tor)

It is possible to tighten security by using these options:

.. code:: bash

   tunnelAllowedPorts=443;allowedPorts=80,443

This prevent tunneling through the proxy and access to the freetz web
interface.

.. _Blockingdomains:

Blocking domains
----------------

Using the extra options it is possible to specify a file with forbidden
domains, like this:

.. code:: bash

   forbiddenFile=/var/media/ftp/uFlash/polipo/forbidden

Add the domains you want to block on separate lines, like this:

.. code:: bash

   doubleclick.net
   googleadservices.com
   google-analytics.com
   googlesyndication.com
   facebook.com/plugins

.. _Issues:

Issues
------

-  Download of large files is broken and wont be fixed:
   `​ticket <https://trac.torproject.org/projects/tor/ticket/1149>`__

.. _Links:

Links
-----

-  `​Polipo home <http://www.pps.jussieu.fr/~jch/software/polipo/>`__
-  `​Polipo status <http://192.168.178.1:8123/polipo/status?>`__
-  `​Polipo configuration <http://192.168.178.1:8123/polipo/config?>`__
-  `Package Tor <tor.html>`__

-  Tags
-  `network </tags/network>`__
-  `packages <../packages.html>`__
-  `proxy </tags/proxy>`__
