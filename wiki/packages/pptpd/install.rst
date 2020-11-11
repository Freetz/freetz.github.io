.. _Installation:

Installation
============

.. _Kernel2.6Freetz:

Kernel 2.6 (Freetz)
-------------------

pptpd ist mittlerweile als Paket in `Freetz <../../index.html>`__
integriert, sodass es hier nur noch bei ``make menuconfig`` entsprechend
ausgewählt werden muss. Nach speichern der Konfiguration sowie
erfolgreichem ``make`` ist pptp dann im erstellten Image enthalten.

|Warning| Wichtig ist hier: Aufgrund der Crypt-Module wird ein "replaced
kernel" benötigt (kann entsprechend in ``make menuconfig`` ausgewählt
werden). Nur dann ist pptpd sichtbar und selektierbar!

.. _Kernel2.4ds-mod:

Kernel 2.4 (ds-mod)
-------------------

Wer pptpd in einem Image mit Kernel 2.4 (also mit dem "alten" DS-Mod)
verbauen will, hat ein wenig mehr Hand anzulegen:

.. _Vorbereitungen:

Vorbereitungen
^^^^^^^^^^^^^^

Man braucht einen Crosscompiler? um den Kernel kompilieren zu können.
Falls noch nicht vorhanden:

.. code:: bash

   make toolchain

Anschließend:

.. code:: bash

   make menuconfig

Die entsprechende Box auswählen, für die nachfolgend der PPTP-Server
kompiliert werden soll. (Es wird nach der entsprechenden Kernel-Größe
4MB oder 8MB unterschieden.)

*menuconfig* beenden und die Einstellungen abspeichern.

Folgende Dateien herunterladen:

-  `​pptp-patch.zip <http://www.ip-phone-forum.de/attachment.php?attachmentid=9892&d=1157118571>`__
-  `​pptpd-1.3.0_fixed.tar.gz <http://www.ip-phone-forum.de/attachment.php?attachmentid=10966&d=1161809653>`__

Die Verzeichnisse für spätere Anpassungen vorbereiten:

.. code:: bash

   make kernel-dirclean
   make kernel-menuconfig

Hier noch keine Einstellungen vornehmen, einfach Beenden und
Abspeichern.

.. _Patcheinspielen:

Patch einspielen
~~~~~~~~~~~~~~~~

``pptp-patch.zip`` entpacken und Patch einspielen

-  für 8MB-Kernel

   ::

      unzip pptp-patch.zip -d DS-MOD-VERZEICHNIS/source/ref-ohio-8mb-04.06/kernel/kernel_ohio-8mb_build/kernel
      cd DS-MOD-VERZEICHNIS/source/ref-ohio-8mb-04.06/kernel/kernel_ohio-8mb_build/kernel
      patch -p0 < pptp-patch.patch

-  für 4MB-Kernel

   ::

      unzip pptp-patch.zip -d DS-MOD-VERZEICHNIS/source/ref-4mb-04.06/kernel/kernel_ohio-8mb_build/kernel
      cd DS-MOD-VERZEICHNIS/source/ref-4mb-04.06/kernel/kernel_ohio-8mb_build/kernel
      patch -p0 < pptp-patch.patch

Beim Patchen werden euch noch ein paar Hinweise erwarten:

.. code:: bash

   The next patch would create the file linux-2.4.17_mvl21/include/asm-mips/kmap_types.h,
   which already exists!  Assume -R? [n]
   Apply anyway? [n]

Dort einfach alles mit *ENTER* betätigen.

.. _Kernelkonfigurierenundkompilieren:

Kernel konfigurieren und kompilieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   make kernel-menuconfig

Folgende Pakete zusätzlich auswählen:

.. code:: bash

   Network device support --->
     <*> PPP (point-to-point protocol) support
     [*] PPP multilink support
     [*] PPP support for async serial ports
     <*> PPP Deflate compression
     <*> Microsoft PPP compression/encyptions

   Cryptographic options --->
     [*] Cryptographic API
     <*> SHA1 digest algorithms
     <*> ARC4 cipher algorithms

Beenden und Abspeichern

.. code:: bash

   make kernel-precompiled

Sollte der Kompiliervorgang mit einem Segmentation-Fault abbrechen, den
Vorgang mit ``make kernel-precompiled`` noch einmal starten. Weshalb der
Fehler auftritt ist mir noch nicht klar, aber es entsteht schließlich
ein lauffähiges Kernel-Image.

.. _KompilierendesImagesvorbereitenunddurchführen:

Kompilieren des Images vorbereiten und durchführen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Das Addon-Paket? ``pptpd-1.3.0_fixed.tar.gz`` nach
``DS-MOD-VERZEICHNIS/addon`` entpacken und anschließen in die Datei
``static.pkg`` eintragen.

.. code:: bash

   tar -C DS-MOD-VERZEICHNIS/addon -xvzf pptpd-1.3.0_fixed.tar.gz
   echo pptpd-1.3.0 >> DS-MOD-VERZEICHINS/addon/static.pkg

Um die Erstellung des fertigen Firmware-Images vorzubereiten:

.. code:: bash

   make menuconfig

Dort die gewünschten Einstellungen vornehmen sowie sonstige Paktete
auswählen.

Für das PPTP-Server-Image ist zusätzlich die Einbindung folgender
Libraries nötig:

.. code:: bash

   Advanced options -->
       Shared libraries-->
           [*] libcc_s.so.1
           uClibc --->
               [*] libutil-0.9.28.so
   </code>

Zuguterletzt erstellen wird das endgültige Image mit:

.. code:: bash

   make

.. |Warning| image:: ../../../chrome/wikiextras-icons-16/exclamation.png

