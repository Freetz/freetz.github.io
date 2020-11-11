.. _SMStools3:

SMStools3
=========

.. figure:: /screenshots/251.jpg
   :alt: SMStools3

   SMStools3

Package um SMS mit einem UMTS-Stick zu versenden und zu empfangen.

|Warning| Falls die FritzBox UMTS-Unterstützung hat, am besten den umtsd
herauspatchen.

| SMStools3 kann komplett per Webif bedient werden oder alternativ per
  Terminal.

.. _Datenverzeichnis:

Datenverzeichnis
----------------

Das "Datenverzeichnis" legt man am besten auf einen USB-Stick, damit
keine SMS verloren gehen. Dennoch wird ein ``modsave`` beim Beenden des
Packages ausgeführt, falls der Pfad mit ``/tmp/flash`` beginnt.

.. _SendenundEmpfangenmitdemTerminal:

Senden und Empfangen mit dem Terminal
-------------------------------------

Eine SMS kann man diesem Befehl versendet werden, der Parameter
``flash`` ist optional:

.. code:: bash

   rc.smstools3 sendsms flash +497771234567 Text der Nachricht

Empfangene SMS können so aufgelistet angezeigt:

.. code:: bash

   rc.smstools3 listsms

.. _Weiteres:

Weiteres
========

-  Komplette Dokumentation:
   `​http://smstools3.kekekasvi.com/ <http://smstools3.kekekasvi.com/>`__
-  Falls der Stick nicht richtig erkannt wird, sondern nur als
   Datenträger: `wiki:/packages/ppp#Weiteres <ppp.html#Weiteres>`__

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

