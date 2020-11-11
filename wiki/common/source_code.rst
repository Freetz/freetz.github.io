.. _Quellcode:

Quellcode
=========

Der Freetz-Quellcode wird in einem
`​Subversion <http://subversion.apache.org>`__-Repository verwaltet.
Subversion wird allgemein abgekürzt mit SVN.

.. _EntwicklerversionTrunk:

Entwicklerversion (Trunk)
-------------------------

| |Warning| Diese Version ist ausschließlich für **erfahrene Benutzer und
  Entwickler** gedacht, die sich selbst zu helfen wissen!
| |Warning| Sie ist ständigen Änderungen unterworfen und funktioniert daher
  möglicherweise **nur eingeschränkt** oder **temporär nicht**!

Aktuelle Liste unterstützter Boxen mit
`Firmware-Version </browser/trunk/FIRMWARES#L3>`__\ `​ </export/HEAD/trunk/FIRMWARES#L3>`__.

Auschecken aus SVN (zuvor ggf ``umask 022`` nicht vergessen!):

.. code:: bash

   $ svn co http://svn.freetz.org/trunk freetz-devel                 <--- freetz-trunk: Lokale Kopie des SVN-Repositorys
   $ svn co http://svn.freetz.org/trunk freetz-devel_r7843 -r 7843   <--- Bestimmte Revision auschecken (hier: 7843)

Auschecken aus Git:

.. code:: bash

   $ git clone https://github.com/Freetz/freetz.git freetz-devel <--- freetz-git: Lokale Kopie des Git-Repositorys

|Warning| `​Git <http://git-scm.com/>`__ ist nicht das führende System und
wird derzeit nicht offiziell unterstützt, sondern nur zusätzlich zu
Testzwecken zur Verfügung gestellt.

| Hinweis-1: Ein entsprechendes Paket, welches das ``git`` Programm
  enhält, muss auf dem Build-Host installiert sein!
| Hinweis-2: Sollte der Projekt-Server oder das SVN-Repository nicht
  erreichbar sein, kann alternativ das Git-Repository genutzt werden.
| Hinweis-3: Das `​Freetz
  Git-Repository <https://github.com/Freetz/freetz>`__ auf GitHub
  bezieht seine Daten direkt vom Projekt-Server!
| Hinweis-4: Wer ``FREETZ_DEVELOPER_VERSION_STRING=y`` benutzt, sollte
  sich das Ticket `fwmod: Identify SVN_VERSION within Freetz Git
  repository </ticket/1754>`__ anschauen.

.. _Updates:

Updates
-------

Aktualisieren (Update) eines vorhandenen lokalen SVN-Repositorys (hier:
Entwicklerversion):

.. code:: bash

   $ cd freetz-devel
   $ svn up         <--- Update auf aktuelle Revision
   $ svn up -r 7843 <--- Update auf eine bestimmte Revision (hier: 7843)

Update eines lokalen Git-Repositorys (hier: Entwicklerversion):

.. code:: bash

   $ cd freetz-devel
   $ git pull

.. _StabileVersion:

Stabile Version
---------------

|Warning| **Die "stabile" Version wird nicht mehr gepflegt und neuere Boxen
wie auch aktuelle Firmwares (06.X) sind hier nicht verfügbar. Es
empfiehlt sich nur den trunk Zweig zu nutzen.** |Warning|

Für einige Box-Typen kann keine Firmware von den AVM-Servern geladen
werden: Abhilfe siehe
`hier <../FAQ.html#Couldnotdownloadfirmwareimage>`__.

Je nach Gerätetyp wird eine der nachstehenden Versionen benötigt:

**freetz-2.0**: aktuellste stabile Version (Liste unterstützter Boxen
mit
`Firmware-Version </browser/branches/freetz-stable-2.0/FIRMWARES#L3>`__\ `​ </export/HEAD/branches/freetz-stable-2.0/FIRMWARES#L3>`__)

.. code:: bash

   $ svn co http://svn.freetz.org/branches/freetz-stable-2.0

**ds-0.2.9-p8** (Kernel 2.4): für sehr alte Boxen, die kein
Firmware-Update mehr von AVM erhalten (mehr Infos
`​hier <http://www.ip-phone-forum.de/showthread.php?t=135253>`__)

.. code:: bash

   $ svn co http://svn.freetz.org/tags/ds-0.2.9-p8

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

