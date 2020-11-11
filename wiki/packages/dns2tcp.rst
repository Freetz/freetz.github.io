.. _Dns2Tcp:

Dns2Tcp
=======

**Dns2tcp** wurde entwickelt, um TCP Connections über DNS Traffic zu
"tunneln". Die Datenkapselung erfolgt bereits auf dem TCP Level, sodass
kein gesonderter Treiber (TUN/TAP) benötigt wird. Der *Dns2tcp* Client
muss nicht mit besonderen Rechten laufen.

*Dns2tcp* besteht aus zwei Teilen: Einem Server- und einem
Client-seitigen Tool. Aus seiner Konfigurationsdatei kennt der Server
eine Liste von Resourcen, wobei jede Resource ein lokaler oder
entfernter Dienst ist, der auf TCP Connections "horcht" ("Listener").
Der Client hört auf einen vordefinierten TCP Port, und leitet jede
eingehende Verbindung über DNS an den Zieldienst weiter.

.. _UsingwithFreeDNS:

Using with FreeDNS
~~~~~~~~~~~~~~~~~~

None of my hosting providers allowed me to set NS records, not even for
a subdomain, which seems to be common. I found out it is also possible
to use FreeDNS for this purpose.

Assuming you have a (`​DynDNS <http://www.dyndns.com/>`__) domain name
pointing to your Fritz!Box, lets say *fabulous.fritzbox.org*, you can do
this:

#. Register at `​FreeDNS <http://freedns.afraid.org/>`__
#. Create a FreeDNS subdomain:

   -  Type: *NS*
   -  Subdomain: anything you like, for example *dns2tcp*
   -  Domain: anything you like, for example *strangled.ne*\ t
   -  Destination: for example *fabulous.fritzbox.org*

#. Set *dns2tcp.strangled.net* as DNS name using the *dns2tcp* WebIF
#. On the client you should be able to create a DNS tunnel like this
   now:

   .. code:: bash

      dns2tcpc -r ssh -l 2222 -z dns2tcp.strangled.net fabulous.fritzbox.org

#. If you want a local `​SOCKS <http://en.wikipedia.org/wiki/SOCKS>`__
   server to browse the internet:

   .. code:: bash

      ssh root@localhost -p 2222 -D 8765

#. | If you want to use Polipo? as http proxy:

   .. code:: bash

      ssh root@localhost -p 2222 -L 8123:localhost:8123

A few notes:

#. Don't forget to forward port UDP 53 to *dns2tcpd*, for example using
   `AVM-Firewall <avm-firewall.html>`__
#. *dns2tcp* works with `dnsmasq <dnsmasq.html>`__, if you forward to a
   port other than 53
#. Use `dropbear <dropbear.html>`__ or *OpenSSH* as SSH server
#. Security advice: disable SSH password login and use a certificate to
   login
#. You can setup dynamic DNS using the regular Fritz!Box interface:

   -  Advanced settings \| Internet \| Permit Access \| Dynamic DNS

#. There is no Windows client available (you could try
   `iodine <iodine.html>`__)

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

-  `​Dns2Tcp Homepage <http://www.hsc.fr/ressources/outils/dns2tcp/>`__
-  `​Artikel: TCP over DNS mit
   dns2tcp <https://netzhure.de/2007/10/22/127-TCP-over-DNS-mit-dns2tcp.html>`__
-  `​IPPF Forumsdiskussion zu
   Dns2Tcp <http://www.ip-phone-forum.de/showthread.php?t=156586>`__

-  Tags
-  `network </tags/network>`__
-  `packages <../packages.html>`__
-  `tunnel </tags/tunnel>`__
