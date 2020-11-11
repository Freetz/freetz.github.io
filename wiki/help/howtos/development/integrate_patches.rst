.. _PatchesinFreetzeinspielen:

Patches in Freetz einspielen
============================

|Warning| Hinweis: Wenn ihr Freetz aus dem svn (trunk oder stable branch)
ausgecheckt habt, dann erhaltet ihr die neuesten Patches durch
``svn up``.

Bei dringenden oder kleinen Änderungen / Neuerungen werden passend zum
letzten Release so genannte Patches angeboten. Diese Patches haben einen
Dateinamen ähnlich diesem: freetz\ *-version-patch-name*.patch.bz2. Der
Patch muss **nach** dem Entpacken des zugehörigen Freetz
freetz\ *version*.tar.bz2 und **vor** dem Erstellen des Image
eingespielt werden. Folgende Anleitung geht davon aus, dass beide
Dateien im aktuellen Verzeichnis liegen:

#. *Falls noch nicht geschehen*: Freetz entpacken
   ``tar -xvjf freetz-version.tar.bz2``
#. Patch entpacken ``bunzip2 freetz-version-patch-name.patch.bz2``
#. Patch anwenden ``patch -p0 < freetz-version-patch-name.patch``

Nun ist der Patch in den entpackten Freetz eingespielt und man kann mit
dem Erstellen des Image fortfahren.

-  Tags
-  `howtos </tags/howtos>`__

.. |Warning| image:: ../../../../chrome/wikiextras-icons-16/exclamation.png

