.. _FAQ:

FAQ
===

Während das FAQ zu Freetz spezifischen Fragen `hier <../FAQ.html>`__ zu
finden ist sollen hier allgemeine Fragen und Antworten zur FritzBox
gesammelt werden.

.. _WiekannicheineneigenenanderenDNS-ServerfüralleangeschlossenenPCsundFritzboxverwenden:

Wie kann ich einen eigenen/anderen DNS-Server für alle angeschlossenen PCs und Fritzbox verwenden ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AVM lässt die Änderung des default DNS-Servers, den die Box nutzt, im
Gegensatz zu anderen Routern über die Benutzeroberfläche derzeit(Ende
2009) nicht zu. Mögliche Lösungswege:

-  dnsmasq: Installation eines eigenen DNS-Servers auf der Fritzbox
   mittels dem Packet `dnsmasq <../packages/dnsmasq.html>`__. Dies ist
   ein allgemeiner Weg der auf jeder Box funktioniert, jedoch einen
   Neubau des Images (freetzen) erfordert. Zusammen mit einer geänderten
   Datei /etc/resolv.conf (im Trunk möglich über die GUI mit
   "Einstellungen"→"Freetz: resolv.conf") kann ein DNS-Server so
   eingetragen werden: "nameserver 208.67.220.220" (hier der von
   OpenDNS)
-  ohne dnsmasq: Bei einigen Boxen, z.B. 7170(Firmware 29.04.76) ist es
   möglich die zentrale Konfigurationsdatei von AVM zu bearbeiten. Mit
   "nvi /var/flash/ar7.cfg" müssen alle Vorkommen von "overwrite_dns1 =
   xxx.xxx.xxx.xxx" und "overwrite_dns2 = xxx.xxx.xxx.xxx" bearbeitet
   werden. Dieser Weg ist nur Personen empfohlen die Grundkenntnisse mit
   nvi und telnet bzw. ssh/telnet haben! Hier läuft der multid von AVM
   als DNS-Server. in der resolv.conf steht ein loopback "nameserver
   127.0.0.1". Dies ermöglicht auch Linux standard Anwendungen auf der
   fritzbox die Auflösung über den multid.
-  Ändern von /etc/resolv.conf: Wenn es nur darum geht, dass die Box
   selbst einen anderen DNS-Server benutzt, reicht eine Änderung in der
   Datei /etc/resolv.conf wie oben beim dnsmasq beschrieben. Dies ändert
   allein jedoch nur die Namensauflösung der Box, angeschlossene Clients
   nutzen dann weiter den Standard-DNS

.. _Wiekannmancharacterdeviceserstellen:

Wie kann man character devices erstellen?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Freetz benutzt auch ein solches `​character
device <http://en.wikipedia.org/wiki/Character_device#Character_devices>`__,
welches Dateien mit Hilfe eines Tiny Flash Filesystems (TFFS) dauerhaft
und veränderbar im Flash abspeichert, um die Konfiguration zu sichern.
Vorraussetzung ist eine Minor Nummer, die von keinem anderen character
device in ``/var/flash/`` verwendet wird (Freetz benutzt die Minor
0x3c), die Major Nummer kann aus ``/proc/devices`` ausgelesen werden:

.. code:: bash

   mknod /var/flash/<dateiname> c <major> <minor>

Da dieses character device in der
`​Ramdisk <http://de.wikipedia.org/wiki/RAM-Disk>`__ unter ``/var/``
erzeugt wurde, muss dieser Befehl jedesmal beim Neustart ausgeführt
werden. Der Inhalt bleibt aber erhalten. |Warning| Zum Bearbeiten solcher
character devices **niemals** vi verwenden! Dafür gibt es das
Wrapper-Skript nvi.

|Warning| **ACHTUNG:** Die Flash Partition des TFFS ist sehr klein und
nicht geeignet Dateien > 10-30 KB aufzunehmen (je nach Größe der anderen
Dateien).

Der aktuelle Füllstand kann wie folgt ausgelesen werden:

::

   echo 'cleanup' > /proc/tffs
   echo 'info' > /proc/tffs
   cat /proc/tffs | grep '^fill='

.. _WasfüreinNetzwerkkabelbenötigeichfürdasrecovern:

Was für ein Netzwerkkabel benötige ich für das recovern ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   RJ45 Standardnetzwerkkabel, kein Crossover

.. _WoranerkenneichdassicheineFB7270v3habe:

Woran erkenne ich, dass ich eine FB 7270v3 habe ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  An der Firmwareversion. Firmwares für 7270v3 beginnen mit 74.xx.xx
-  An der Anzeige im AVM-Web-Interface
   `​http://fritz.box <http://fritz.box>`__, z.B.
   **Produktinformationen**: FRITZBox Fon WLAN 7270 v3 (UI)
-  Anhand der Seriennummer (s.u.)

.. _WiealtistmeineFritzBox:

Wie alt ist meine FritzBox ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Benötig werden dazu die ersten vier Stellen der Seriennummer:
| Beispiel: **W484**-xxx-xx-xxx-xxx ⇒ **Donnerstag, den 27.11.2008**

| **W484 = Produktionswoche (Achtung: bitte nicht verwechseln mit der
  Kalenderwoche) 48 und 4. Tag = Donnerstag**

   +---------------+-------------+
   | **Buchstabe** | **Baujahr** |
   +---------------+-------------+
   | U             | 2006        |
   +---------------+-------------+
   | V             | 2007        |
   +---------------+-------------+
   | W             | 2008        |
   +---------------+-------------+
   | X             | 2009        |
   +---------------+-------------+
   | A             | 2010        |
   +---------------+-------------+
   | B             | 2011        |
   +---------------+-------------+
   | C             | 2012        |
   +---------------+-------------+

| **Info:** Wo liegt der Unterschied zwischen Produktionswoche und
  Kalenderwoche:
| In meinem Beispiel ist die Produktionswoche = der Kalenderwoche, aber
  z.B. im Jahr 2010 unterscheiden sich die Tage etwas:
| A101 = Kalenderwoch 10 = sollte einen Montag in der 10 KW, also
  08.03.2010 ergeben, das ist aber falsch,
| A101 = Produktionswoche 10 ergibt einen Montag in der 9 KW und zwar
  den 01.03.2010
| Quelle meiner Behauptung: - Wird nachgeliefert.

.. _WievielFlashhatmeineFritzBox7270:

Wie viel **Flash** hat meine FritzBox 7270 ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Für die zweite  Ziffern-Gruppe (xxxx-**XXX**-xxx-xxx) sind bislang
  folgende Nummern aufgetreten:

   +---------+---------+---------+---------+---------+---------+---------+
   | **Numme | **HWRev | **Brand | **Flash | **Farbe | **Versi | **Komme |
   | r**     | ision** | ing**   | größe   | **      | on**    | ntar**  |
   |         |         |         | (in     |         |         |         |
   |         |         |         | MB)**   |         |         |         |
   +---------+---------+---------+---------+---------+---------+---------+
   | 293     | 122     | AVM     | 8       | rot     | 7270 V1 |         |
   +---------+---------+---------+---------+---------+---------+---------+
   | 294     | 122     | 1und1   | 8       | schwarz | 7270 V1 |         |
   |         |         |         |         | /       |         |         |
   |         |         |         |         | silber  |         |         |
   +---------+---------+---------+---------+---------+---------+---------+
   | 304     | 139     | AVM     | 16      | rot     | 7270 V2 |         |
   +---------+---------+---------+---------+---------+---------+---------+
   | 305     | 139     | 1und1   | 16      | schwarz | 7270 V2 |         |
   |         |         |         |         | /       |         |         |
   |         |         |         |         | silber  |         |         |
   +---------+---------+---------+---------+---------+---------+---------+
   | 336     | 139     | AVM     | 16      | rot     | 7270 V2 | für     |
   |         |         |         |         |         |         | Kabel   |
   |         |         |         |         |         |         | Deutsch |
   |         |         |         |         |         |         | land-Ku |
   |         |         |         |         |         |         | nden    |
   +---------+---------+---------+---------+---------+---------+---------+
   | 334     | 145     | 1und1   | 16      | schwarz | 7270 V3 |         |
   +---------+---------+---------+---------+---------+---------+---------+
   | 351     | 145     | AVM     | 16      | rot     | 7270 V3 |         |
   +---------+---------+---------+---------+---------+---------+---------+
   | 352     | 145     | otwo    | 16      | rot     | 7270 V3 | für     |
   |         |         |         |         |         |         | o2-Kund |
   |         |         |         |         |         |         | en      |
   +---------+---------+---------+---------+---------+---------+---------+
   | 354     | 145     | AVM     | 16      | rot     | 7270 V3 | für     |
   |         |         |         |         |         |         | Netcolo |
   |         |         |         |         |         |         | gne-Kun |
   |         |         |         |         |         |         | den     |
   +---------+---------+---------+---------+---------+---------+---------+
   | 355     | 145     | EWE     | 16      | weiß /  | 7270 V3 | für     |
   |         |         |         |         | grau    |         | EWE-Kun |
   |         |         |         |         |         |         | den     |
   +---------+---------+---------+---------+---------+---------+---------+
   | 307     | 139     | AVME    | 16      | rot     | 7270 V2 | Interna |
   |         |         |         |         |         |         | tionale |
   |         |         |         |         |         |         | -Versio |
   |         |         |         |         |         |         | n       |
   +---------+---------+---------+---------+---------+---------+---------+
   | 310     | 139     | AVME    | 16      | rot     | 7270 V2 | A-/CH-V |
   |         |         |         |         |         |         | ersion  |
   +---------+---------+---------+---------+---------+---------+---------+

| Beispiel: W484-\ **305**-xx-xxx-xxx ⇒ Fritzbox mit 16MB und
  1und1-Branding

oder

| 1.) Support Datei auslesen über:
  `​http://fritz.box/html/support.html <http://fritz.box/html/support.html>`__
| 2.) In der Datei sollte folgender Eintrag zu finden sein:

-  8MB: **flashsize 0x00800000**
-  16MB: **flashsize 0x01000000**

| 00800000 Hex = 8.388.608 Dezimal = 8.192 KB = 8 MB
| 01000000 Hex = 16.777.216 Dezimal = 16.384 KB = 16 MB
| Weitere Details sind
  `​[hier] <http://www.ip-phone-forum.de/showpost.php?p=1124950&postcount=2>`__
  beschrieben.

.. _SteuercodesfürdieFritzbox:

Steuercodes für die Fritzbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hier findet Ihr eine (unvollständige) Liste der Steuercodes für Eure
Fritzbox:

   +--------------------+----------------------------------------------+
   | **Telefoncode**    | **Funktion**                                 |
   +--------------------+----------------------------------------------+
   | #96*0\*            | WLAN ausschalten                             |
   +--------------------+----------------------------------------------+
   | #96*1\*            | WLAN einschalten                             |
   +--------------------+----------------------------------------------+
   | #96*2\*            | CAPI over TCP (NetCAPI) ausschalten          |
   +--------------------+----------------------------------------------+
   | #96*3\*            | CAPI over TCP (NetCAPI) einschalten          |
   +--------------------+----------------------------------------------+
   | #96*4\*            | Anrufmonitor ausschalten                     |
   +--------------------+----------------------------------------------+
   | #96*5\*            | Anrufmonitor einschalten                     |
   +--------------------+----------------------------------------------+
   | #96*6\*            | Anzeige: "Kein Bier vor 4" oder "Bier holen" |
   +--------------------+----------------------------------------------+
   | #96*7\*            | telnetd einschalten                          |
   +--------------------+----------------------------------------------+
   | #96*8\*            | telnetd ausschalten                          |
   +--------------------+----------------------------------------------+
   | #96*9\*            | Anzeige: Uptime des Routers                  |
   +--------------------+----------------------------------------------+
   | #990*15901590\*    | Reboot der Fritzbox                          |
   +--------------------+----------------------------------------------+
   | #991*15901590\*    | Rücksetzen auf Werkseinstellungen            |
   +--------------------+----------------------------------------------+
   | #83*hhmmddmmyyyy\* | Uhr stellen                                  |
   +--------------------+----------------------------------------------+

.. _HilfedieBoxisttotalverkonfiguriertFreetzNot-AUS:

Hilfe, die Box ist total verkonfiguriert / Freetz "Not-AUS"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Jetzt ist es passiert: Paket konfiguriert und dabei irgendwas so
verstellt, dass die Box nicht mehr erreichbar ist. Auch in so einem Fall
gibt es noch eine Möglichkeit vor dem Recover:

`​Den Freetz "Not-Aus"
Schalter <http://www.voipfans.de/showthread.php?p=1001087>`__.

Wenn der Parameter *kernel_args* den Eintrag ``ds_off=y`` enthält, wird
der Haupteil von Freetz nicht mehr gestartet (genauer wird
/etc/init.d/rc.mod nicht aufgerufen). Um den Parameter zu setzen muss
man sich allerdings per FTP auf die Box verbinden, hat aber dann gute
Chancen, die Box ohne Recover erfolgreich zu neu wiederbeleben.

So geht es:

-  PC eine "feste" IP aus dem Netz 192.168.178.0 geben, z.B.
   192.168.178.12 255.255.255.0
-  Direkt nach dem Einschalten des Routers per FTP auf die 192.168.178.1
   (User/PW: adam2/adam2) verbinden (der FTP-Server steht nur wenige
   Sekunden nach dem Einstecken des Netzteils zur Verfügung, also
   eventuell ein paar mal versuchen (oder den Hinweis aus dem letzten
   Punkt ausprobieren)
-  Im FTP:

   .. code:: bash

      quote SETENV kernel_args ds_off=y
      quote REBOOT

   (bereits vorhandene Einträge in den kernel_args gehen dadurch
   natürlich verloren…)

-  Falls die Box auf die IP 192.168.178.1 nicht reagiert hilf in der
   Regel der Trick, ein unpassendes Recover einer anderen(!) Box zu
   starten, was zwar mit einer Fehlermeldung abbricht, aber zwei
   angenehme Nebeneffekte hat: Die Box wird (wenn der PC eine IP wie
   oben hat) im FTP-Modus auf die IP 192.168.178.1 gesetzt und bleibt im
   FTP-Modus, so dass das Abpassen des kurzen Momentes nach dem Starten
   entfällt.

Jetzt sollte zumindest die AVM-Oberfläche wieder wie gewohnt zu
erreichen sein. Man kann sich nun per Telnet auf die Box verbinden und
die "fehlerhafte" Konfiguration eines Paketes zurücksetzen, indem man
z.B. /var/tmp/flash/<paket>.diff löscht, von Hand "korrigiert" oder
umbenennt. Wenn dann der Aufruf von ``/etc/init.d/rc.mod`` wieder ein
"normal funktionierendes" Freetz startet, braucht man nur noch den
``ds_off=y`` Parameter zu entfernen, und alles sollte wieder gehen:

.. code:: bash

   . /usr/bin/kernel_args
   ka_removeVariable ds_off

Ergänzender Hinweis: Analog schaltet ``dbg_off=y`` das Abarbeiten der
debug.cfg beim Starten ab.

-  Tags
-  `faq </tags/faq>`__

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

