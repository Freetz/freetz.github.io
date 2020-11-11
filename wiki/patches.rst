.. _FreetzPatches:

Freetz Patches
==============

-  Die Größenabgaben (Platzeinsparung im komprimierten Dateisystem) sind
   nur ungefähre Richtwerte und können von Version zu Version variieren.
-  Es werden nur Patches angezeigt die für die ausgewählt FritzBox
   nutzbar sind
-  Die Auswirkungen eines Patches sind nicht unbedingt im
   AVM-Webinterface sichtbar

= Web menu patches =

Freetz **Funktionserweiterung-Patches** dienen dazu, das Verhalten der
FritzBox zu verbessern, indem einige Funktionen der Original-Firmware
verbessert oder erweitert werden. Neben diesem Überblick über die
**Patches** existiert noch `​ein Thread in
IPPF <http://www.ip-phone-forum.de/showthread.php?t=180289>`__, wo jeder
seine Lieblingskonfiguration posten kann. Diese
"Lieblingskonfigurationen" geben einen guten Richtwert dazu, welche
Patches in welcher Konfiguration sinnvoll und zu empfehlen sind. Denn
auch hier gilt auf keinen Fall die Regel "je mehr desto besser".

**Name**

**Beschreibung**

**Größe**

Patch VCC?

Es kann der 2. VCC bearbeitet werden

-

Patch ATA?

Es kann die ATA Konfiguration bearbeitet werden

-

`Patch enum <patches/enum.html>`__

Fügt dem WebIF Konfigurationsseiten für ENum hinzu

-

DSL settings?

Es können mehr DSL Optionen bearbeitet werden

-

external SIP?

Es können externe SIP verbindungen konfiguriert werden

-

`Patch 3rd alarm-clock <patches/alarmclock.html>`__

Fügt einen 3. Wecker zum AVM WebIF hinzu

-

`Patch webmenu signed message <patches/signed.html>`__

Entfernt den Hinweis auf "nicht unterstützte Modifikationen" aus dem AVM
WebIF

-

= USB patches =

Patches die die Funktionalität von USB Geräten beeinflussen

**Name**

**Beschreibung**

**Größe**

`Patch USB storage names <patches/usb_names.html>`__

Vergibt einheitliche Namen für USB-Speichermedien und verbessert
deutlich die Unterstützung der USB-Speichermedien

-

`Execute autorun <patches/exec_autorun.html>`__

Ermöglicht autorun.sh nach Mounten eines USB Speichermediums auszuführen

-

`FREETZMOUNT <patches/freetzmount.html>`__

Vergibt einheitliche Namen für USB-Speichermedien, verbessert deutlich
die Unterstützung der USB-Speichermedien, ermöglicht mounten nach LABEL.
FREETZMOUNT ist der Nachfolger vom USB-Storage-Patch und beinhaltet auch
autorun/autoend patch. Nach dem Umstieg zu FREETZMOUNT wird es empfohlen
das Paket fstyp manuell abzuwählen.

-

`Raise the count of connectable usb
devices <patches/maxdevcount.html>`__

Erhöht die Anzahl maximal anschließbarer USB-Devices auf 9

-

`Multiple Printers <patches/multpile_printers.html>`__

Ermöglicht die Nutzung mehrere Drucker an der FritzBox

-

Modify UMTSD?

Der umtsd wird nur für bekannte Modems gestartet und blockiert so
/dev/ttyUSB? nicht.

-

`Custom UDEV rules <patches/custom_udev_rules.html>`__

Es können eigene Regeln die UDEV auswertet hinterlegt werden.

-

= Removal patches =

Freetz **Remove-Patches** (auch Removes genannt) dienen dazu, Platz für
andere `Pakete <packages.html>`__ zu schaffen, indem nicht benötigte
Bestandteile der Original-Firmware entfernt werden. Neben diesem
Überblick über die **Remove-Patches** existiert noch `​ein Thread in
IPPF <http://www.ip-phone-forum.de/showthread.php?t=180289>`__, wo jeder
seine Lieblingskonfiguration posten kann. Diese
"Lieblingskonfigurationen" geben einen guten Richtwert dazu, welche
Removes in welcher Konfiguration sinnvoll und zu empfehlen sind. Denn
auch hier gilt auf keinen Fall die Regel "je mehr desto besser". Wenn
ein Freetz-Package eine Funktionalität ersetzt kann automatisch ein
Remove-Patch ausgewählt werden

**Name**

**Beschreibung**

**Größe**

Remove Annex X firmware file?

Die entsprechende Annex Firmware wird entfernt. Es wird immer nur eine
benötigt, im ATA-Modus (z.B. Kabelanschlus) keine.

je 335-745kB

Remove v1/v2 piglet file(s)?

Es wird nur eine Version abhängig von der Hardversion benötigt.

?

`Remove assistant <patches/remove_assistant.html>`__

Entfernt den Einrichtungs-Assistenten. Achtung! Dadurch ist die
automatische Einrichtung z.B. mit 1und1-Startcode nicht mehr möglich.

ca. 50kB

`Remove aura usb <patches/remove_aura_usb.html>`__

Entfernt die Unterstützung für den AVM-USB-Fernanschluss (hierfür hat
FREETZ das Paket `USB-IP <packages/usbip.html>`__ zu bieten)

ca. 16kB

Remove avalanche_usb.ko?

???

ca. 60kB

Remove AVM NAS Webinterface?

Das AVM-NAS Webinterface wird entfernt und kann nicht mehr genutzt
werden. Entfernt auch den AVM-Media-Server (s. u.)

ca. 390kB

`Remove AVM vpn <patches/remove_vpn.html>`__

Entfernt AVM-VPN-Server (FREETZ bietet OpenVPN als Alternative)

ca. 123kB

Remove AVM web server?

Der Webserver für das AVM-Webinterface wird entfernt und durch httpd
(immer in Freetz enthalten) ersetzt. (Zusammen mit UPnP kann auch die
libwebsrv.so library entfernt werden.)

5(+38)kB

Remove branding?

Es können verschieden Brandings entfernt werden. Das auf der Box aktive
Branding darf nicht entfernt werden||?

`Remove CapiOverTCP <patches/remove_capi.html>`__

Entfernt CapiOverTCP-Schnittstelle der FritzBox. Achtung! CapiOverTCP
wird von mehreren nützlichen PC-Programmen für den Zugriff auf die Box
benutzt! FritzFax nutzt z.B. diese Schnittstelle, um Faxe von PC aus
über die FritzBox zu verschicken

ca. 10kB

Remove chronyd?

Der chronyd zur Zeitsynchronisation wird entfernt. Dessen Aufgabe
übernimmt dann multid.

165-215kB

Remove cdrom.iso?

Die cdrom.iso wird entfernt.

130-265kB

Remove DECT files?

Es können keine DECT Geräte mehr verbunden werden.

20-360kB

`Remove dsld <patches/remove_dsld.html>`__

Entfernt den DSL-daemon - die Box kann dann nur noch als IP-Client
verwendet werden. Achtung! Ohne dsld kann die Box keine DSL-Verbindung
aufbauen und auch "Internet über LAN" geht nicht mehr, weil der dsld
auch Firewall und NAT übernimmt.

115-245kB

Remove showdsldstat?

Entfernt showdsldstat, ein Werkzeug mit dem der Status der
Internetverbindung (CPMAC-Modus, Verbindungszeit, DNS-Server und
Router), IPv6, VoIP und TR069 angezeigt werden kann.

10-30kB

Remove dtrace?

Entfernt trace Debugging-Utility für den D-Kanal von ISDN

85-225kB

`Remove ftpd <patches/remove_ftpd.html>`__

Entfernt den AVM-FTP-Server (kann durch die Freetz-Pakete vsftpd oder
bftpd ersetzt werden)

ca. 30kB

`Remove help <patches/remove_help.html>`__

Entfernt die Online-Hilfe zum AVM-WebIF

ca. 20kB

Remove jffs2.ko?

Entfernt das Kernelmodul für
`​JFFS2 <http://en.wikipedia.org/wiki/JFFS2>`__. Benötigt zur Nutzung
des optionalen, internen Speichers */data*, wo z.B.
Anrufbeantworterdaten und AVM-Plugins (7270_v1) gespeichert werden,
sofern die Firmware genügend Platz im Flash-Speicher frei gelassen hat
und kein USB-Speicher angeschlossen ist.

144-192kB

Remove lsof?

Entfernt lsof.

ca. 150kB

`Remove mediasrv <patches/remove_mediasrv.html>`__

Entfernt den AVM-Media-Server

ca. 40kB

`Remove minid <patches/remove_minid.html>`__

Entfernt die Unterstützung für FritzMini

ca. 215kB

`Remove MyFritz <patches/remove_myfritz.html>`__

Entfernt das MyFritz Web Interface (AVM's DynDNS)

ca. 1.1MB

Remove NTFS support?

AVM's NTFS Unterstützung wird entfernt.

118-180kB

Remove printserv?

Die Fritzbox kann kein Druckserver mehr sein.

15-20 kB

Remove run_clock?

Der Betriebsstundenzähler wird entfernt.

10-15kB

`Remove Samba <patches/remove_samba.html>`__

Entfernt den AVM-Samba-Server

300-600kB

Remove strace?

Entfernt strace.

ca. 440kB

`Remove the support-files <patches/remove_support.html>`__

Entfernt die support-files, welche man über die URL
`​http://fritz.box/html/support.html <http://fritz.box/html/support.html>`__
generieren und abspeichern kann.

ca. 8kB

`Remove tr069 stuff <patches/remove_tr069.html>`__

Entfernt tr069 (Remote-Konfiguration durch den Provider). Ohne tr069 ist
keine Einrichtung mit 1und1-Startcode möglich.

ca. 70kB

Remove UMTS support?

Danach kann die FritzBox keine UMTS Verbindung mehr aufbauen.

ca. 12kB

`Remove UPnP daemon <patches/remove_upnp.html>`__

Entfernt den UPnP-daemon. Achtung! Ohne UPnP-daemon ist keine
Einrichtung von FritzFax möglich.

ca. 10kB

`Remove usermand <patches/remove_usermand.html>`__

| Entfernt die ausschließlich für die Kindersicherung benötigten Dateien
  (usermand, userman.ko).
| Für die FBox **WLAN 3170** bitte diesen Patch nicht auswählen\ **,
  ansonsten gibt es Dauerreboot.**

ca. 40kB

Remove AVM e2fsprogs binaries?

Entfernt blkid, fsck, mkfs.

ca. 220kB

Remove VoIP files?

Entfernt Daten für VoIP-Betrieb.

ca. 250kB

Remove VoIP & ISDN files?

Entfernt vollständig neben dem VoIP-daemon noch die
Telefoniefunktionalität der Box. Achtung! Damit funktioniert die Box
dann **nicht** mehr als Telefonanlage.

?

Remove webdav?

Entfernt die Dateien die für Webdav benötigt werden.

10-510kB

Remove WLAN files?

Entfernt Daten für WLAN-Betrieb.

ca. 700kB

= Replacement patches =

**Name**

**Beschreibung**

**Größe**

Replace AVM SSL Libs?

Die SSL Libs von AVM werden ersetzt.

ca. 400kB

Replace dtrace?

Statt dtrace wird ein eigenes `Script <packages/mod.html#dtrace>`__ (per
Telefoncode) ausgeführt.

85-225kB

`Replace onlinechanged <patches/replace_onlinechanged.html>`__

Onlinechanged wird durch eigenen IP-Watchdog angestoßen (geht auch auf
IP-Clients).

-

= Additional patches =

**Name**

**Beschreibung**

**Größe**

Add Annex firmware file?

Fügt eine Annex firmware ins Image ein.

?

Enforce urloader settings?

Ändert das Environment des Urloaders.

-

= Misc patches =

**Name**

**Beschreibung**

**Größe**

Change LED semantics to W920V?

Passt die LEDs der Beschriftung vom Speedport an.

-

Disable serial console?

Deaktiviert die Konsole am internen seriellen Port.

-

= AVM daemons =

**Name**

**Beschreibung**

**Größe**

Disable igd/upnp?

Es werden immer die Parameter gesetzt um dsld's IGD & multid's
UPNP-device zu deaktivieren. `Remove UPnP
daemon <patches/remove_upnp.html>`__ nutzt diese Option.

-

Disable ntp client?

Die Sytemzeit wird nicht von multid gesetzt. Ausgewählt wenn chrony
vorhanden ist oder ein eigener Zeitserver wie zB OpenNTPd.

-

Disable IGMP?

Der IGMP-Proxy von multid wird deaktiviert.

-

Disable tr069?

Das tr069discover von multid wird abgeschaltet. Wird vom Patch `Remove
tr069 stuff <patches/remove_tr069.html>`__ automatisch ausgewählt.

-

Disable DNS?

Der DNS-Port wird (mit Hilfe von libmultid) nicht von multid belegt. So
kann ein anderer DNS-Server genutzt werden, das Dynamic-DNS Update sowie
die Zeitsysnchronisation funktionieren weiterhin.

-

= Invisible? patches =

**Name**

**Beschreibung**

**Größe**

`Onlinechanged <patches/onlinechanged.html>`__

Ermöglicht das Ausführen von Skripten bei einer Änderung des
Online-Statuses der Box

-

-  Tags
-  `patches <patches.html>`__
