|<!>| **In Überarbeitung**

.. _WakeonLanWoLmitderFritzbox:

Wake on Lan (WoL) mit der Fritzbox
==================================

.. _MöglichkeitenderNutzungvonWoL:

Möglichkeiten der Nutzung von WoL
---------------------------------

Freetz bietet hier mehrere Möglichkeiten der Nutzung:

-  Weboberfläche (`wol-cgi <../../../packages/wol.html>`__)
-  Callmonitor
-  Shellscripte

Standardmäßig wird hierzu das ether-wake Applet der busybox verwendet.
Bei Problemen kann mit dem optional auswählbaren
`wol <../../../packages/wol.html>`__ Binary getestet werden.

.. _Callmonitor:

Callmonitor
-----------

TODO

.. _Shellscripte:

Shellscripte
------------

.. _WakeonLAN-Skript:

Wake on LAN-Skript
~~~~~~~~~~~~~~~~~~

Um nicht über die Fritzbox-Weboberfläche arbeiten zu müssen, sondern
schnell per Kommandozeile einen PC aufzuwecken, kann folgendes Skript
verwendet werden (einfach in die ``rc.custom`` eintragen):

.. code:: bash

   # Skript für 'wakeup HOSTNAME' erstellen
   # WAKEUPPATH should be root's homedirectory, if you want to login via
   # ssh root@fritz.box './wakeup HOSTNAME'
   WAKEUPPATH=~root
   WAKEUP=$WAKEUPPATH/wakeup
   echo 'PATH=$PATH:'$WAKEUPPATH >> ~root/.profile
   touch $WAKEUP
   chmod +x $WAKEUP
   echo '#!/bin/sh' >> $WAKEUP
   echo 'test -z "$1" && echo "Syntax: wakeup HOSTNAME" && return 1' >> $WAKEUP
   echo '# Hostname auf Macadresse mappen (steht in /var/tmp/ethers)' >> $WAKEUP
   echo 'macadresse=$(sed -ne "/[[:blank:]]$1$/{s/[[:blank:]].*$//p;q}" /var/tmp/ethers)' >> $WAKEUP
   echo 'test -z "$macadresse" && echo "Macadresse von $1 wurde nicht gefunden!" && return 1' >> $WAKEUP
   echo '# Etherwake ausführen' >> $WAKEUP
   echo 'ether-wake $macadresse 2> /dev/null' >> $WAKEUP

Ab sofort kann dann mit Hilfe von ``wakeup HOSTNAME`` ein PC aufgeweckt
werden.

.. _WakeonLANautomatisierenüberSSH:

Wake on LAN automatisieren (über SSH)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um per Doppelklick oder durch einfaches Ausführen eines Skriptes einen
PC aufzuwecken, kann das unter `Wake on
LAN-Skript <wol.html#WakeonLAN-Skript%7C>`__ erwähnte Skript über eine
`SSH <../../../packages/dropbear.html>`__-Verbindung ausgeführt werden.
Hier eine kurze Anleitung zur "vollständigen Automation" für
Wake-On-Lan:

-  `Wake on LAN-Skript einrichten <wol.html#WakeonLAN-Skript>`__
-  `SSH-Zugang ohne Passwort
   einrichten <../../../packages/dropbear.html#SSH-ZugangohnePasswortHost-basedAuthentication>`__
-  `Wake on LAN-Skript
   ausführen <../../../packages/dropbear.html#möglicheAnwendungvonssh>`__:
   ``ssh -i <identityfile> root@fritz.box './wakeup <hostname>'``

Kommentar: Sollte dieses Wake on LAN-Skript nicht in eines der Packages?
Oder gibt es das vielleicht schon?

-  Tags
-  `howto </tags/howto>`__
-  `wol </tags/wol>`__

.. |<!>| image:: ../../../../chrome/wikiextras-icons-16/exclamation-red.png

