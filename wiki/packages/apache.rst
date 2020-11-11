.. _ApacheWebservermitPHPCGI:

Apache Webserver mit PHP CGI
============================

*Mit diesem Paket ist es möglich, den Apache Webserver entweder allein
oder mit zusätzlichem PHP CGI Binary zu erstellen.*

Apache ist unter Testing zu finden, PHP unter Standard packages.

Das Paket enthält die minimale Verzeichnisstruktur für Apache + PHP. Die
Konfigurationsdateien bedürfen wahrscheinlich noch einiger Anpassungen
an die jeweiligen Bedürfnisse, bevor das ganze dann entweder manuell auf
ein an die Box angeschlossenes USB-Gerät (USB-Stick, Festplatte) - oder
aber ins Verzeichnis ``root`` (zur Integration ins Firmware-Image)
kopiert werden kann.

Man kann PHP auch ohne den Apache erstellen; das CGI Binary
(``sapi/cgi/php``) ist anschließend unter packages/php-x.y.z zu finden
(php-cgi) Wer hingegen das CLI Binary (``sapi/cli/php``) benötigt, muss
es sich leider selbst besorgen.

Beide Pakete, Apache sowohl auch PHP werden standardmäßig dynamisch
gegen die benötigten Bibliotheken gelinkt. Wer statische Binaries
bevorzugt, kann dies jedoch mit entsprechenden Einstellungen anpassen.

Werden spezielle Features (etwa SSL für Apache, XML Handling in PHP,
etc.) benötigt, müssen die Makefiles entsprechend angepasst werden.
Entsprechende Tipps und Tricks finden sich im
`​Forum <http://www.ip-phone-forum.de/showthread.php?t=127089>`__.

Das Apache Paket befindet sich nach dem Build in
*packages/apache-x.y.z,* ebenso ist dort die Config für PHP zu finden.
Das PHP Binary wird automatisch in das Firmware Image gepackt, dies ist
auf Grund der Größe nicht zu empfehlen. Besser ist folgende
Vorgehensweise:

#. Freetz Image ohne Apache und Php erstellen und auf die Box spielen
#. Apache und ev. PHP als statisch gelinkte binaries auswählen und
   erneut make ausführen
#. Die Binaries aus *packages/apache-x.y.z* und *packages/php-x.y.z* auf
   einen externen Stick packen (das php-cgi sollte in den cgi-bin Ordner
   des apache gelegt werden
#. apache.conf bzw httpd.conf im apache binary anpassen, ev. ist es
   nötig, dass zwei symlinks erstellt werden dies kann z.B so gelöst
   werden

.. code:: bash

     ln -s /var/media/ftp/uStor01/apache/logs /var/logs

Danach kann man die Apache Befehle direkt verwenden (z.B. apachectl
start|stop|restart):

.. code:: bash

   /var/media/ftp/uStor01/apache/bin/apachectl start

**Verwendet man kein selbsterstelltes Binary, so sollte (muss) man
Apache mittels folgendem Befehl starten:**

.. code:: bash

   httpd-2.2.4/bin/apachectl -f /Pfad/zur/Apache/Config/httpd.conf -k start

-  Sollte die Website nicht direkt erreichbar sein, bitte unter
   apache/logs nachsehen, welche Fehlermeldungen dort ausgegeben werden
-  Lässt sich Apache gar nicht erst starten ein chmod -R 777
   /var/media/ftp/uStor01/apache durchführen (evtl. reicht auch nur
   chmod -R +x /var/media/ftp/uStor01/apache)
-  Wichtig: damit PHP funktioniert müssen folgende Zeilen in die
   Apache-Konfiguration eingefügt werden:

.. code:: bash

   Action       php-script /cgi-bin/php-cgi
   AddHandler      php-script .php

Für CGI's muss folgende Zeile hinzugefügt/auskommentiert werden:

.. code:: bash

   AddHandler    cgi-script .cgi

Es kann auch eine bereits fertiger Apache2 Binary mit dem oben
beschriebenem PHP Binary verwendet werden.

Wird z.B. mod_proxy bzw. sogar mod_proxy_html benötigt empfehle ich das
fertige Binary aus diesem
`​Thread <http://www.ip-phone-forum.de/showthread.php?t=103110&p=1730858&viewfull=1#post1730858>`__.

apache.conf
-----------

Der User muss auf einen vorhandenen User abgeändert werden (der User
root ist nur bei speziellen Binaries möglich).

Derzeit (Stand Juli 2011) kann folgendes verwendet werden:

.. code:: bash

   User boxusr80
   Group root

Sollen die .htaccess Dateien verwendet werden, so muss für das
entsprechende Verzeichnis AllowOverride entsprechend angepasst werden
(man kann auch einfach "AllowOverride All" verwenden)

Hier eine entsprechende Config für ein Verzeichnis (diese ermöglicht
jedem den Zugriff!):

.. code:: bash

   <Directory "/var/media/ftp/uStor01/apache/htdocs">
   Options All
   AllowOverride    All
   Order allow,deny
   Allowfrom all
   </Directory>

   <Directory "/var/media/ftp/uStor01/apache/cgi-bin">
   AllowOverride    None
   Options ExecCGI
   Order allow,deny
   Allow from all</Directory>

.. _Passwortschutzmit.htaccess:

Passwortschutz mit .htaccess
----------------------------

   Soll ein Verzeichnis mittels *.htaccess* vor autorisiertem Zugriff
   geschützt werden kann folgendes hinzugefügt werden:

.. code:: bash

   AuthType
   Basic AuthUserFile    /path/to/.ht.password !AuthName    "Die Website erfordert Zugangsdaten" require valid-user

..

   **Wichtig** : im apache Ordner befindet sich htpasswd, mit dem man
   die Passwortdatei erstellen kann.

.. code:: bash

   htpasswd -c/path/to/.ht.password username

(Dies erstellt eine neue oder überschreibt die vorhandene Passwortdatei
mit dem angegebenem Usernamen)

Um Benutzer zur Passwortdatei hinzuzufügen folgendes benutzen:

.. code:: bash

    htpasswd/path/to/.ht.password username

Es ist generell empfehlenswert vor zu schützenden Daten das Kürzel .ht
anzugeben, dadurch bekommt der Benutzer die Datei nicht zu sehen.

.. _ApachealsProxy:

Apache als Proxy
----------------

Ein guter Einsatzzweck des Apaches ist es, ihn als Proxy zu verwenden.

Dies kann wie folgt aussehen: Nach extern ist nur der Port 80
freigegeben. Gibt der user z.B. freetz.meinedomain.at ein, so kommt er
auf das Freetz-Interface bei fritzbox.meinedomain.at auf das
AVM-Interface usw.

Der Vorteil besteht dabei, dass man nur einen Port nach außen freigeben
muss, und zusätzlich kann man die einzelnen Seiten auch mit einem
Passwort sichern. (Die Fritzbox kann z.B. nicht mehr zurückgesetzt
werden, wenn vorher ein Passwort eingegeben werden muss.

**Umsetzung:** Nötig ist dafür ein Apache mit dem Modul Proxy. Ich
verwende hierfür das von MaxMuster erstellte
`​Binary <http://www.ip-phone-forum.de/showthread.php?t=103110&p=1737217&viewfull=1#post1737217>`__.

Die Einrichtung erfolgt wie weiter oben beschrieben. Für jede
zusätzliche Website, welche angezeigt werden soll, muss ein VirtualHost
erstellt werden. Hier eine Beispielkonfiguration um das Freetz-Interface
über freetz.meinedomain.at anzeigen zu lassen:

.. code:: bash

   <VirtualHost *:80>
   ProxyPreserveHost On
   ProxyPass / http://localhost:81/
   ProxyPassReverse / http://localhost:81/
   ServerName freetz.meinedomain.at
       <Proxy *>
           Order Deny,Allow
           Allow from all
       </Proxy>
       <Location />
           Require valid-user
           AuthType basic
           AuthName "Passwortgeschuetzt - Login"
           AuthUserFile /Pfad/zur/Datei/.htpasswd
       </Location>
   </VirtualHost>

Das Location Element bewirkt, dass der Benutzer sich vor dem
Seitenaufbau anmelden muss.

.. _Sonstiges:

Sonstiges
---------

Sollte jemand auf die Idee kommen, ein CMS auf der Fritzbox laufen zu
lassen, so empfehle ich `​phpSqliteCms <http://phpsqlitecms.net/>`__
dies ist ein sehr smartes und schnelles CMS welches problemlos auf der
Box läuft (nur die Bildkomprimierung sollte man nicht nutzen).Andere CMS
wie Joomla!, Kajona, oder gar Drupal sollte man aufgrund der geringen
Systemleistung der `FritzBox </search/opensearch?q=wiki%3AFritzBox>`__
vergessen. Außer man kann mit Seitenaufbauzeiten von 1-3 Minuten leben
(dafür muss die php.ini angepasst werden).

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

-  `​Forumsdiskussion <http://www.ip-phone-forum.de/showthread.php?t=127089>`__
   mit Tipps und Tricks zu diesem Paket
-  `​Homepage <http://httpd.apache.org/>`__ des Apache Webservers
-  `​Wikipedia
   Artikel <http://de.wikipedia.org/wiki/Apache_HTTP_Server>`__ zum
   Apache Webserver
-  `​Homepage <http://www.apache.org/>`__ der Apache Software Foundation
-  `​Wikipedia
   Artikel <http://de.wikipedia.org/wiki/Apache_Software_Foundation>`__
   zur Apache Software Foundation
-  `​Apache Wiki <http://wiki.apache.org/general/>`__
-  `​PHP Homepage <http://de.php.net>`__
-  `​Wikipedia Artikel <http://de.wikipedia.org/wiki/Php>`__ zu PHP
-  `​Apache 1.3.37 und PHP 5.2.0 CGI auf der
   FritzBox <http://www.xobztirf.de/selfsite.php?aktion=Apache%20und%20PHP>`__

-  Tags
-  `daemons </tags/daemons>`__
-  `packages <../packages.html>`__
-  `server </tags/server>`__
-  `web </tags/web>`__
