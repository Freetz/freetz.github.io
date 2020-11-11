.. _Funktionsweise:

Funktionsweise
==============

.. figure:: /screenshots/39.gif
   :alt: Freetz Menü

   Freetz Menü

Der Einstieg in die Rudi-Shell erfolgt in Freetz übers Hauptmenü (siehe
Bild). Direkt kann sie ebenfalls erreicht werden, und zwar über
`​http://fritz.box:81/cgi-bin/rudi_shell.cgi <http://fritz.box:81/cgi-bin/rudi_shell.cgi>`__.

Die Oberfläche präsentiert sich spartanisch, aber funktionell und
besteht aus folgenden Elementen:

-  Mehrzeiliges **Eingabefenster** für
   `​UNIX-Shell <http://de.wikipedia.org/wiki/Unix-Shell>`__-Skripte.
   Verwendet wird die auch von der Original-Firmware bekannte
   Standard-Shell ``/bin/sh`` der Busybox, die
   `​ash <http://en.wikipedia.org/wiki/Almquist_shell>`__ (eine
   `​Bourne-Shell <http://de.wikipedia.org/wiki/Bourne_Shell#Die_Bourne-Shell>`__-Variante).
-  **Ausführen-Knopf**, um die Skripten zur FritzBox zu schicken und
   dort auszuführen.
-  **Ergebnis-Ausgabe** (scrollbar) im unteren Fensterbereich. Dorthin
   werden Standard- und Fehlerausgabe der Shell umgelenkt, sofern nichts
   anderes angegeben ist.
-  **Befehls-Historie**, bestehend aus einer numerierten Auswahlliste.
   #0 ist immer die zuletzt eigegebene Befehlsfolge, die höheren Nummern
   sind entsprechend ältere Skripten. Die Anzahl der Einträge ist
   grundsätzlich unbegrenzt. Sollte der Browser irgendwann langsamer
   werden, weil er zu viele Informationen puffert, einfach auf den
   **Löschen-Knopf** drücken.
-  `Download <../../Download.html>`__\ **-Schalter**, um die
   Befehls-Ausgabe anstatt auf der Konsole als Datei zu empfangen.
   Normalerweise hat der `Download <../../Download.html>`__ den (im
   Speichern-Dialog des Browsers änderbaren) Namen *rudi_download*.
-  Kreuzt man zusätzlich einen der **Dateiendung-Schalter (.tar, .gz)**
   an, wird die entsprechende Endung (oder beide zusammen, also .tar.gz)
   an den Namensvorschlag angehängt. Das dient nur zur Bequemlichkeit,
   man kann es auch selbst beim Speichern machen. Für Benutzer mit
   `Download <../../Download.html>`__-Manager und ausgeschaltetem
   Speichern-Dialog ist es so ein bißchen einfacher. |Warning| Achtung: Die
   Schalter ändern *nicht* das Dateiformat, nur die Dateiendung.
-  **Datei-Uploads** werden über die beiden Textfelder "Quelldatei" und
   "Zieldatei" abgewickelt. Die Quelldatei kann mit "Durchsuchen" direkt
   über einen Datei-Browser ausgewählt werden, die Zieldatei hat den
   änderbaren Vorschlagsnamen ``/var/tmp/rudi_upload``. Es sollte
   natürlich ein existierendes, beschreibbares Verzeichnis gewählt
   werden. Ein nicht existierendes kann ja vorher über die
   Befehlseingabe erzeugt werden. |Warning| **Achtung:** Bitte nicht
   versuchen, Dateien nach ``/var/flash`` hochzuladen. Immer erst
   temporär woanders speichern und mittels ``cat`` ins *tffs* schreiben!
   |Warning|

|Warning| **Achtung, besonders wichtig: Die Rudi-Shell, insbesondere die
Historie, funktioniert ohne Navigation auf der Hauptseite. D.h., Sie
brauchen weder die Schaltflächen "Vor/Zurück" noch "Neu laden" des
Browsers. Im Gegenteil, wenn Sie sie benutzen, werden erstens die
Historie gelöscht und zweitens alle Schalter und Textfelder auf ihre
Standardwerte zurückgesetzt.** |Warning| *Für die Techniker unter uns:
Alles, was an Rudi-Shell dynamisch ist, passiert in einem unsichtbaren
IFrame bzw. auf der Hauptseite durch javascript-basierte Änderungen am
DOM der Seite.*

-  Tags
-  `rudi-shell </tags/rudi-shell>`__

.. |Warning| image:: ../../../chrome/wikiextras-icons-16/exclamation.png

