iodine
======

`​iodine <http://code.kryo.se/iodine/>`__ erlaubt es, IPv4 Daten über
DNS zu tunneln. Eine hilfreiche Sache, wenn man z.B. hinter einer
restriktiven Firewall sitzt - da DNS Traffic in den seltensten Fällen
geblockt wird |;)|

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

-  `​iodine Homepage <http://code.kryo.se/iodine/>`__
-  `​iodine Man page <http://linux.die.net/man/8/iodine>`__
-  `​iodine documentation <http://code.kryo.se/iodine/README.html>`__

.. _UsingwithFreeDNS:

Using with FreeDNS
------------------

See package `dns2tcp <dns2tcp.html>`__ for signing up with FreeDNS and
some other details.

Put this in your *rc.custom* (there is no WebIF):

.. code:: bash

   mkdir /tmp/iodine
   chown nobody /tmp/iodine
   iodined -c -P <password> -u nobody -t /tmp/iodine 10.0.0.1 -p 10053 dns2tcp.strangled.net

(assuming user *nobody* exists)

The trunk version of Freetz has an iodine WebIF now (changeset #6657;
thanks oliver!)

Create a tunnel from the client like this:

.. code:: bash

   sudo ./bin/iodine -f -P <password> dns2tcp.strangled.net

To connect to Polipo?:

.. code:: bash

   ssh root@10.0.0.1 -L 8123:localhost:8123

The advantages over `dns2tcp <dns2tcp.html>`__ are:

-  There is an iodine Windows client available
-  It is possible to run iodine on Android
-  Traffic can easily be route through the tunnel

Building `​iodine for
Android <http://blog.bokhorst.biz/5123/computers-en-internet/iodine-for-android/>`__.

.. _Security:

Security
--------

Install `iptables <iptables.html>`__ and add these rules to allow only
traffic to the internet and not your local net:

.. code:: bash

   iptables -I OUTPUT -o dns0 -s 192.168.178.0/24 -j DROP
   iptables -I INPUT -i dns0 -d 192.168.178.0/24 -j DROP
   iptables -A FORWARD -i dns0 -o dsl -j ACCEPT
   iptables -A FORWARD -i dns0 -j DROP

Of course you can always allow specific traffic from tunnel to your
local net, for example to a SSH server by using something like:

.. code:: bash

   iptables -I INPUT -i dns0 -p tcp --dport 22 -j ACCEPT

.. _Forwarding:

Forwarding
----------

iodine can forward DNS requests for unknown (sub)domains to a real
DNS-server on another port with this switch:

.. code:: bash

   -b 5353

-  Tags
-  `network </tags/network>`__
-  `packages <../packages.html>`__
-  `tunnel </tags/tunnel>`__

.. |;)| image:: ../../chrome/wikiextras-icons-16/smiley-wink.png

