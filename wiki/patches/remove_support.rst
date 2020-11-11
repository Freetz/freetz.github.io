.. _Removethesupport-files:

Remove the support-files
========================

Entfernt die support-files, welche man über die URL
`​http://fritz.box/html/support.html <http://fritz.box/html/support.html>`__
generieren und abspeichern kann.

.. _Waswirdentfernt:

Was wird entfernt?
------------------

| Mit dem Patch wird neben dem Code zur Generierung der support-files
  auch die entsprechende Webseite im AVM WebGUI entfernt.
| Wenn man o.g. Link nach Entfernung der support-files aufruft, kommt
  eine Meldung, dass die URL nicht gefunden werde:

   | **FRITZ!Box:**
   | Die angegebene URL wurde nicht gefunden.
   | Sie werden auf die Startseite der FRITZBox weitergeleitet.
   | Falls Sie nicht automatisch auf die Startseite der FRITZBox
     weitergeleitet werden, klicken Sie `​hier <http://fritz.box>`__.

… und wird wieder auf die Startseite des AVM WebGUIs umgeleitet.

-  Tags
-  `patches <../patches.html>`__
