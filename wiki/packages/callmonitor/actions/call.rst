.. _AllgemeineHinweisezuFunktionsaufrufen:

Allgemeine Hinweise zu Funktionsaufrufen
========================================

Der Aufruf von Funktionen, die auf `getmsg <getmsg.html>`__ oder
`rawmsg <rawmsg.html>`__ basieren, sieht immer so aus:

.. code:: bash

     foomessage [OPTION]... <host> [<message>]...

Der einfachste und am meisten genutzte Fall ist dementsprechend

.. code:: bash

     foomessage <host>

Als Optionen können alle Optionen verwendet werden, die auch
`getmsg <getmsg.html>`__ bzw. `rawmsg <rawmsg.html>`__ verstehen.

Die Standard-Nachricht wird generell von einer Funktion mit der
Namenskonvention ``default_foomessage`` erzeugt und kann so einfach
überschrieben wird.

|<!>| Bei den Funktionen können eventuell Umgebungsvariablen verwendet
werden. Diese werden vor dem Funktionsaufruf gesetzt. Der Callmonitor
sorgt automatisch für die Kodierung der Umgebungsvariablen, die Text
enthalten (z.B. ``XBOX_CAPTION`` und ``DREAM_CAPTION``). Man kann also
einfach

.. code:: bash

     FOO_CAPTION="Dies ist der zu 100% richtige Titel" foomessage <host>

schreiben, ohne sich Gedanken über Kodierungen (URL- oder printf-)
machen zu müssen.

.. |<!>| image:: ../../../../chrome/wikiextras-icons-16/exclamation-red.png

