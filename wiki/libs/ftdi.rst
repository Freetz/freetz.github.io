ftdi
====

Das Paket
`​ftdi <http://www.ip-phone-forum.de/showthread.php?p=1193103#post1193103>`__
stellt entsprechende Treiber für
`​RS-232 <http://de.wikipedia.org/wiki/Rs232>`__-`​USB <http://de.wikipedia.org/wiki/USB>`__-Adapter
auf der Box zur Verfügung, so dass man mit einem solchen Adapter mit
`​FTDI <http://www.ftdichip.com>`__-Chipsatz ein serielles Gerät
(Relais-Karten, Temperaturfühler, Wetterstationen, ggf. ganze
Heizanlagen uvm.) an die Box anschließen und darüber mit diesen Geräten
kommunizieren kann.

.. _Benutzung:

Benutzung
---------

.. _Beispiel-Parameter:

Beispiel-Parameter
~~~~~~~~~~~~~~~~~~

.. code:: bash

   T: Bus=01 Lev=01 Prnt=01 Port=00 Cnt=01 Dev#= 3 Spd=12 MxCh= 0
   D: Ver= 1.10 Cls=00(>ifc ) Sub=00 Prot=00 MxPS= 8 #Cfgs= 1
   P: Vendor=0403 ProdID=6001 Rev= 4.00
   S: Manufacturer=ftdi
   S: Product=usb serial converter
   S: SerialNumber=ftBNKG1I
   C:* #Ifs= 1 Cfg#= 1 Atr=a0 MxPwr= 44mA
   I: If#= 0 Alt= 0 #EPs= 2 Cls=ff(vend.) Sub=ff Prot=ff Driver=ftdi_sio
   E: Ad=81(I) Atr=02(Bulk) MxPS= 64 Ivl=0ms
   E: Ad=02(O) Atr=02(Bulk) MxPS= 64 Ivl=0ms

.. _AnpassenderBaudrate:

Anpassen der Baudrate
~~~~~~~~~~~~~~~~~~~~~

Eine ggf. erforderliche Anpassung der Baudrate wird in `​diesem
Forum <http://www.mikrocontroller.net/topic/92022>`__ diskutiert.

.. _VerbindungzumTesten:

Verbindung zum Testen
~~~~~~~~~~~~~~~~~~~~~

-  Verkabelung herstellen:
   Fritzbox ⇔ USB-RS-232-Adapter ⇔
   `​Null-Modem <http://de.wikipedia.org/wiki/Nullmodem>`__-Kabel ⇔
   Kontrollgerät (PC/Laptop/Macbook o.ä.)

-  Auf dem Kontrollgerät ein
   `​Hyperterminal <http://de.wikipedia.org/wiki/HyperTerminal>`__
   öffnen
-  Auf der Fritzbox:

   .. code:: bash

      echo "Hallo" > /var/ttyUSB0

..

      Statt *ttyUSB0* ist ggf. etwas anderes zu wählen, je nach dem, ob
      man den Adapter direkt an der Fritzbox angeschlossen hat, oder
      über einen USB-Hub mit mehreren USB-Ports.

-  Ergebnis im Hyperterminal auf dem Kontrollgerät:

   .. code:: bash

      Hallo

Und das sollte auch anders herum funktionieren, also von der Fritzbox
aus.

.. _USB-Fernanschluss:

USB-Fernanschluss
-----------------

| Da es von AVM (leider nur für Windows) den sog.
  `​USB-Fernanschluss <http://www.avm.de/de/Service/FAQs/FAQ_Sammlung/14300.php3?portal=FRITZ!Box_Fon_WLAN_7170&weitere=weitere>`__
  gibt, lässt sich das Ganze auch bequem vom Wohnzimmer aus steuern,
  auch wenn die Fritzbox woanders steht (LAN/WLAN-Anschluss reicht aus).
| Voraussetzung ist, dass das Tool USB-Fernanschluss den Chipsatz
  unterstützt, wie es z.B. für den
  `​PL2303 <http://www.ip-phone-forum.de/showthread.php?p=1021916#post1021916>`__
  der Fall ist.
| Sollte das Tool "Keine FRITZBox gefunden!" melden, wird von AVM
  `​hier <http://www.avm.de/de/Service/FAQs/FAQ_Sammlung/14564.php3?sessionid=g0q1vnu8m6d0rsjbped1svk8e7&kodo_KostenstellenProdukt=FRITZ!Box_Fon_WLAN_7170&kodo_OS=Windows%20XP&kodo_Anwendungsbereich=USB-Host&entryPoint=FAQs&URL=FAQs/FAQ_Sammlung/14564.php3>`__
  eine mögliche Lösung beschrieben.

.. _ListemitunterstützenAdaptern:

Liste mit unterstützen Adaptern
-------------------------------

Hier folgt eine Liste mit unterstützen Adaptern. Auch dazu gibt es einen
`​Diskussions-Thread im
IP-Phone-Forum <http://www.ip-phone-forum.de/showthread.php?t=165042>`__.

-  …
-  …
-  …

.. _Anregungen:

Anregungen
----------

Hier folgt eine Liste mit Anregungen und Links zu Projekten, welche
Geräte man ggf. an eine Fritzbox anschließen und darüber steuern kann:

-  `​Tecalor THZ 303
   SOL <http://www.tecalor.de/Kunden-Portal/THZ-403303-SOL.html>`__
   (Luftwärmepumpe/Heizung mit integrierter Wärmerückgewinnung) - siehe
   auch in
   `​diesem <http://www.haustechnikdialog.de/Forum/Default.aspx?t=85548&headline=Software+zum+Auslesen+der+Tecalor+THZ+303+SOL+%c3%bcber+RS232+o.a.+Schnittstelle>`__
   Forum
   (Falls Links zu kommerziellen Seiten hier unerwünscht sind, kann man
   den Link gerne wieder rausnehmen.)
-  `​Powerswitch <http://www.obdev.at/products/avrusb/powerswitch.html>`__
   von Objective Development mit Atmel AVR Microcontroller (AVR-USB)
-  `​USB-Relaisschalter <http://www.ip-phone-forum.de/showthread.php?t=175015>`__
-  …

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

-  `​FTDI Treiber im
   Freetz-Mod? <http://www.ip-phone-forum.de/showthread.php?t=159126>`__
   (Haupt-Diskussionsthread)
-  `​RS232-USB-Adapter an
   Fritzbox <http://www.ip-phone-forum.de/showthread.php?t=165042>`__
-  `​Hilfe!! PL2303
   Adapter <http://www.ip-phone-forum.de/showthread.php?t=137606>`__
-  `​USB-Seriell-Adapter an
   7170? <http://www.ip-phone-forum.de/showthread.php?t=164738>`__
-  `​USB - Seriell Treiber in
   DS-Mod <http://www.ip-phone-forum.de/showthread.php?t=101712>`__
-  `​Frage Steckdosenleiste mit FB
   steuern? <http://www.ip-phone-forum.de/showthread.php?t=105490>`__
-  `​ARK3116 USB zu Seriell Adapter an
   FB7150 <http://www.ip-phone-forum.de/showthread.php?t=151020>`__
-  `​Wie Konsole an serieller Schnittstelle? FB
   3170 <http://www.ip-phone-forum.de/showthread.php?t=146800>`__
-  `​ftdi_sio crasht unter Last (bug:
   CVE-2006-2936) <http://www.ip-phone-forum.de/showthread.php?t=164738>`__
-  `​Montageanweisung Tecalor THZ 303 SOL
   Luftwärmepumpe <http://energie-effizientes-haus.de/Daten/Niedrigstenergietechnik/THZ%20303%20SOL%20-%20Gebrauchs-%20und%20Montageanweisung.pdf>`__
   (Schaltbilder mit RS232-Schnittstelle auf Seiten 17+18)
-  `​Seriellen / V24 Port der FB als virtuellen Port auf Windows PC
   nutzen <http://www.ip-phone-forum.de/showthread.php?t=143186>`__
-  `​Mikrocontroller an AVM. Frage zu: Mögliche fritzboxinterne
   Kommunikation <http://www.ip-phone-forum.de/showthread.php?p=1137643#post1137643>`__
