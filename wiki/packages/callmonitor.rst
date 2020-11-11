.. _Callmonitor:

Callmonitor
===========

Der Callmonitor ermöglicht es, bei eingehenden Anrufen auf einer
FritzBox beliebige `Aktionen <callmonitor/actions.html>`__ auszuführen,
abhängig davon, wer wen anruft. Beliebt sind das Senden von
Benachrichtigungen an verschiedenste Arten von "Boxen" (TV/Sat-Receiver,
Spielekonsolen, PCs) oder das Aufwecken von Geräten (Wake on LAN).

Dabei kann über eine Rückwärtssuche in Internet-Telefonbüchern oft auch
der Name des Anrufers angezeigt werden.

Das Besondere an diesem Callmonitor (leider gibt es viele Projekte mit
ähnlichem Namen) ist, dass er komplett auf der Fritzbox läuft; es ist
also nicht nötig, weitere Rechner eingeschaltet zu haben.

.. _Installation:

Installation
------------

.. figure:: /screenshots/6.png
   :alt: Callmonitor WebInterface

   Callmonitor WebInterface

Der Callmonitor ist als Paket im Rahmen von `Freetz <../index.html>`__
(`​Forum <http://www.ip-phone-forum.de/showthread.php?t=85371>`__)
realisiert, und kann bei dessen Installation einfach ausgewählt werden.

Das Callmonitor-Paket kann nicht als `Addon-Paket
installiert <../help/howtos/development/install_addon.html>`__ werden.

.. _InstallationneuerVersionen:

Installation neuer Versionen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bitte beachtet: Mit Freetz 1.1 können nur Callmonitor-Version bis 1.15
eingesetzt werden. Callmonitor 1.15.1 und höher benötigen Änderungen,
die in Freetz 1.2 oder der Freetz-Entwicklerversion enthalten sind.

Zum Einbinden der aktuellsten Version aus der Entwicklerversion in
Freetz 1.2 kann man so vorgehen (im Wurzelverzeichnis von Freetz):

.. code:: bash

   svn switch http://svn.freetz.org/trunk/make/callmonitor/callmonitor.mk make/callmonitor/callmonitor.mk

.. _Konfiguration:

Konfiguration
-------------

Zur Konfiguration gibt es im Web-Interface von Freetz mehrere neue
Seiten, darunter:

-  `Pakete/Callmonitor <callmonitor/config.html>`__: Optionen zum
   Startverhalten, zur
   `Rückwärtssuche <callmonitor/reverse_search.html>`__ etc.
-  `Einstellungen/Regeln <callmonitor/listeners.html>`__: Die
   `Aktionen <callmonitor/actions.html>`__, die bei bestimmten Mustern
   von Quell- und Zielrufnummer ausgeführt werden sollen.
-  `Einstellungen/Telefonbuch <callmonitor/phonebook.html>`__: Das
   dauerhaft (im Flash) gespeicherte Telefonbuch. Dies kann zusätzlich
   zum AVM-Telefonbuch verwendet werden.

Außerdem lässt sich über das Web-Interface die Regelmenge mit
vorgetäuschten `Testanrufen <callmonitor/testcall.html>`__ testen (es
wird bei euch nicht klingeln; die Testanrufe sieht nur der Callmonitor).
Das ist recht praktisch bei der Fehlersuche. Es existiert außerdem noch
eine Seite zur `Wartung <callmonitor/maintenance.html>`__ des
Telefonbuchs.

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

-  `FAQ <callmonitor/faq.html>`__
-  `​Entwicklungsseite bei
   Sourceforge <http://sourceforge.net/projects/callmonitor/>`__
-  `​Forumsseite für Fragen und
   Diskussionen <http://www.ip-phone-forum.de/showthread.php?t=191723>`__

-  Tags
-  `packages <../packages.html>`__
-  `phone </tags/phone>`__
