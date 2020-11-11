.. _DGStationRelook400S:

DGStation Relook 400S
=====================

Die `​DGStation Relook 400S <http://www.dgstation.co.kr>`__ unterstützt
nur die Anzeige einer kurzen Zeile ohne Umlaute. Die Anzeigedauer kann
über die Umgebungsvariable ``RELOOK_TIMEOUT`` beeinflusst werden (in
Sekunden).

.. code:: bash

     relookmessage (default_relookmessage)

Beispiel für Benutzung mit veränderter Anzeigedauer (25 Sekunden):

.. code:: bash

     RELOOK_TIMEOUT=25 relookmessage 192.168.34.56
