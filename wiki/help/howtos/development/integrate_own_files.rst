.. _EigeneDateienindieFirmwareintegrieren:

Eigene Dateien in die Firmware integrieren
==========================================

Die Fritzbox besitzt zwei Speicherbereiche:

#. den `Flash <flash.html>`__
#. den Arbeitsspeicher (RAM)

Um im laufenden Betrieb Dateien anzulegen und zu verändern, lässt sich
das Verzeichnis ``/tmp`` nutzen. Es liegt im Arbeitsspeicher in einer
RAM-Disk und arbeitet wie ein normales beschreibbares Dateisystem.
Folgende Dinge sind jedoch zu beachten:

-  Es nutzt den vorhandenen Arbeitsspeicher mit, der je nach Box bis zu
   64MB gross ist. Wird die Menge der Daten im Arbeitsspeicher zu groß,
   startet die Box ohne Vorwarnung neu.
-  Alles, was im Arbeitsspeicher liegt, ist nach einem Reboot oder
   Stromausfall verloren.

Für die "feste Integration" gibt es mehrere Möglichkeiten:

+-----------------------+-----------------------+-----------------------+
| Variante              | Pros                  | Contras               |
+=======================+=======================+=======================+
| via Freetz Image      | -  einfaches Handling | -  die modifizierte   |
|                       | -  keine bestehende   |    Firmware muss      |
|                       |    Internetverbindung |    geflasht werden    |
|                       |    erforderlich       | -  der Flash-Speicher |
|                       |                       |    ist kleiner als    |
|                       |                       |    das RAM und oft eh |
|                       |                       |    schon fast voll    |
+-----------------------+-----------------------+-----------------------+
| via ``debug.cfg``     | -  funktioniert auf   | -  funktioniert nur   |
|                       |    jeder Box          |    mit ASCII-Dateien, |
|                       | -  keine bestehende   |    wie z.B. mit       |
|                       |    Internetverbindung |    Skripten oder      |
|                       |    erforderlich       |    Konfigurationsdate |
|                       |                       | ien                   |
|                       |                       | -  werden Änderungen  |
|                       |                       |    an diesen Dateien  |
|                       |                       |    vorgenommen,       |
|                       |                       |    müssen diese auch  |
|                       |                       |    wieder in die      |
|                       |                       |    debug.cfg          |
|                       |                       |    übernommen werden  |
+-----------------------+-----------------------+-----------------------+
| Nachladen von         | -  funktioniert mit   | -  bestehende         |
| Webserver             |    allen Dateien,     |    Internetverbindung |
|                       |    auch mit binären.  |    oder laufender     |
|                       |    Notwendig z.B. für |    interner Webserver |
|                       |    nachgeladene       |    erforderlich       |
|                       |    Programme wie z.B. | -  private Dateien    |
|                       |    bFTP,              |    wie z.B. secret    |
|                       |    dropbear(SSH) oder |    keys für SSH oder  |
|                       |    OpenVPN,           |    VPN dürfen         |
|                       | -  funktioniert auf   |    keinesfalls im Web |
|                       |    jeder Box          |    abgelegt werden!   |
|                       | -  Umgeht die         |    Wer dies tut, kann |
|                       |    Probleme des       |    sich               |
|                       |    knappen            |    Verschlüsselung    |
|                       |    Flash-Speichers    |    gleich sparen.     |
|                       | -  Änderungen lassen  |                       |
|                       |    sich leicht am     |                       |
|                       |    Rechner mit dem    |                       |
|                       |    eigenen Editor     |                       |
|                       |    (z.B. TextPad)     |                       |
|                       |    vornehmen          |                       |
|                       |    (Achtung: Auf      |                       |
|                       |    UNIX-Formatierung  |                       |
|                       |    achten!) und dann  |                       |
|                       |    auf den Webspace   |                       |
|                       |    hochladen.         |                       |
|                       | -  wer mehrere        |                       |
|                       |    Fritz!Boxen oder   |                       |
|                       |    Router hat, kann   |                       |
|                       |    so auf einmal die  |                       |
|                       |    Konfiguration für  |                       |
|                       |    alle gleichzeitig  |                       |
|                       |    anpassen           |                       |
+-----------------------+-----------------------+-----------------------+
| Nachladen vom USB     | -  funktioniert mit   | -  funktioniert nur   |
| Stick                 |    allen Dateien,     |    bei vorhendenem    |
|                       |    auch mit binären.  |    USB Slot mit einem |
|                       |    Notwendig z.B. für |    USB Stick (bzw.    |
|                       |    nachgeladene       |    anderem USB        |
|                       |    Programme wie z.B. |    Speichermedium)    |
|                       |    bFTP,              | -  Die USB devices    |
|                       |    dropbear(SSH) oder |    werden, je nach    |
|                       |    OpenVPN,           |    Firmware, leider   |
|                       | -  Umgeht die         |    unter              |
|                       |    Probleme des       |    verschiedenen      |
|                       |    knappen            |    Namen eingebunden, |
|                       |    Flash-Speichers    |    sodaß in der       |
|                       | -  Änderungen lassen  |    debug.cfg darau    |
|                       |    sich leicht am     |    eingegangen werden |
|                       |    Rechner mit dem    |    muß.               |
|                       |    eigenen Editor     |                       |
|                       |    (z.B. Notepadplus) |                       |
|                       |    vornehmen          |                       |
+-----------------------+-----------------------+-----------------------+
| WebDAV- bzw. NFS-     | -  RAM wird nicht mit | -  bestehende         |
| Share mounten         |    lokalen Kopien von |    Internetverbindung |
|                       |    Dateien gefüllt    |    und WebDAV-Server  |
|                       |    (abgesehen von der |    (z.B. GMX/1&1      |
|                       |    Ausführung)        |    MediaCenter)       |
|                       | -  funktioniert mit   |    erforderlich       |
|                       |    allen Dateien,     | -  private Dateien    |
|                       |    auch mit binären   |    wie z.B. secret    |
|                       | -  funktioniert auf   |    keys für SSH oder  |
|                       |    jeder Box          |    VPN dürfen         |
|                       | -  umgeht die         |    keinesfalls im Web |
|                       |    Probleme des       |    abgelegt werden!   |
|                       |    knappen            |    Wer dies tut, kann |
|                       |    Flash-Speichers    |    sich               |
|                       | -  sehr komfortabel,  |    Verschlüsselung    |
|                       |    da kein Nachladen  |    gleich sparen.     |
|                       |    per debug.cfg      |                       |
|                       |    nötig ist          |                       |
|                       | -  Änderungen lassen  |                       |
|                       |    sich leicht am     |                       |
|                       |    Rechner mit dem    |                       |
|                       |    eigenen Editor     |                       |
|                       |    (z.B. TextPad)     |                       |
|                       |    vornehmen          |                       |
|                       |    (Achtung: Auf      |                       |
|                       |    UNIX-Formatierung  |                       |
|                       |    achten!) und dann  |                       |
|                       |    auf den            |                       |
|                       |    WebDAV-Share       |                       |
|                       |    hochladen.         |                       |
|                       | -  wer mehrere        |                       |
|                       |    Fritz!Boxen oder   |                       |
|                       |    Router hat, kann   |                       |
|                       |    so auf einmal die  |                       |
|                       |    Konfiguration für  |                       |
|                       |    alle gleichzeitig  |                       |
|                       |    anpassen           |                       |
+-----------------------+-----------------------+-----------------------+

Die "perfekte Lösung" gibt es natürlich nicht. Je nach Anwendungsfall
werden die Möglichkeiten kombiniert.

.. _FesteIntegrationüberdasFreetzImage:

Feste Integration über das Freetz Image
---------------------------------------

-  Freetz-1.1.x: Die Datei kann unter ``./root`` an die gewünschte
   Stelle kopiert werden.
-  Ab Freetz-1.2: Dies kann ohne großen Aufwand über das Beispiel Addon
   ``own-files-0.1`` realisiert werden. Einfach das Kommentarzeichen vor
   ``own-files-0.1`` in addon/static.pkg entfernen und die gewünschten
   Dateien in das Verzeichnis ``./addon/own-files-0.1/root/`` an die
   Stelle kopieren, an der sie im root Dateisystem der Box landen
   sollen.
   Beispiel: eine Datei ``./addon/own-files-0.1/root/usr/bin/foo`` wird
   auf der Box in ``/usr/bin/foo`` landen.

..

   Dateien und Verzeichnisse, die unterhalb von ``/var`` liegen sollen
   können nach ``./addon/own-files-0.1/var.tar`` kopiert werden.
   Änderungen an diesen Dateien gehen bei jedem Reboot verloren.

.. _ErzeugenderDateienausderdebug.cfg:

Erzeugen der Dateien aus der debug.cfg
--------------------------------------

Beim Booten werden die gewünschten Dateien im Verzeichnis ``/tmp`` neu
erstellt. Dazu wird das Script ``debug.cfg`` missbraucht, das beim
Starten der FritzBox automatisch ausgeführt wird. Da die ``debug.cfg``
selbst im beschreibbaren TFFS des Flash (mtd3/4) liegt, gehen ihre
Inhalte beim Reboot nicht verloren.

Beispiel:

Der Code wird einfach in die ``debug.cfg`` eingefügt. Am einfachsten
geht es mit Putty:

-  Code in Zwischenablage kopieren
-  mit der Box via telnet / SSH verbinden
-  nvi /var/flash/debug.cfg
-  mit *: set paste RETURN* in den Einfügen/Paste Modus wechseln
-  an der passenden stelle "i" für insert drücken
-  rechte Maustaste auf Putty fügt den Text ein
-  nacheinander *ESC ESC : w q RETURN* drücken (Abbrechen wäre: *ESC ESC
   : q ! RETURN*)
-  Neustarten

Hier wird ein Skript erzeugt, das sich mit ``/var/tmp/checkonline.sh``
aufrufen lässt. Es zeigt an, welcher der neun Rechner im FB-LAN online
ist. Wichtig ist, daß der "Endmarker" (hier 'ENDCHECK') **nicht
eingerückt** ist. Die letzte Zeile macht das Script ausführbar. Abbruch
mit STRG+C.

::

   cat > /var/tmp/checkonline.sh << 'ENDCHECK'
   #!/bin/sh

   while [ 1 = 1 ]
   do
        clear
        echo Online:
        date
        echo ------------------------------------------------
        for a in "2 Desktop1" "3 Michael" "20 Christina" "21 -" "22 -" "23 -" "24 -" "25 -" "26 -" "27 -" "28 -"  "29 -" "45 FB WLAN SL(WDS)"

        do
                 ping -c 1 192.168.178.$a |grep "bytes from ">/dev/null && echo 192.168.178.$a &
        done
        sleep 1
        echo ------------------------------------------------
        sleep 9
   done

   ENDCHECK
   chmod +x /var/tmp/checkonline.sh

.. _NachladenvomWebserver:

Nachladen vom Webserver
-----------------------

Beim Booten werden alle gewünschten Dateinen aus dem Internet oder von
einem Webserver im Intranet auf die Box geladen.

.. _NachladenvomUSB-Stick:

Nachladen vom USB-Stick
-----------------------

Beim Booten werden alle gewünschten Dateinen direkt vom USB Stick bzw.
via FTP vom internen FTP Server auf die Box geladen.

.. _WebDAVSharemounten:

WebDAV Share mounten
--------------------

Für `Freetz <../../../index.html>`__ gibt es das Paket
`WebDAV <../../../packages/davfs2.html>`__, über das man einen
WebDAV-Share direkt mounten kann. Als Konsequenz werden alle
Remote-Dateien so behandelt, als wären sie lokal vorhanden, und zwar
ohne gesondertes Nachladen.

.. _NFS-Sharemounten:

NFS-Share mounten
-----------------

Mit dem `NFS Paket <../../../packages/nfs.html>`__ lässt sich gleiches
erreichen wie mit WebDAV (s.o.), nur etwas stabiler |:)|

-  Tags
-  `howtos </tags/howtos>`__

.. |:)| image:: ../../../../chrome/wikiextras-icons-16/smiley.png

