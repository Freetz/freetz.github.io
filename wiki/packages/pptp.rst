.. _PPTPClient:

PPTP Client
===========

``"PPTP Client is a Linux, FreeBSD, NetBSD and OpenBSD client for the proprietary Microsoft Point-to-Point Tunneling Protocol, PPTP. Allows connection to a PPTP based Virtual Private Network (VPN)."``

Viele Firmen setzen den PPTP-Server von Microsoft ein. Mit dem Client
kann man ein Verbindung zu diesem VPN über das **Point-to-Point
Tunneling Protocol** (**PPTP**) aufbauen

|Warning| Das PPTP-Package benötigt "replace kernel".

.. _PPTPKonfiguration:

PPTP Konfiguration
------------------

| 
| **Hostname**: ``VPN-Server``\ (Beispiel vpn.tolledomain.de)
| **Benutzername**: ``VPN-Benutzername``\ (Bei Windows bitte Domäne so
  schreiben → DOMÄNE/user oder DOMÄNE\\user, nicht DOMÄNE\user)
| **Servername**: ``PPTP``

.. _IPRouting:

IP Routing
----------

| 
| Aktivieren und in das Textfeld das Firmennetz samt Subnetzmaske
  reinschreiben (z.B. 10.0.0.0 255.255.255.0)

| Die Änderungen übernehmen und nochmal auf die Seite. Jetzt auf
  ``PPPD: chap-secrets bearbeiten`` klicken und dort folgendes
  eintragen: ``VPN-Username PPTP VPN-Password *``
| *Wichtig*: VPN-Username und VPN-Password sind durch eure Sachen zu
  ersetzen!

Danach unter Dienste das PPTP-Package starten und per SSH von der
Fritzbox einen Rechner im Firmennetz anpingen.

Routing/NAT infos folgen

Screenshot?

-  Tags
-  `daemons </tags/daemons>`__
-  `network </tags/network>`__
-  `packages <../packages.html>`__
-  `security </tags/security>`__
-  `server </tags/server>`__
-  `tunnel </tags/tunnel>`__

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

