.. _Tabellen:

Tabellen
========

Auch hier haben wir dem "schnöden Standard" ein wenig nachgeholfen - und
so gibt es verschiedene Möglichkeiten der Tabellen-Formatierung. Den
einzelnen Details möchte ich eine kurze Übersicht voranstellen:

.. _ÜberblickderverschiedenenFormate:

Überblick der verschiedenen Formate
-----------------------------------

.. _Standard:

Standard
~~~~~~~~

Den Standard haben wir ein klein wenig "aufgebohrt", sodass er im
Allgemeinen ausreichen sollte. Hier stehen innerhalb der einzelnen
Zellen alle Trac-Wiki Formatierungen zur Verfügung - dafür gestaltet es
sich etwas schwieriger, Zeilenumbrüche einzubringen oder Zellen zu
verbinden. Normalerweise ist dieses Format jedoch die erste Wahl.

.. _RST:

RST
~~~

`​Re-Structured Text <http://de.wikipedia.org/wiki/ReStructuredText>`__
bietet bei relativ einfacher Syntax zahlreiche zusätzliche
Formatierungsmöglichkeiten (siehe auch
`hier <../../WikiRestructuredText.html#BiggerReSTExample>`__. Dafür sind
innerhalb eines solchen Blocks keinerlei Wiki-Markups möglich - womit
RST für viele Dinge nicht in Frage kommt.

.. _MediaWiki:

MediaWiki
~~~~~~~~~

Da wir auch das `​MediaWiki
Plugin <http://trac-hacks.org/wiki/MediaWikiPluginMacro>`__ eingebunden
haben, bieten sich damit zahlreiche zusätzliche Möglichkeiten. Aber auch
hier gilt: Trac-Wiki Syntax ist innerhalb eines Media-Wiki Blocks nicht
möglich.

.. _Anwendung:WieerstelleicheineTabelle:

Anwendung: Wie erstelle ich eine Tabelle?
-----------------------------------------

.. _Standard1:

Standard
~~~~~~~~

Mit dem Trac-Wiki Standard (in gepatchter Form |;)|) ist dies am
einfachsten möglich:

.. code:: bash

   |||   ||| 1 ||| 2 ||| 3 ||
   ||| A ||  X ||    ||  X ||
   ||| B ||    ||  X ||    ||
   ||| C ||  X ||  X ||    ||

wird zu

+------+------+------+------+
| \|   | \| 1 | \| 2 | \| 3 |
+------+------+------+------+
| \| A | X    |      | X    |
+------+------+------+------+
| \| B |      | X    |      |
+------+------+------+------+
| \| C | X    | X    |      |
+------+------+------+------+

.. _RST1:

RST
~~~

Hier sieht das ein wenig anders aus:

.. code:: bash

   {{{
   #!rst
   =====  =====  ======
      Inputs     Output
   ------------  ------
     A      B    A or B
   =====  =====  ======
   False  False  False
   True   False  True
   False  True   True
   True   True   True
   =====  =====  ======
   }}}

Wird zu

Inputs

Output

A

B

A or B

False

False

False

True

False

True

False

True

True

True

True

True

.. _MediaWiki1:

MediaWiki
~~~~~~~~~

Hier haben wir auch wieder zahlreiche Möglichkeiten - von denen hier nur
zwei aufgezeigt werden sollen:

.. _EinfachesBeispiel:

Einfaches Beispiel
^^^^^^^^^^^^^^^^^^

Gibt man folgendes ein:

.. code:: bash

   {{{
   #!mediawiki
   {|class="table"
   |-
   ! Überschrift 1. Spalte
   ! Überschrift 2. Spalte
   |-
   | Inhalt 1.Zeile 1.Spalte
   | Inhalt 1.Zeile 2.Spalte
   |}
   }}}

kommt dabei das heraus:

+-------------------------+-------------------------+
| Überschrift 1. Spalte   | Überschrift 2. Spalte   |
+=========================+=========================+
| Inhalt 1.Zeile 1.Spalte | Inhalt 1.Zeile 2.Spalte |
+-------------------------+-------------------------+

.. _komplexeresBeispiel:

komplexeres Beispiel
^^^^^^^^^^^^^^^^^^^^

Zu guter Letzt ein leicht komplexeres Beispiel, bei dem einige
Formatierungen (Hintergrund-Farbe etc.) explizit mit vorgegeben, und
auch ein paar Zellen verbunden werden. Eingegeben wurde also:

.. code:: bash

   {{{
   #!mediawiki
   {|border="1" cellpadding="2px" style="border-collapse:collapse;border:1px solid #8cacbb;border-width:1px;"
   |-
   !background-color="#ff0"|'''Überschrift'''
   !background-color="#ff0"|'''Zweite Überschrift'''
   |-
   | Inhalt Zelle 1-1
   | Inhalt Zelle 1-2
   |-
   | colspan="2" align="center"|Verbundene Zellen zentriert
   |-
   | Inhalt Zelle 3-1
   | rowspan="2"|Verbundene Zelle
   |-
   | Inhalt Zelle 4-1
   |}
   }}}

Und dabei kam folgendes heraus:

**Überschrift**

**Zweite Überschrift**

Inhalt Zelle 1-1

Inhalt Zelle 1-2

Verbundene Zellen zentriert

Inhalt Zelle 3-1

Verbundene Zelle

Inhalt Zelle 4-1

-  Tags
-  `help <../../help.html>`__
-  `wikiedit </tags/wikiedit>`__

.. |;)| image:: ../../../chrome/wikiextras-icons-16/smiley-wink.png

