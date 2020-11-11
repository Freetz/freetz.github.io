.. _RemoveFTPdeamonftpd:

Remove FTP deamon (ftpd)
========================

Mit diesem Patch wird AVMs FTP Daemon entfernt. Auch wenn die regulären
Optionen für diesen im AVM WebIF nach wie vor verfügbar bleiben, ist
nach dem Entfernen des FTP Daemons kein Zugriff auf angeschlossene
Laufwerke per FTP mehr möglich! Dieser kann jedoch auch per
`bftpd <../packages/bftpd.html>`__ bzw.
`vsftpd <../packages/vsftpd.html>`__ konfiguriert werden - vorausgesetzt
natürlich, diese Pakete wurden auch installiert.

|Warning| Der Patch ist nur auswählbar, wenn vorher die Option *Show
Advanced Options* ausgewählt wurde.

-  Tags
-  `patches <../patches.html>`__

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

