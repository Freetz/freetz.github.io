.. _WassollteichbeiderErstellungeinesneuenTicketsbeachten:

Was sollte ich bei der Erstellung eines neuen Tickets beachten?
---------------------------------------------------------------

|Warning| **Grundsätzlich**: Das Bug-Tracking-System (BTS) ist primär für
**Bug-Reports** und **Erweiterungen** vorgesehen. **Support** gibt es im
`​IP-Phone-Forum
(IPPF) <http://www.ip-phone-forum.de/forumdisplay.php?f=525>`__ oder
`IRC <help/irc.html>`__.

-  Bitte nicht vergessen: Entwickler und User wollen sich einen
   **schnellen Überblick** im BTS verschaffen.
   Wir bitten um etwas Disziplin in den Kommentaren, da sonst die
   Lesebereitschaft und auch die Qualität des BTS leidet.

-  Vorsicht: Tickets können **nicht gelöscht** werden, daher bitte erst
   unten aufgelistete Punkte abklären, dann Ticket erstellen |:-)|.

-  Bitte prüfen **bevor** ein **neues Ticket** erstellt wird:

   -  **Reproduzierbarkeit**:
      Tritt der Fehler immer noch auf:

      -  wenn auf die aktuellste Revision aus dem SVN-Repository
         geupdatet wird (``svn up``)
      -  wenn nochmals frisch (Quellcode vorher löschen) ausgechecked
         wird?
      -  wenn anstatt alter exisitierender ".config" eine neue mittels
         ``make menuconfig`` erstellt wird?
      -  nach einem ``make dirclean`` oder ``make clean``?

   -  **IRC ##fritzbox**:
      Bitte nachfragen im offiziellen `IRC <help/irc.html>`__
      Support-Channel (evtl. lässt sich das Problem direkt im Chat
      lösen).
   -  **IPPF-Forum**: Zuerst das offizielle
      `​Forum <http://www.ip-phone-forum.de/forumdisplay.php?f=525>`__
      konsultieren (evtl. wurde dort schon das Problem geposted).
   -  Bitte auch die Liste der **offenen Tickets** `hier </report/9>`__
      inspizieren, um doppelte Einträge zu vermeiden.

-  Bitte einen **aussagekräftigen Titel** für das Ticket auswählen.
   Dieser sollte eine kurze und exakte Beschreibung des Problems
   enthalten.

-  Hilfreich zum **Eingrenzen des Problems** (Liste evtl.
   unvollständig). Im Falle eines Tickets vom Typ **defect** sind die
   hinten mit **[d]** markierten Punkte **zwingend notwendig**, Tickets
   ohne entsprechende Anhänge/Informationen werden kommentarlos als
   invalid geschlossen:

   -  FritzBox Modell (z.B. FRITZBox Fon WLAN 7170) **[d]**
   -  Firmware-Version (z.B. 29.04.87) **[d]**
   -  verwendete Freetz-Version bzw. SVN-Branch (z.B. trunk) und
      Revision (z.B. `r7300 </changeset/7300>`__) **[d]**
   -  nachvollziehbare Fehlerbeschreibung (siehe
      `​Fehlerberichte <http://www.chiark.greenend.org.uk/~sgtatham/bugs-de.html>`__
      und `​Wie man Fragen richtig
      stellt <http://www.tty1.net/smart-questions_de.html>`__)
   -  Beschreiben was man bisher versucht hat (mit und ohne Erfolg)
   -  Dateianhänge (bitte nicht als Verweis auf eine Pastebin-URL):

      -  Konfigurationsdatei ".config" aus dem Freetz
         Quellcode-Verzeichnis (z.B. als freetz-config.txt) **[d]**
      -  Output-Dateien von Debug-Werkzeugen wie strace, ltrace, lsof,
         gdb etc.
      -  Supportdatei (Freetz Webinterface → System → Supportdatei
         erstellen)

   -  Weitere wichtige Felder:

      -  Typ (Fehler, Erweiterung, Aufgabe oder Versionssprung)
      -  Komponente (betroffene Komponente)
      -  Die Felder Priorität und Meilenstein werden von den Entwicklern
         festgelegt.

-  Die Bereitstellung eines **Patch** kann die Fehlerbehebung unter
   Umständen erheblich beschleunigen.

   -  `Patch How-to <patch.html>`__ (noch Work-In-Progress)

-  **Rückmeldung und Testen** von bereitgestellten Patches und/oder
   Lösungsmöglichkeiten trägt zum erfolgreichen Abschluss eines Tickets
   bei.
   Bitte Aktivitäten im Ticket mitverfolgen, hilfreich "Watch page"
   Funktion.

-  TIPP: Beim **Editieren** gibt es eine Vorschau-Funktion
   (**Preview**). Bitte damit den Eintrag vorher testen und somit
   unleserliche Einträge vermeiden.

-  Werden die Daten im Ticket als "ungenügend" oder "formal falsch"
   betrachtet, so wird es auf Status "**invalid**" (ungültig) gesetzt.

-  Quellcode, Logausgaben usw in {{{ }}} einschließen, siehe
   `WikiFormatting <WikiFormatting.html>`__

`Neues Ticket erstellen </newticket>`__

.. |Warning| image:: ../chrome/wikiextras-icons-16/exclamation.png
.. |:-)| image:: ../chrome/wikiextras-icons-16/smiley.png

