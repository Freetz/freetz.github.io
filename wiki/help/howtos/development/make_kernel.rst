.. _Kernelkonfigurierenundkompilieren:

Kernel konfigurieren und kompilieren
====================================

Vorraussetzung ist eine Toolchain (siehe `Cross-Compiler / Toolchain
erstellen <create_cross-compiler_toolchain.html>`__). Sollten jemals
Probleme mit nicht vorhandenen Verzeichnissen auftauchen, so kann ein
``make world`` Abhilfe schaffen. In der Regel sollte das aber nicht
nötig sein.

#. Der Boxtyp (Type) sollte richtig gewählt sein, da nur der Kernel für
   die entsprechende Box kompiliert wird
#. ``make kernel-dirclean`` Löscht den aktuell entpackten Source Tree
   des Kernels (wir werden von komplett sauberen Kernel Sourcen
   kompilieren; wer das nicht will, kann es mit ``make kernel-clean``
   versuchen)
#. ``make kernel-menuconfig`` Die Konfiguration des Kernels wird danach
   wieder nach ``./make/linux/Config.<kernel-ref>`` zurückgespeichert
#. ``make kernel-precompiled`` Nun werden der Kernel und die Kernel
   Module kompiliert:

   -  ``./kernel/kernel-<kernel-ref>.bin``
   -  ``./kernel/modules-<kernel-ref>/``

-  Tags
-  `howtos </tags/howtos>`__
