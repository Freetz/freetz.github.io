.. _Aktionen:

Aktionen
========

Aktionen werden anhand von Regeln ausgeführt, die in den sogenannten
`Listeners <listeners.html>`__ definiert sind. Dabei kann beliebiger der
FritzBox bekannter Shell-Code (Programme/Befehle) ausgeführt werden. Die
Aktionen müssen im Listener als Parameter <action> übergeben werden
(siehe Beispielbild unten für die Aktion *dboxpopup*), wobei
`Umgebungsvariablen <listeners.html#ereignis-informationen_fuer_aktionen>`__
mit Informationen über den auslösenden Anruf verwendet werden können.

Einige Standardfunktionen werden direkt vom callmonitor bereitgestellt
und sind im Folgenden beschrieben. Mit dem Script *callaction* lassen
sich alle Callmonitor-Aktionen von außerhalb (z.B. von der Kommandozeile
zum Testen) aus aufrufen.

Wenn man in Verbindung mit *checkmaild* neu eingetroffene Emails auf
einem VDR ausgeben will, kann man das machen, indem man die Datei
``/var/mod/etc/maillog.cfg`` z.B. wie folgt anlegt:

::

   #!/bin/sh
   # neue Email empfangen
   if [ "$1" = "0" ];
   then
      callaction vdr m741 "Am $6 um $7 Uhr schrieb $8: $9"
   fi

Hintergrundinfos zur Datei ``maillog.cfg`` und dem checkmaild Paket kann
man auch hier im Wiki unter `checkmaild <../checkmaild.html>`__
nachlesen.

.. _Benachrichtigen:

Benachrichtigen
---------------

Benachrichtigungen sind dafür da, eingehende und/oder verpasste Anrufe
über verschiedene Kommunikationswege und auf verschiedenen Geräten zu
signalisieren.

Die vorgegebenen Standardtexte der Funktionen können an die `eigenen
Bedürfnisse angepasst <adapt_messages.html>`__ werden.

Funktionen, die auf `getmsg <actions/getmsg.html>`__ basieren:

-  `DGStation Relook 400S <actions/relook.html>`__
-  `DBox <actions/dbox.html>`__
-  `DreamBox <actions/dreambox.html>`__
-  `XBox <actions/xbox.html>`__
-  `Freecom MusicPal <actions/musicpal.html>`__

Falls nötig, können beim Aufruf auch `Passwörter und
Benutzernamen <actions/password.html>`__ angegeben werden.

Funktionen, die auf `rawmsg <actions/rawmsg.html>`__ basieren:

-  `SoundBridge <actions/soundbridge.html>`__ von Roku
-  `VDR <actions/vdr.html>`__
-  `YAC <actions/yac.html>`__: Yet Another Caller ID Program

Benachrichtung auf ganz anderem Wege:

-  `mailmessage <actions/mail.html>`__: Benachrichtigung per Mail
-  `Samsung TV <actions/samsung.html>`__: Benachrichtigung
   SOAP-Nachricht
-  `Snarl <actions/snarl.html>`__: Benachrichtigung für Snarl

.. _WählenWeckenKonfigurieren:

Wählen, Wecken, Konfigurieren
-----------------------------

-  `Wählhilfe <actions/dial.html>`__: Ansprechen der Wählhilfe der
   FritzBox
-  `WOL <actions/wol.html>`__: Wake on LAN
-  `Fritz!Box-Konfiguration <actions/config.html>`__: WLAN, SIP,
   Portforwarding ein- und ausschalten

.. _EigeneAktionen:

Eigene Aktionen
---------------

Mit den beiden Basisfunktionen *getmsg* und *rawmsg* können auf den
Zielmaschinen nahezu beliebige Funktionen ausgeführt werden — sofern sie
dort entsprechend realisiert sind (Start über den Webserver oder
Lauschen an einem TCP-Port).

-  `getmsg <actions/getmsg.html>`__: HTTP-GET-Requests
-  `rawmsg <actions/rawmsg.html>`__: Nachrichten über "rohe"
   TCP-Verbindungen
-  `Aufruf <actions/call.html>`__: Hinweise zu Funktionsaufrufen

Auch andere, selbst-definierte Aktionen sind möglich:

-  `Selbst-definierte Aktionen <actions/self-defined.html>`__

.. _ListeverfügbarerAktionen:

Liste verfügbarer Aktionen
--------------------------

(generiert)

#. `HTTP-Requests (getmsg) <actions/getmsg.html#HTTP-Requestsgetmsg>`__

   #. `Syntax: <actions/getmsg.html#Syntax:>`__
   #. `Beispiel: <actions/getmsg.html#Beispiel:>`__

#. `DBox2 <actions/dbox.html#DBox2>`__

   #. `DBox2 mit Neutrino
      Image <actions/dbox.html#DBox2mitNeutrinoImage>`__
   #. `DBox2 mit Enigma Image <actions/dbox.html#DBox2mitEnigmaImage>`__

#. `Wählhilfe <actions/dial.html#Wählhilfe>`__
#. 

   #. `Listener-Eintrag: <actions/snarl.html#Listener-Eintrag:>`__
   #. `Screenshots: <actions/snarl.html#Screenshots:>`__

#. `Selbstdefinierte
   Aktionen <actions/self-defined.html#SelbstdefinierteAktionen>`__
#. `Benutzernamen und
   Passwörter <actions/password.html#BenutzernamenundPasswörter>`__

   #. `Beispiel <actions/password.html#Beispiel>`__

#. `Freecom MusicPal <actions/musicpal.html#FreecomMusicPal>`__
#. `Roku SoundBridge <actions/soundbridge.html#RokuSoundBridge>`__
#. `VDR <actions/vdr.html#VDR>`__
#. `Benachrichtigung auf einem Samsung
   TV <actions/samsung.html#BenachrichtigungaufeinemSamsungTV>`__
#. `XBox <actions/xbox.html#XBox>`__

   #. `Anpassungen auf der
      XBox <actions/xbox.html#AnpassungenaufderXBox>`__
   #. `Weitere Möglichkeiten <actions/xbox.html#WeitereMöglichkeiten>`__

#. `YAC <actions/yac.html#YAC>`__
#. `Allgemeine Hinweise zu
   Funktionsaufrufen <actions/call.html#AllgemeineHinweisezuFunktionsaufrufen>`__
#. `FritzBox-Konfiguration <actions/config.html#FritzBox-Konfiguration>`__

   #. `Portforwarding <actions/config.html#Portforwarding>`__
   #. `WLAN <actions/config.html#WLAN>`__
   #. `DECT <actions/config.html#DECT>`__
   #. `SIP <actions/config.html#SIP>`__
   #. `Rufumleitung <actions/config.html#Rufumleitung>`__
   #. `Abfragen von
      Konfigurationswerten <actions/config.html#AbfragenvonKonfigurationswerten>`__

#. `Alternative <actions/config.html#Alternative>`__
#. `DreamBox <actions/dreambox.html#DreamBox>`__

   #. `Dreambox mit Enigma
      1 <actions/dreambox.html#DreamboxmitEnigma1>`__

      #. `StandBy Check <actions/dreambox.html#StandByCheck>`__

   #. `DreamBox mit Enigma
      2 <actions/dreambox.html#DreamBoxmitEnigma2>`__

#. `E-Mail-Benachrichtigung <actions/mail.html#E-Mail-Benachrichtigung>`__

   #. `mail <actions/mail.html#mail>`__
   #. `Ersatz für
      mail_missed_call <actions/mail.html#Ersatzfürmail_missed_call>`__

#. `DGStation Relook 400S <actions/relook.html#DGStationRelook400S>`__
#. `Einfache TCP-Verbindungen
   (rawmsg) <actions/rawmsg.html#EinfacheTCP-Verbindungenrawmsg>`__
#. `Wake on LAN <actions/wol.html#WakeonLAN>`__

.. _Third-PartySoftware:

Third-Party Software
--------------------

CallMon2: auf Windows und Linux laufendes Perl-Skript,
`​http://zephyrsoftware.sf.net/ <http://zephyrsoftware.sourceforge.net/?q=fritzbox/callmon2>`__
(dort genaue Informationen zum Einrichten des ganzen!)

-  Tags
-  `callmonitor </tags/callmonitor>`__
