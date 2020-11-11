.. _Ruby:

Ruby
====

`​Ruby <http://www.ruby-lang.org/de/>`__ ist eine dynamische
Programmiersprache mit dem Fokus auf Produktivität und Einfachheit. Es
verfügt über eine elegante Syntax, die sich natürlich liest und einfach
zu schreiben ist. Und dann ist das Ganze natürlich auch noch Open
Source…

Das *Ruby* Paket enthält:

-  den *Ruby* Interpreter (ca. 800kb "stripped size")
-  die interaktive *Ruby* Konsole (``irb``)
-  das komplette *Ruby*
   `​API <http://de.wikipedia.org/wiki/Programmierschnittstelle>`__ -
   also alle ``*.rb`` Module (ca. 4.7MB)
-  alle zugehörigen ``*.so`` Erweiterungs-Bibliotheken (ca. 1MB)
   *Diese können auch statisch gelinkt oder weggelassen werden, aber
   dafür gibt es (noch?) keinen Eintrag
   in*\ `menuconfig <../help/howtos/common/install/menuconfig.html>`__\ *.
   Wer dies also machen möchte, muss es "zu Fuß" nach den Angaben in der
   ``README`` Datei tun.*

Das summiert sich auf ca. 5.5MB für alle installierten Dateien, wobei
man ungewünschte noch manuell entfernen kann (dies muss nach
``make precompiled``, jedoch vor ``make`` passieren). Klingt jetzt echt
fett, aber: *Ruby* Module lassen sich wunderbar packen, so dass die
"volle Ladung" im gepackten Squash nur noch ca. 1.3MB Platz benötigt.
Wer also eine Box mit "mehr Speicher" (ab 8MB aufwärts) benutzt, kann
*Ruby* also durchaus auch in der Firmware selbst unterbringen. Naja,
u.U. muss dafür so einiges anderes weggelassen werden |:-)|

|Warning| **Achtung:** Auf dem "Build-Host" muss die gleiche *Ruby* Version
installiert sein, die man für die Box bauen möchte!

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

-  `​Ruby Homepage <http://www.ruby-lang.org/de/>`__
-  `​Wikipedia
   Artikel <http://de.wikipedia.org/wiki/Ruby_(Programmiersprache)>`__
-  `​WikiBooks: Ruby
   Programmierung <http://de.wikibooks.org/wiki/Ruby-Programmierung>`__

--------------

-  Tags
-  `packages <../packages.html>`__
-  `programming </tags/programming>`__

.. |:-)| image:: ../../chrome/wikiextras-icons-16/smiley.png
.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

