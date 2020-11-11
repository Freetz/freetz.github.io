.. _NFS-UtilsNFS-Server:

NFS-Utils / NFS-Server
======================

Die NFS-Utils erweitern Freetz um einen NFS Server inklusive
Administrationswebinterface (siehe `nfsd-cgi <nfsd.html>`__) für die
Konfigdateien ``Exports``, ``allow_hosts`` und ``deny_hosts``.

.. _Hinweise:

Hinweise
--------

-  Exports funktionieren nur richtig mit ext2, ext3 oder ReiserFS
   Dateisystemen.
-  Squashfs und tmpfs/ramfs (/var) können nicht über NFS exportiert
   werden
-  Wenn keine Verbindung zustande kommt kann das an einer falschen NFS
   Version des Clients liegen. Beheben kann man das mit dem zusätzlichen
   mount Parameter ``-o nfsvers=3``.

.. _Referenzen:

Referenzen
----------

-  `​http://www.ip-phone-forum.de/showthread.php?p=1609992 <http://www.ip-phone-forum.de/showthread.php?p=1609992>`__
-  `​http://de.wikipedia.org/wiki/Network_File_System <http://de.wikipedia.org/wiki/Network_File_System>`__

-  Tags
-  `filesystem </tags/filesystem>`__
-  `packages <../packages.html>`__
