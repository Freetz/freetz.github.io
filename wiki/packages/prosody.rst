.. _ProsodyIM:

Prosody IM
==========

"*Prosody ist ein flexibler Jabber/XMPP-Server, geschrieben in der
Skriptsprache Lua. Die Ziele von Prosody sind einfache Bedienbarkeit und
geringe Systemauslastung.*"

**Dieses Paket ist in Arbeit!**

.. _Konfiguration:

Konfiguration
-------------

Zunächst kopieren wir uns die Beispielkonfiguration aus /var/mod/etc/:

.. code:: bash

   cp /var/mod/etc/prosody.cfg.lua /var/tmp/flash/mod/prosody.cfg.lua

Diese können wir dann mit vi bearbeiten:

.. code:: bash

   vi /var/tmp/flash/mod/prosody.cfg.lua

.. _VirtualHosthinzufügen:

VirtualHost hinzufügen
~~~~~~~~~~~~~~~~~~~~~~

Zunächst sollte man einen VirtualHost konfigurieren, dazu verändert man
man die "example.com" in die gewünschte Domain und entfernt das enabled
= false

.. code:: bash

   VirtualHost "example.com"
           enabled = false -- Remove this line to enable this host

.. _SSLverwenden:

SSL verwenden
~~~~~~~~~~~~~

Wenn man SSL verwenden möchte, benötigt man eine Zertifikat und einen
Schlüssel, diese kann man mit OpenSSL erstellen und auf ein externes
Speichermedium (z.B. USB-Stick) auf die FritzBox übertragen.

Die Pfade dazu müssen in der prosody.cfg.lua entsprechend verändert
werden:

.. code:: bash

   ssl = {
           key = "/var/media/ftp/uStor01/certs/localhost.key";
                   certificate = "/var/media/ftp/uStor01/certs/localhost.crt";
                   }

.. _InsInternetfreigeben:

Ins Internet freigeben
~~~~~~~~~~~~~~~~~~~~~~

Damit der Prosodyserver auch im Internet verfügbar ist, muss man nun
noch die entsprechenden Ports auf die FritzBox weiterleiten. Dazu fügt
man in der `AVM-Firewall <avm-firewall.html>`__ die Einträge für den
TCP-Port 5222 (für client-zu-server) und 5269 (server-zu-server) auf die
IP der entsprechenden FritzBox (meist 0.0.0.0) hinzu.

.. _Benutzerhinzufügen:

Benutzer hinzufügen
~~~~~~~~~~~~~~~~~~~

Das Hinzufügen von Benutzern ist standardmäßig aus Sicherheitsgründen
deaktiviert. Dies kann man in der prosody.lua.cfg temporär ändern, indem
man false bei Allow registration auf true setzt. Danach kann man sich
mit einem XMPP-Client registrieren.

Alternativ kann man mit der Shell Benutzer erstellen:

.. code:: bash

   prosodyctl adduser [Benutzer]@[Domain]

.. _POSIXaktivieren:

POSIX aktivieren
~~~~~~~~~~~~~~~~

Damit man prosody als Hintergrundprozess ausführen kann und damit man
logging aktivieren kann, muss POSIX aktiviert werden.

Zunächst aktiviert man das Modul in der prosody.cfg.lua:

.. code:: bash

      modules_enabled = {
           -- andere Module
           "posix"; -- mod_posix aktivieren
       }

Zusätzlich wird noch ein pid-File benötigt, dazu fügen wir in der
prosody.cfg.lua an:

.. code:: bash

   pidfile = "/var/tmp/flash/mod/prosody.pid"

.. _Datenexternspeichern:

Daten extern speichern
~~~~~~~~~~~~~~~~~~~~~~

Damit die Benutzerdateien nicht auf der FritzBox sondern auf einem
externen Medium gespeichert werden, erstellt man eine symbolische
Verlinkung:

.. code:: bash

   ln -s /var/media/ftp/uStor01/prosody/data /var/tmp/flash/mod/prosody/

.. _Benutzerhinzufügen1:

Benutzer hinzufügen
~~~~~~~~~~~~~~~~~~~

Damit prosody nicht mit root-Rechten geöffnet werden muss, wird ein
anderer Benutzer benötigt. Diesen kann man mithilfe der Shell erstellen:

.. code:: bash

   addgroup prosody
   adduser -G prosody prosody
   chown -R prosody:prosody /var/mod/home/prosody

.. _BeiSystemstartausführen:

Bei Systemstart ausführen
~~~~~~~~~~~~~~~~~~~~~~~~~

Wenn man die Daten nicht extern speichert, reicht es, wenn mit vi
/tmp/flash/mod/rc.custom folgendes hinzufügt:

.. code:: bash

   prosodyctl start

Wenn man die Daten extern speichert, sollte man in das Verzeichnis
/var/tmp/flash/mod wechseln und dort die folgenden Dateien anlegen:

.. code:: bash

   root@fritz:/var/tmp/flash/mod# vi rc.prosody
   #!/bin/sh

   start() {
           /usr/bin/prosodyctl start
   }

   stop() {
           /usr/bin/prosodyctl stop
   }

   case $1 in
           ""|start)
                   start
                   ;;
           stop)
                   stop
                   ;;
           *)
                   echo "Usage: $0 [start|stop]" 1>&2
                   exit 1
                   ;;
   esac

   exit 0

.. code:: bash

   root@fritz:/var/tmp/flash/mod# vi rc.external
   #!/bin/sh
   case $1 in
           load)
                   ;;
           unload)
                   sh /etc/init.d/rc.ngircd stop
                   sh /etc/init.d/rc.prosody stop
                   ;;
   esac

   eventadd 1 "Running custom rc.external done."

.. code:: bash

   root@fritz:/var/tmp/flash/mod# vi /var/tmp/flash/onlinechanged-cgi
   case "$1" in
    start)
      # Kommandos beim Start des Routers
      # ggf. sollten hier die Entraege von online) stehen
      ;;
    online)
      # Kommandos wenn der Router online geht (zB Zwangstrennung)
      #
         sleep 2;
         /var/tmp/flash/mod/rc.prosody start;
      ;;
    offline)
      # Kommandos wenn der Router offline geht (zB Zwangstrennung)
        /var/tmp/flash/mod/rc.prosody stop;
        sleep 2;
      ;;
   esac

.. _Änderungenspeichern:

Änderungen speichern
~~~~~~~~~~~~~~~~~~~~

|Warning| Damit diese Änderung beim Neustart erhalten bleibt müssen diese
gespeichert werden:

.. code:: bash

   modsave all

.. _Prosodyausführen:

Prosody ausführen
-----------------

Prosody kann auch manuell gestartet werden mit:

.. code:: bash

   prosodyctl start

.. _Links:

Links
-----

-  `​Prosody IM homepage <http://prosody.im/>`__
-  `​Ticket with patches <http://trac.freetz.org/ticket/858>`__
-  `​Lua homepage <http://www.lua.org/>`__
-  `Lua package <lua.html>`__
-  `​Wikipedia:
   XMPP <http://en.wikipedia.org/wiki/Extensible_Messaging_and_Presence_Protocol>`__
   (Jabber)
-  `​OpenWrt thread <http://open-wrt.ru/forum/viewtopic.php?id=21643>`__

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

