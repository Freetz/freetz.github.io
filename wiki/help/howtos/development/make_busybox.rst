.. _Busyboxkonfigurierenundkompilieren:

Busybox konfigurieren und kompilieren
=====================================

Vorraussetzung ist eine Toolchain (siehe `Cross-Compiler / Toolchain
erstellen <create_cross-compiler_toolchain.html>`__). Sollten jemals
Probleme mit nicht vorhandenen Verzeichnissen auftauchen, so kann ein
``make world`` Abhilfe schaffen. In der Regel sollte das aber nicht
nötig sein.

#. Der Boxtyp (Type) sollte richtig in der Freetz Konfiguration (make
   menuconfig)gewählt sein, da nur die Busybox für die entsprechende Box
   kompiliert wird
#. ``make busybox-dirclean`` Löscht die aktuell entpackten Sourcen der
   Busybox (wir werden von komplett sauberen Busybox Sourcen
   kompilieren; wer das nicht will, kann es mit ``make busybox-clean``
   versuchen)
#. ``make busybox-menuconfig`` Die Konfiguration der Busybox wird danach
   wieder nach ``./make/busybox/Config.<target-ref>`` zurückgespeichert
#. ``make busybox-precompiled`` Dies kompiliert die Busybox und
   aktualisiert:

   -  ``./busybox/busybox-<target-ref>``
   -  ``./busybox/busybox-<target-ref>.links``

-  Tags
-  `howtos </tags/howtos>`__
