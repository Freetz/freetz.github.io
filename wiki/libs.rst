.. _Bibliothekenlibraries:

Bibliotheken (libraries)
========================

.. _AbwählenvonBibliotheken:

Abwählen von Bibliotheken
-------------------------

Bibliotheken (im Nachfolgenden "libs" genannt") zu Paketen, die
abgewählt wurden, werden nicht automatisch mit abgewählt. Um nach der
Abwahl diverser Pakete auch die nicht mehr benötigten libs zu entfernen
(damit das Image nachher auch tatsächlich nicht zu groß wird) gibt es
folgende *make*-Targets:

.. code:: bash

   # Unnötige Libs und Busybox-Applets deselektieren
   make config-clean-deps

   # Oder nur unnötige Libs deselektieren, Busybox-Applets in Ruhe lassen
   make config-clean-deps-keep-busybox

.. _ListederBibliotheken:

Liste der Bibliotheken
----------------------

Bibliotheken, die als "ex" (external) markiert sind, lassen sich
wahlweise direkt in das Firmware-Image einbauen - oder aber "nach extern
auslagern" (z.B. auf einen USB-Stick). "St" beschreibt den aktuellen
Stand (Status) der Einbindung in Freetz (|{*}| stable, |{o}| testing,
|<!>| unstable), und ist nicht unbedingt immer aktuell (den aktuelleren
Status erkennt man daran, wo das Paket letztendlich in
`menuconfig <help/howtos/common/install/menuconfig.html>`__ auftaucht.

+-------------+-------------+-------------+-------------+-------------+
| **Paketname | **Beschreib | **ex**      | **St**      | **Größe**   |
| **          | ung**       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| `ftdi <libs | ftdi        |             | |{o}|       |             |
| /ftdi.html> | drivers for |             |             |             |
| `__         | RS-232-USB  |             |             |             |
|             | adapters    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

-  Tags
-  `libs <libs.html>`__

.. |{*}| image:: ../chrome/wikiextras-icons-16/stable.png
.. |{o}| image:: ../chrome/wikiextras-icons-16/testing.png
.. |<!>| image:: ../chrome/wikiextras-icons-16/exclamation-red.png

