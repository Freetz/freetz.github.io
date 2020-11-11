**This package was removed in**\ `r1823 </changeset/1823>`__\ **!**

.. _Mediaserver:

Mediaserver
===========

Der Mediaserver kann mittels Freetz aus der Labor-Version von AVM
extrahiert und in andere Firmwares integriert werden. AVM beschreibt den
Server als
`​FRITZ!Musikbox <http://www.avm.de/de/Service/Service-Portale/Service-Portal/Labor/labor_download_usb_host/labor_download_usb_host.php>`__
- im Grunde ist es aber "nur" ein UPnP-Mediaserver, welcher Mediendaten
(in diesem Fall MP3s) an kompatible Hard- und Software streamt.

Wer den *Mediaserver* in der Firmware seiner FritzBox hat, ihn aber gar
nicht benötigt, kann ihn auch mit einem
`Patch <../patches/remove_mediasrv.html>`__ aus selbiger entfernen
lassen. Er macht ja z.B. keinerlei Sinn, wenn auf der Box gar keine
Media-Dateien (MP3 etc.) vorhanden sind, und mangels angeschlossenem
Storage auch gar kein Platz für selbige vorhanden wäre.

.. _Funktionsweise:

Funktionsweise
--------------

Sobald ein USB-Massenspeicher mit FAT32-Dateisystem von der FritzBox
erkannt wird, wird über die storage-Konfig des Hotplug-Daemons der
Mediaserver gestartet. Der FTP-Server läuft weiterhin, der Mediaserver
verlinkt sogar auf das Verzeichnis des FTP-Servers.

In der Ereignisanzeige sollte folgende Meldung erscheinen:

.. code:: bash

   Mediaserver mit xx Mediendateien gestartet. Alle Mediendateien stehen zur Verfügung.

Mit den entsprechenden UPnP-Clients kann dann auf die MP3s zugegriffen
werden.

.. _Dateien:

Dateien
-------

Folgende Dateien gehören zum Mediaserver-Paket:

+-----------------------------------+-----------------------------------+
| \|Datei                           | \|Zweck                           |
+-----------------------------------+-----------------------------------+
| ``/sbin/start_mediasrv``          | Prüft verschiedene Ordner, setzt  |
|                                   | einen Link von /var/media/ftp auf |
|                                   | /var/media/mediapath, startet den |
|                                   | Mediaserver.                      |
+-----------------------------------+-----------------------------------+
| ``/sbin/stop_mediasrv``           | Stoppt den Mediaserver.           |
+-----------------------------------+-----------------------------------+
| ``/sbin/mediasrv``                | Das eigentliche Server-Binary.    |
+-----------------------------------+-----------------------------------+
| ``/usr/lib/mediasrv/ConnectionMan |                                   |
| ager.xml``                        |                                   |
+-----------------------------------+-----------------------------------+
| ``/usr/lib/mediasrv/MediaServerDe |                                   |
| vDesc-template.xml``              |                                   |
+-----------------------------------+-----------------------------------+
| ``/usr/lib/mediasrv/mediapath``   |                                   |
+-----------------------------------+-----------------------------------+
| ``/usr/lib/mediasrv/MediaServerDe |                                   |
| vDesc.xml``                       |                                   |
+-----------------------------------+-----------------------------------+
| ``/usr/lib/mediasrv/ContentDirect |                                   |
| ory.xml``                         |                                   |
+-----------------------------------+-----------------------------------+
| ``/etc/default.Fritz_Box_7170/{av |                                   |
| m,1und1,freenet}/ConnectionManage |                                   |
| r.xml``                           |                                   |
+-----------------------------------+-----------------------------------+
| ``/etc/default.Fritz_Box_7170/{av |                                   |
| m,1und1,freenet}/MediaServerDevDe |                                   |
| sc-template.xml``                 |                                   |
+-----------------------------------+-----------------------------------+
| ``/etc/default.Fritz_Box_7170/{av |                                   |
| m,1und1,freenet}/mediapath``      |                                   |
+-----------------------------------+-----------------------------------+
| ``/etc/default.Fritz_Box_7170/{av |                                   |
| m,1und1,freenet}/MediaServerDevDe |                                   |
| sc.xml``                          |                                   |
+-----------------------------------+-----------------------------------+
| ``/etc/default.Fritz_Box_7170/{av |                                   |
| m,1und1,freenet}/ContentDirectory |                                   |
| .xml``                            |                                   |
+-----------------------------------+-----------------------------------+

Außerdem werden verschiedene Bibliotheken benutzt, die auch in normalen
Firmware enthalten sind (z.B. für UPnP oder HTTP), und verschiedene
Skripte prüfen, ob ein Mediaserver in der Firmware enthalten ist und
reagieren entsprechend.

.. _KompatibleClientsAuswahl:

Kompatible Clients (Auswahl)
----------------------------

.. _Software:

Software
~~~~~~~~

-  Itunes
-  Windows Mediaplayer 11

.. _Hardware:

Hardware
~~~~~~~~

-  Roku Soundbridge
-  Terractec Noxon
-  Pinnacle Systems Soundbridge

.. _Firmware-Kompatibilität:

Firmware-Kompatibilität
-----------------------

Ein extrahierter Mediaserver lässt sich nicht wahllos mit jeder anderen
Firmware kombinieren, zum einen müssen verschiedene Scripte für das
Starten des Mediaservers schon vorbereitet sein, zum anderen müssen die
Bibliotheken der beiden Firmwares kompatibel sein, da verschiedene
Querabhängigkeiten existieren.

Der Mediaserver aus der Laborversion 29.04.95-7553 funktioniert z.B. mit
den stabilen Firmwares 29.04.37 und 40.04.37.

Der Mediaserver aus 29.04.95-8221 geht mit den beiden obigen Firmwares
nicht, dafür aber mit der 29.04.39.

-  Tags
-  `audio </tags/audio>`__
-  `network </tags/network>`__
-  `packages <../packages.html>`__
