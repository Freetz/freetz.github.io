.. _FREETZMOUNT:

FREETZMOUNT
===========

#. Replaces and deselects usb-storage patch. The names of USB storage
   directories can be defined by WebIF (default: uStorXY) or by volume
   LABEL.
#. Replaces and deselects autorun.sh/ autoend.sh patch.

   -  - autorun/ autoend behaviour can be activated/ deactivated via
      WebIF.
   -  - autorun/ autoend are useful to start/ terminate applications
      located on USB devices, e.g. apache, samba or even swapfiles,
      after connecting or before disconnecting of USB devices.

#. Auto-mounted USB storage devices will be fully accessible, e.g. it is
   now possible to put user home directories (e.g. for FTP) on a
   FAT32-formatted partition and permit shell and FTP users to actually
   write to their own home directories.
#. Avoid deleting whole filesystems on USB devices.
#. Enhanced behaviour during mounting and unmounting.

**Notes:**

#. fstyp is not needed and can be deselected in Package-Selection →
   Testing.
#. You should not externalize ef2progs or blkid onto the same USB
   device(s) which you later want to use freetzmount for.

Further information (in German) is available in the following threads of
the IP-Phone forum:

-  `​FREETZMOUNT: Mounten ohne 1000 und ein Mal zu
   patchen <http://www.ip-phone-forum.de/showthread.php?t=200293>`__
-  `​/etc/hotplug/run_mount
   modifizieren <http://www.ip-phone-forum.de/showthread.php?t=200293>`__
-  `​Skript für immer gleiche Mountpoints (auch nach Verlust des
   Mounts) <http://www.ip-phone-forum.de/showthread.php?t=181859>`__

-  Tags
-  `patches <../patches.html>`__
