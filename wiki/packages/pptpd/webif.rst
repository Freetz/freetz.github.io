.. _DasWeb-FrontendzumPaket:

Das Web-Frontend zum Paket
==========================

Das Interface an sich ist leicht überschaubar |;-)|.

Unter **Einstellungen** sind die Links zu den einzelnen
Konfigurationsdateien zu finden.

Ein Übersicht über die Einstellmöglichkeiten gibt die Dokumantation von
Poptop auf deren `​Homepage <http://poptop.sourceforge.net/dox/>`__.

-  **"pptpd Einstellungen bearbeiten"** editiert die Datei
   `​pptpd.conf <http://poptop.sourceforge.net/dox/pptpd.conf.txt>`__

   -  Pfadangaben zum Binary sowie zur Konfigurations-Datei
   -  mögliche Debug-Infos einschalten
   -  Server-IP festlegen (Standard: localip 192.168.178.1)
   -  IP-Bereich angemeldeter Rechner festlegen (Standard: remoteip
      192.168.178.210-229 )
   -  Sonstiges

-  **"PPPD Einstellungen bearbeiten"** editiert die Datei
   `​options.pptpd <http://poptop.sourceforge.net/dox/options.pptpd.txt>`__

   -  Name des PPTP-Server (Standard: fritzbox)
   -  Angabe, welche Protokolle zugelassen sind
   -  DNS-Server für Clients festlegen (Standard: ms-dns 192.168.178.1)
   -  Sonstiges

-  **"Password bearbeiten"** editiert die Datei
   `​chap-secrets <http://poptop.sourceforge.net/dox/chap-secrets.txt>`__

   -  verwaltet berechtigte Benutzer sowie deren Passwörter

.. figure:: /screenshots/38.png
   :alt: pptpd Einstellungen

   pptpd Einstellungen

.. _Portweiterleitung:

Portweiterleitung
-----------------

Um sich schließlich von außen auf den PPTP-Server verbinden zu können,
muss natürlich eine Portweiterleitung auf die IP der FRITZBox
eingerichtet werden.

.. code:: bash

   Protokoll: TCP  Port: 1723
   Protokoll: GRE  (keine Portangabe nötig)

Siehe dazu auch folgende Paketen:

-  `Virtual IP <../virtualip.html>`__
-  `AVM Firewall CGI <../avm-firewall.html>`__

.. |;-)| image:: ../../../chrome/wikiextras-icons-16/smiley-wink.png

