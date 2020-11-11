hd-idle
=======

`​hd-idle <http://hd-idle.sourceforge.net/>`__ ist ein Tool, um externe
Festplatten nach einer festgelegten "Idle-Zeit" (also "Nix-Tun")
herunterzufahren ("Spin-Down"). Da die meisten externen
IDE-Festplatten-Gehäuse das Setzen eines "Idle-Timers" nicht erlauben,
wird ein Utility wie *hd-idle* (oder das mit Freetz ebenfalls verfügbare
`spindown-CGI <spindown.html>`__) benötigt, um den Job zu erledigen.

Es gibt, herstellerabhängig 3 verschiedene Powermodes:

.. code:: bash

   active/idle (normal operation)
   standby (low power mode, drive has spun down)
   sleeping (lowest power mode, drive is completely shut down)

-  Tags
-  `filesystem </tags/filesystem>`__
-  `hardware </tags/hardware>`__
-  `packages <../packages.html>`__
