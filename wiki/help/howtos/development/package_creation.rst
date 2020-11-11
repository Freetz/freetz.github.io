**Diese Beschreibung ist höchstwahrscheinlich nicht das Gesuchte,
Verwendung auf eigene Gefahr!
**\ `Hier gibt es eine Beschreibung zur Erstellung eines Pakets für ein
fertiges
Programm <developer_information/package_development_start.html>`__

.. _WiebaueicheineigenesPaketfürFreetz:

Wie baue ich ein eigenes Paket für Freetz?
==========================================

Anmerkung: Dieser Beitrag Beitrag vermischt zwei verschiedenen
Fragestellungen:

-  Wie schreibe ich mein erstes Programm?
-  Wie integriere ich ein vorhandenes Programm als Package in Freetz?

Die zweite Frage wird schon an anderer Stelle behandelt. Wenn Interesse
an der ersten Frage besteht, sollte man das entsprechend aufteilen.
Normalerweise werden eher fertige Programme in Freetz integriert und
nicht welche, die komplett neu geschrieben werden. Als Grundlage für ein
komplexeres Programm ist möglicherweise `​GNU
Hello <http://ftp.gnu.org/gnu/hello/hello-2.3.tar.gz>`__ besser
geeignet, da hier auch mit automake eine cofigure-Datei erstellt wird.
(ralf)

Da dies mein erster Wiki-Eintrag ist, möchte ich Euch um Nachsicht
bitten, wenn nicht gleich alles so aussieht wie es sein sollte.

Um für Freetz ein Paket selbst zu erstellen, musste ich erst einmal ein
geeignetes "Projekt" finden, für das es auch Sourcecode gibt, der sich
für die Fritzbox überhaupt kompilieren lässt.

Bei der Suche stieß ich auf den `​HTTP Tunnel
Server <http://www.nocrew.org/software/httptunnel.html>`__. Mit
*httptunnel* kann man TCP-Verbindungen über das http-Protokoll tunneln
und damit von überall sogar durch sehr restriktive Proxies Zugriff zu
seiner Fritzbox bekommen. Näheres dazu ist
`​hier <http://linuxwiki.de/HttpTunnel>`__ nachzulesen.

Die Evolution meiner Erfahrungen, bereichert um zahlreiche hilfreiche
Tipps und Hinweise der Linux-Gurus und Entwickler hier im Forum könnt
Ihr in `​diesem
Thread <http://www.ip-phone-forum.de/showthread.php?t=167980>`__
nachlesen, wo auch der richtige Platz für weitere Fragen und Diskussion
ist.

Folgende Umgebung habe ich zum Bau des Pakets verwendet:

-  Fritzbox 7170 mit Freetz-1.0
-  StinkyLinux 1.06 in einer VM auf einem Macbook

Es gibt aber auch noch andere Umgebungen, um FW bzw. Freetz-Pakete zu
bauen, welche `hier <../common/install.html>`__ nachzulesen sind.

In den `HowTos <../../howtos.html>`__ gibt es einige wichtige
Informationen darüber, was man mit *Make*-Targets wie
`menuconfig <../common/install/menuconfig.html>`__, *toolchain*,
*precompiled*, *recover* usw. erreichen kann beim Bau einer
`Freetz <../../../freetz.html>`__-Firmware. Die Infos dort sind durchaus
lesenswert, wenn man besser verstehen will, was genau beim Bau einer FW
bzw. eines neuen Pakets für Freetz abläuft, wenngleich ich diese Infos
auch erst hinterher gelesen habe (mea culpa).

Eine sehr gute Anleitung ist
`hier <developer_information/package_development_start.html>`__ zu
finden.

Es gibt ein kleines Demo Package (demopackagea). Weiteres dazu hier:

`DemoPackageA <../../../packages/DemoPackageA.html>`__ Ein Demo-Package
"Hello World" —- `​Forum-Beitrag incl.
Download <http://www.ip-phone-forum.de/showthread.php?t=177052>`__

Kurz-Anleitung um ein bestehendes Package anzupassen

-  Annahme es ist ein Build-System vorhanden. Dies kann das oben
   genannte StinkyLinux, in dem Freetz ausgecheckt wurde, sein. Alle
   hier genannten Verzeichnisse sind im Freetz-Ordner, dieser wird im
   folgenden Kurz-Anleitung mit "/" Symbolisiert.
-  Es gibt ein kompaktes Package mit dem Namen: "Empty". Hierbei handelt
   es sich um ein konkretes Package, das man als Vorlage nutzen kann.
   Dies einfach mal ansehen. ("freetz.ordner"/make/empty/\* ).
-  Einen kurzen prägnanten Namen für das eigene Package ausdenken.
-  In dem Verzeichnis "make" einen Ordner erstellen. Dieser Ordner
   sollte so heißen wie das Package, dieser wird im folgenden
   Package-Ordner genannt.
-  Von dem "Empty-Package" die Datei "empty.mk" in den Package-Ordner
   übernehmen (und natürlich umbenennen. Der Name dieser Datei bestimmt
   den Namen des Packages).
-  Die Datei "package.mk" muss auch Inhaltlich angepasst werden. (In der
   Datei sollte kein "empty" (CASE-LESS) mehr stehen). Die Version
   sollte man auf "0.0.01" ändern. Der SITE-Eintrag ist nicht relevant,
   solange sich die Datei im Verzeichnis /dl befindet. Wenn man später
   die Datei zum `Download <../../../Download.html>`__ anbietet, muß
   hier der entsprechende Wert eingetragen werden.
-  Die Dateien "Config.in" und "Makefile.in" anpassen, aber nicht
   umbenennen.
-  Damit das Package über "make menuconfig" gefunden werden kann muss in
   der Datei /make/Config.in das eigene Package eingetragen werden (Wie
   z.B. das Package empty eingetragen ist). Für ein neues Package ist
   erstmal der Bereich "Testing" angemessen.
-  make menuconfig aufrufen und das Package auswählen.
-  Jetzt kennt Freetz das Package, es muss aber noch erstellt werden.
   Dieses Mini-Package besteht aus zwei Dateien (pluginName.c und
   Makefile)
-  Erstelle einen Ordner (egal wo wird gleich wieder gelöscht) der Name
   des Orders muss "pluginName-Version" lauten. (Version=0.0.01)
-  Erstelle in diesem Ordner die Datei "pluginName.c" mit dem Inhalt:

   ::

      /*  "plugin_name".c Version:0.0.01  */
      #include <stdio.h>

      main(){
       printf("Hello World \n");
      }

-  Erstelle in diesem Ordner die Date Makefile mit dem Inhalt:

   .. code:: bash

      BINARY=plugin_name
      OBJS=plugin_name.o

      all: $(BINARY)

      $(BINARY): $(OBJS)

      clean:
          $(RM) $(BINARY) $(OBJS)

-  wechsle eine Verzeichnisebende runter
-  erstelle ein tgz Archiv (der Ordner kann danach gelöscht werden)(tar
   cfz plugin-0.0.01.tgz plugin-0.0.01)
-  kopiere das tgz Archiv in das Verzeichnis /dl
-  Jetzt kann das Package mittels make Packagename-precompiled das erste
   Mal erzeugt werden (aus: "/")

to be continued…
