.. _NFS:

NFS
===

Um den doch etwas begrenzten Speicherplatz zu erweitern, kann man die
Fritzbox als NFS-Client benutzen. Da es kein Webinterface für diese
Funktion gibt muss das manuell erledigt werden. Zur Nutzung von
NFS-Shares muss das NFS-Kernel-Modul im menuconfig ausgewählt werden.
Abhängig von der verwendeten Konfiguration kann NFS auch fest im Kernel
sein. Dann kann man das modprobe weglassen und der mount-Befehl reicht
aus.

::

   modprobe nfs
   mount -t nfs -o soft server:/export/fritzbox mountpunkt

Damit das nach dem Hochfahren der Fritzbox automatisch passiert kann man
z.B. das hier in die debug.cfg einbauen:

::

   (
       nfssrv=mein.server.zu.hause

       while ! ping -c 1 $nfssrv ; do
           sleep 30
       done

       base=/var/mod/root
       mkdir $base/mnt
       modprobe nfs
       mount -t nfs -o soft $nfssrv:/export/fritzbox $base/mnt

       cd $base

       $base/mnt/startup.sh
   ) 2>&1 | logger &

Damit wird gewartet, bis der NFS-Server erreichbar ist, dann gemountet
und gleich ein dort liegendes ``startup.sh`` ausgeführt.

.. _Alternative:

Alternative
-----------

Komfortabler geht das ganze mit `autofs <autofs.html>`__, damit werden
die Verzeichnisse nur bei Bedarf gemountet.

-  Tags
-  `filesystem </tags/filesystem>`__
-  `packages <../packages.html>`__
