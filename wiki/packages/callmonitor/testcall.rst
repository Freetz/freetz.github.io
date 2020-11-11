.. _Testanruf:

Testanruf
=========

Nachdem die `Listeners <listeners.html>`__ definiert sind, empfiehlt es
sich, sie auf korrekte Funktion zu testen. Da man nicht immer jede
Konfiguration mit echten Anrufen testen kann, gibt es eine Seite im
Web-Interface, die Anrufe simuliert. Dabei klingeln keine Telefone, es
wird lediglich dem CallMonitor ein Anruf vorgetäuscht, den er wie einen
echten Anruf behandelt.

.. figure:: /screenshots/22.png
   :alt: Callmonitor: Testanruf

   Callmonitor: Testanruf

| 

Die Maske sollte weitgehend selbsterklärend sein. Unter "Ereignis" kann
man einstellen, welches `Ereignis <listeners.html#Format>`__ simuliert
werden soll. Die Quellrufnummer ist diejenige, von der dieses Ereignis
ausgeht und die Zielrufnummer diejenige, die das Ziel des Ereignisses
ist. Man gibt jeweils ein Ereignis mit Rufnummern ein, die zu einem in
den Listeners definierten Muster passen. Nach einem Klick auf
"Testanruf" sollte der Callmonitor nun die zu diesem Listener-Eintrag
gehörende Aktion ausführen. Im Webinterface werden die
Debug-Informationen des Callmonitors angezeigt, die bei einer
eventuellen Fehlersuche helfen.

-  Tags
-  `callmonitor </tags/callmonitor>`__
