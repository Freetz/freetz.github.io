dnsd
====

Schlanker DNS-Server für statische Namensauflösung (BusyBox Applet)

.. _Links:

Links
-----

-  `​Man page <http://www.busybox.net/downloads/BusyBox.html#dnsd>`__

.. _Beispielkonfiguration:

Beispielkonfiguration
---------------------

Port 53 mit `AVM firewall CGI <avm-firewall.html>`__ nach 10053 mappen
wo `iodine <iodine.html>`__ läuft. Dieses leitet Anfragen unbekannter
Domains auf Port 5353 weiter wo *dnsd* läuft. *dnsd* beantwortet für ein
paar Subdomains diese Anfragen.

-  Tags
-  `network </tags/network>`__
-  `packages <../packages.html>`__
