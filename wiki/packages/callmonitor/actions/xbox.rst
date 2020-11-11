.. _XBox:

XBox
====

Für diese Funktion muss das `​XBox Media Center
(XBMC) <http://www.xboxmediacenter.com>`__ laufen und dort unter
*Einstellungen → Netzwerk* der Webserver aktiviert werden. Ggf. mit den
Optionen (s.o.) Port, Username und Passwort übergeben. Das XBMC stellt
die Nachricht dann in einem kleinen Fenster dar, das automatisch
geschlossen wird.

.. code:: bash

     xboxmessage (default_xboxmessage)

Die XBox erlaubt mit ``xboxmessage`` keine Kommas in den Nachrichten.
Der Titel der Nachricht kann über die Umgebungsvariable
``XBOX_CAPTION="Telefonanruf"`` beeinflusst werden.

.. _AnpassungenaufderXBox:

Anpassungen auf der XBox
------------------------

Anzeigedauer und Größe des Fensters können in der Datei
``DialogKaiToast.xml`` angepasst werden. Je nach gewähltem TV-Typ ist
die jeweilige Datei unter ``skin\Project Mayhem III\PAL\`` oder
``skin\Project Mayhem III\PAL16x9\`` zuständig. Folgende Überarbeitung
der "PAL"-Datei erreicht ein brauchbares Ergebnis (nur geänderte
Zeilen):

.. code:: bash

   ...
     <coordinates>
       <system>1</system>
       <posx>275</posx>
       <posy>420</posy>
     </coordinates>
     <animation effect="slide" time="5000" start="300,0">WindowOpen</animation>
     <animation effect="slide" time="5000" end="300,0">WindowClose</animation>
   ...
       <control>
         <description>Popup Kai Toast Dialog Background</description>
         ...
         <width>400</width>
         <height>125</height>
   ...
       <control>
         <description>avatar</description>
         ...
         <posx>40</posx>
         <posy>25</posy>
   ...
       <control>
         <description>Caption Label</description>
         ...
         <posx>46</posx>
         <posy>30</posy>
         <width>305</width>
   ...
       <control>
         <description>Description Button</description>
         ...
         <posx>46</posx>
         <posy>46</posy>
         <width>305</width>
   ...

.. _WeitereMöglichkeiten:

Weitere Möglichkeiten
---------------------

Es gibt außerdem einen
`​Python-Script <http://ca.geocities.com/farside@rogers.com/Scripts/callerid.html>`__,
das eine CallerID-Anzeige auf der Xbox ermöglicht. Dann kann die
Nachricht mit der Funktion ``yac`` an die XBox gesendet werden. Das
Script ist auch im Script
`​xbmcfritz <http://www.xbmc.de/xbmc/download.php?view.150>`__
enthalten, das zusätzlich die Anruferliste der FritzBox auf der XBox
darstellen kann.
