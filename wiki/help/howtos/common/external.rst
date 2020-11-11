.. _External:

External
========

.. figure:: /screenshots/118.jpg
   :alt: external menuconfig page

   external menuconfig page

Entstanden aus diesem Thread im IPPF:
`​http://www.ip-phone-forum.de/showthread.php?t=160920 <http://www.ip-phone-forum.de/showthread.php?t=160920>`__

| Mit "External" kann dem Platzproblem im Flash der Fritzboxen
  entgegengewirkt werden, man kann also ein größeres Image als das Flash
  zulassen würde installieren. Hierzu werden Packages, Librarys als auch
  benutzerdefinierte Dateien aus dem Image "externalisiert" oder
  ausgelagert. Bei Boxen mit USB-Host bietet sich hierzu ein
  angeschlossener USB-Stick an. Bei älteren Boxen können unter
  Zuhilfenahme des
  `Downloader-CGIs <../../../packages/downloader.html>`__ die Dateien
  von einem FTP- oder HTTP-Server in den RAM nachgeladen werden.
  Alternativ können die Dateien auch per
  `autofs <../../../packages/autofs.html>`__ eingebunden werden.
| Mit External kann man die Meldung `Filesystem image too
  big <../../../FAQ.html#Filesystemimagetoobig>`__ vermeiden.

| |Warning| Der Pfad zu den external-Dateien kann im Webinterface unter
  Freetz → Einstellungen → external konfiguriert werden.

In diesem dürfen sich keine andere Dateien befinden, dies könnte zu
`​Fehlern <http://www.ip-phone-forum.de/showthread.php?p=1469406#post1469406>`__
führen.

| |Warning| Es können nur Pakete ausgelagert werden, die zur Installation
  ausgewählt wurden.

.. _Konfiguration:

Konfiguration
=============

zu finden im menuconfig unter "Advanced Options" → "External"

.. _PreparefilesforDownloader:

Prepare files for Downloader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Diese Option ist nur zu sehen, wenn das Downloader-CGI zur
  Installation ausgewählt wurde.
| Es werden hiermit beim make-Prozess Pakete für den späteren
  `Download <../../../Download.html>`__ erstellt.
| Näheres hierzu beim
  `Downloader-CGI <../../../packages/downloader.html>`__.

.. _Keepsubdirectories:

Keep subdirectories
~~~~~~~~~~~~~~~~~~~

Die Verzeichnisstruktur der ausgelagerten Dateien wird beibehalten. Dies
hat den Vorteil dass eine gleichlautende Datei an verschiedenen Stellen
im Image ausgelagert werden kann. Ein Nachteil ist, dass das händische
Kopieren auf die Box umständlicher ist.

.. _Createfileforupload:

Create file for upload
~~~~~~~~~~~~~~~~~~~~~~

Alle ausgelagerten Dateien werden in eine Datei gepackt, die mittels
Freetz-Webinterface auf die Box geladen werden kann. Die Datei ist im
Verzeichnis .\ *image* zu finden und trägt den gleiche Namen wie das
erstellte Image, weist aber die Endung ".external" auf.

.. _ownfiles:

own files
~~~~~~~~~

Hier können noch zusätzliche Dateien zum auslagern angegeben werden. Es
ist der Pfad auf der Fritzbox anzugeben! Wenn es mehr als eine Datei
ist, sind diese mit einem Leerzeichen voneinander zu trennen.

.. _Auswahl:

Auswahl
=======

packages
~~~~~~~~

Hier können verschiedene "binary-only" Packages zum auslagern ausgewählt
werden. Es sollten alle unproblematisch sein.

services
~~~~~~~~

Hier können verschiedene automatisch startende Packages zum auslagern
ausgewählt werden.

|Warning| Diese werden erst geladen wenn der USB-Stick verfügbar ist und
die Option zum automatischen Starten von ausgelagerten Diensten im
Webinterface aktiviert ist.

libraries
~~~~~~~~~

Hier können verschieden Libraries zum auslagern ausgewählt werden.

|Warning| Zu beachten ist, dass Programme, die gegen diese gelinkt sind,
erst gestartet werden können, wenn die Datei auf der Box geladen ist.
Also vorher bitte die Abhängigkeiten prüfen.

.. _Installation:

Installation
============

Die Dateien, die für external ausgewählt wurden, müssen auf der Box
verfügbar gemacht werden.

Im Falle eines USB-Sticks sollte man bei der Konfiguration die Option
"Create file for upload" auswählen. Die damit erzeugte Datei kann man
über das installierte Freetz Webinterface System" → "Firmware-Update" →
Option "external-Datei hochladen" auf die Box kopieren.

Wenn man einen FTP/HTTP-Server oder einen NFS-Server verwendet, muß man
selbst dafür sorgen, daß die Box auf die Dateien zugreifen kann.

.. _AutomatischesstartenstoppenvonDiensten:

Automatisches starten/stoppen von Diensten
==========================================

| Dies kann im Webinterface unter ``Einstellungen`` konfiguriert werden.
  Dienste die hier eingetragen sind erscheinen im Webinterface nur
  solange der Datenträger mit den ausgelagerten Dateien zur Verfügung
  steht.
| Ansonsten müssten die Optionen selbsterklärend sein. Hier noch ein
  Screenshot davon:

.. figure:: /screenshots/175.jpg
   :alt: external_services

   external_services

| Unter ``Logdateien`` wird im Webinterface die
  ``/var/log/external.log`` angezeigt.
| In dieser bedeutet in den "Waiting" Zeilen jeder Punk, dass 1 Sekunde
  gewartet wurde. Falls es also "tausende" Punkte sind, behindert
  irgendetwas das saubere hochfahren der Box, vermutlich ein Timer in
  der rc.custom oder debug.cfg.

.. _Firmware-build-ProzessundUpdate:

Firmware-build-Prozess und Update
=================================

Beim Firmware-build werden zwei Dateien erzeugt: xxx.image → die
eigentliche Firmware-Image xxx.external → Die Dateien, die
externalisiert werden sollen

Beide Dateien sind im Ordner [images] zu finden. Bei der external-Datei
handelt es sich um eine gepackte tar-Datei, die beim Upload übers
Freetz-Webinterface automatisch ins Zielverzeichnis entpackt wird. Es
wird empfohlen, erst die external hochzuladen [Freetz-WebIf → System →
Firmware-Update] und danach erst die Firmware. So stehen die
external-Pakete der aktualisierten Firmware schon zur Verfügung.

-  Tags
-  `external </tags/external>`__

.. |Warning| image:: ../../../../chrome/wikiextras-icons-16/exclamation.png

