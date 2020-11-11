.. _Troubleshooting:

Troubleshooting
---------------

.. _Troubleshooting.config:

Troubleshooting .config
~~~~~~~~~~~~~~~~~~~~~~~

| Je nach Änderungen am Buildsystem und Config-Variablen kann eine
  existierende (alte) ``.config`` Datei eingeschränkt oder garnicht mehr
  verwendet werden.
| Mögliche Abhilfe:

.. code:: bash

   $ yes "" || make oldconfig <--- Alte .config Datei auffrischen
   oder
   $ make menuconfig          <--- Ggf. .config Datei neu erstellen

.. _TroubleshootingBuild-Abbruch:

Troubleshooting Build-Abbruch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Warning| Sollte während des Build-Prozesses ein Abbruch auftreten, so kann
man versuchen diese Strategien anzuwenden:

Einzelnes Paketes erneut erstellen:

.. code:: bash

   $ make iptables-dirclean     <--- Sourceverzeichnis eines problematischen Package löschen (hier: iptables)
   weiter mit
   $ make iptables-precompiled  <--- Versuchen problematisches Package von Anfang neu zu bauen

Von Anfang neu bauen:

.. code:: bash

   $ make dirclean          <--- Source-Verzeichnisse aller bisher erstellter Software löschen
   weiter mit
   $ make                   <--- Versuchen problematische Software von Anfang neu zu bauen

Bei Nichterfolg können `Wiki, Forum und
IRC <../index.html#WikiForumundIRC>`__ genutzt werden, um das Problem
weiter zu behandeln.

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

