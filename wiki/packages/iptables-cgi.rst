iptables-cgi
============

**iptables-CGI** ist ein Web-Frontend für
`​iptables <http://de.wikipedia.org/wiki/Iptables>`__. Mittels iptables
lassen sich Firewallregeln umsetzen, indem einzelne Portregeln erstellt
bzw. gelöscht werden. Genutzt wird iptables u.a. von
`knockd <knock.html>`__.

.. _Installation:

Installation
------------

iptables-cgi kann in ``make menuconfig`` angewählt werden, wenn man
iptables markiert.

.. _HäufigeFragenHowto:

Häufige Fragen / Howto
----------------------

Die Funktionen und die Geschichte von iptables wird hier nicht
wiederholt bzw. erzählt, denn dazu gibt es schon genug Dokumentation in
Internet. Eine sehr gute Seite ist z.B. folgende:
`​http://de.wikipedia.org/wiki/Iptables <http://de.wikipedia.org/wiki/Iptables>`__

Hier wird nur auf das Webinterface von iptables eingegangen und mit
einfachen Sätzen erklärt, wie man damit arbeitet.

.. _Activation:

Activation
~~~~~~~~~~

Wenn hier "Active" ausgewählt wird, dann werden die iptables Module beim
Starten der Box geladen.

Beim "Stop" unter Dienste werden die Regeln und die Module entladen.

.. _iptablesaddremoverule:

iptables add/remove rule
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **Bezeichnug**                    | **Funktion**                      |
+-----------------------------------+-----------------------------------+
| Add                               | Fügt eine neue Regel hinzu        |
+-----------------------------------+-----------------------------------+
| Insert                            | Fügt eine neue Regel in die unter |
|                                   | "Position" angegebene Stelle ein  |
+-----------------------------------+-----------------------------------+
| Position (ID)                     | Dieses Feld ist nur in Verbindung |
|                                   | mit Insert nutzbar                |
+-----------------------------------+-----------------------------------+
| Chain                             | Gibt an, in welche Tabelle die    |
|                                   | Regel abgelegt werden soll        |
+-----------------------------------+-----------------------------------+
| Source Address                    | Bestimmt die ausgehende           |
|                                   | IP-Adresse (host)                 |
+-----------------------------------+-----------------------------------+
| Destination Address               | Bestimmt die Ziel IP-Adresse      |
|                                   | (host)                            |
+-----------------------------------+-----------------------------------+
| Port                              | Gibt den Source / Destination     |
|                                   | Port an (ANY = Alle)              |
+-----------------------------------+-----------------------------------+
| Protokoll                         | Das verwendete Protokoll = tcp,   |
|                                   | udp, icmp (ping)                  |
+-----------------------------------+-----------------------------------+
| Interface                         | Gibt das Interface an, auf das    |
|                                   | die Regel wirken soll             |
+-----------------------------------+-----------------------------------+
| NAT                               | Network Address Translation /     |
|                                   | Maskierung der Adresse            |
+-----------------------------------+-----------------------------------+
| Action                            | Gibt an, ob Erlaubt (Accept) oder |
|                                   | Verbot (Drop) oder Loggen (LOG)   |
+-----------------------------------+-----------------------------------+

Für die Felder **Source Address** und **Destination Address** können
auch in der HOSTS gespeicherte Hostnamen eingetragen werden. Die Box
macht eine automatische Namensauflösung.

.. _Services:

Services
~~~~~~~~

Die unter **Port** auswählbaren Services (Dienste) sind unter
*Einstellungen → Iptables: Services* gespeichert und können beliebig
erweitert werden. Dabei bitte den folgenden Syntax verwenden:

.. code:: bash

   Service:Port   z.B. SSH:22

.. _Rules:

Rules
~~~~~

Die Regeln werden fest in den Flash-Speicher der Box gespeichert und
gehen also nicht verloren. Diese Regel-Liste kann auch unter
*Einstellungen → Iptables: Rules* händig verändert werden. Beim
speichern dieser Liste werden die regeln sofort angewendet.

.. _LöschenvonRegeln:

Löschen von Regeln
~~~~~~~~~~~~~~~~~~

Regeln können entweder über den *Remove* Link rechts neben der
entsprechenden Regel gelöscht werden, oder manuell unter *Einstellungen
→ Iptables: Rules*

.. _ZuBeachten:

Zu Beachten
-----------

In diversen Foren kursiert die Halbwahrheit, dass IPTables instabil sei
und die Box zu unprovozierten Reboots verleitet. Dies ist so nicht ganz
korrekt: IPTables selbst läuft stabil. Die Probleme werden durch das
**conntrack** Modul verursacht, sofern es geladen ist. Da es für die
allgemeine Funktion von IPTables jedoch nicht unbedingt benötigt wird,
muss man es auch nicht installieren.

|Warning| Bei der Auswahl von iptables-cgi in ``make menuconfig`` wird
*conntrack* u.U. rekursiv mit ausgewählt. Man kann es jedoch manuell
abwählen, sodass dessen Installation unterbleibt.

-  Tags
-  `cgi </tags/cgi>`__
-  `firewall </tags/firewall>`__
-  `network </tags/network>`__
-  `packages <../packages.html>`__
-  `routing </tags/routing>`__
-  `security </tags/security>`__

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

