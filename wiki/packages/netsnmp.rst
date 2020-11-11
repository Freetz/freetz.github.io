.. _Net-SNMP:

Net-SNMP
========

**SNMP** ist das **S**\ imple **N**\ etwork **M**\ anagement
**P**\ rotocol (einfaches Netzwerk-Verwaltungs Protokoll). Dieses
Protokoll wird genutzt, um die Geräte in großen Netzwerken verwalten zu
können. Fast jeder bessere Switch spricht SNMP. Man kann dann z.B.
remote einzelne Ports ein- bzw. ausschalten oder den aktuellen Traffic
einsehen und vieles mehr.

Dazu werden sogenannte Agenten eingesetzt, hier das Programm **snmpd**
(SNMP-Daemon), das direkt auf dem zu überwachenden Gerät (FRITZBox)
läuft. Diese Agenten sind in der Lage, den Zustand des Gerätes zu
erfassen und auch selbst Einstellungen vorzunehmen oder Aktionen
auszulösen.

Da hier im Wiki noch keine weitere Beschreibung vorhanden ist, zur
Information vorläufig das Folgende:

-  `​snmpd auf der
   FB <http://www.ip-phone-forum.de/showthread.php?t=122073>`__
-  `​snmpd.conf
   anpassen <http://www.ip-phone-forum.de/showthread.php?t=142295>`__
-  `​Einrichtung von SNMP-Agenten im Forschungszentrum
   Jülich <http://www.fz-juelich.de/zam/docs/tki/tki_html/t0320/t0320.html>`__

Im Webinterface von Freetz gibt es - sofern der snmpd im Image eingebaut
ist - unter *Einstellungen* den Punkt *snmpd.conf*. Dort kann man die
Datei ``snmpd.conf`` direkt editieren.

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

-  `​Net-SNMP Homepage <http://www.net-snmp.org/>`__ (hier finden sich
   auch englisch-sprachige Tutorials)
-  `​Wikipedia Article on Net-SNMP
   (English) <http://en.wikipedia.org/wiki/Net-SNMP>`__
-  `​Wikipedia:
   SNMP <http://de.wikipedia.org/wiki/Simple_Network_Management_Protocol>`__
-  `​SNMPLink.ORG <http://www.snmplink.org/>`__ (EN) gibt zahlreiche
   Referenzen zum Thema SNMP

--------------

-  Tags
-  `network </tags/network>`__
-  `packages <../packages.html>`__
