.. _DynamischeBandbreitenanzeigeperSVG:

Dynamische Bandbreitenanzeige per SVG
=====================================

Bei dd-wrt und OpenWRT gibt's ein putziges SVG, das den aktuellen
Durchsatz der verschiedenen Interfaces anzeigt - In/Out mit Werten und
als Graphik, jede Sekunde aktualisiert. Firefox zeigt SVG an, aber auch
z.B. Opera 9.51 für Windows Mobile. Mit winzigen Änderungen läuft das
auch auf Freetz, ausgeführt vom busybox-httpd.

.. _AnleitungzurTest-Installation:

Anleitung zur Test-Installation
-------------------------------

#. Das
   `​graph_if.tar.gz <http://www.ip-phone-forum.de/attachment.php?attachmentid=28097&d=1220733960>`__
   auf die Box übertragen und irgendwo auspacken:

   ::

      tar xzf graph_if.tar.gz

   Dadurch wird ein Unterverzeichnis graph_if erstellt.

#. In das Verzeichnis wechseln und den BusyBox-httpd auf einem freien
   Port starten:

   ::

      cd graph_if
      httpd -f -v -p 83

   Wenn es dann läuft, kann man das -f -v weglassen.

#. Jetzt sollte beim Aufruf von
   `​http://fritz.box:83/cgi-bin/graph_if_svg.cgi?eth0 <http://fritz.box:83/cgi-bin/graph_if_svg.cgi?eth0>`__
   der Graph für die Schnittstelle ``eth0`` zu sehen sein. Die anderen
   Interfaces kann man sehen, wenn man sie in der URL statt eth0 angibt.
#. Eine Test-HTML-Seite, auf der alle Interfaces ausser lo angezeigt
   werden, findet sich unter
   `​http://fritz.box:83/cgi-bin/all_ifs.cgi <http://fritz.box:83/cgi-bin/all_ifs.cgi>`__

Zu Testzwecken kann man als Parameter "object", "embed" oder "iframe"
angeben, dann werden die SVG-Graphen in die entsprechenden Tags gehüllt.
"iframe" ist der Default.

*(Quelle:*\ `​IPPF
Thread <http://www.ip-phone-forum.de/showthread.php?t=174653>`__\ *)*

-  Tags
-  `howtos </tags/howtos>`__
-  `install </tags/install>`__
