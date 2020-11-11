.. _RegelnListeners:

Regeln (Listeners)
==================

Die Listeners-Datei enthält eine Liste von Regeln, die festlegen, welche
`Aktionen <actions.html>`__ unter welchen Bedingungen ausgeführt werden
sollen.

Leerzeilen werden ignoriert, ebenso Zeilen, die mit *#* beginnen (das
sind Kommentare).

Jede Regel steht in einer Zeile und besteht aus vier Angaben, die durch
Leerraum getrennt in dieser Reihenfolge aufeinander folgen:

#. Ereignis
#. Quellrufnummer: Muster für SOURCE
#. Zielrufnummer: Muster für DEST
#. Aktion: Beliebiger Shell-Code

Die beiden Muster für *SOURCE* und *DEST* sind `​"extended regular
expressions"
(ERE) <http://www.selflinux.org/selflinux/html/regex.html>`__, wie sie
von *egrep* verstanden werden. Das Ereignis (ein-/ausgehender Anruf;
Klingeln, Annahme, etc.) wird mit der unten angeführten Syntax
angegeben.

Man kann negative Muster bei den Listeners verwenden, indem man ein
Ausrufezeichen voranstellt: ``!123`` passt auf alle Nummern, die nicht
irgendwo 123 enthalten.

Beispiele:

+-----------------------------------+-----------------------------------+
| \| Muster                         | \| passt auf                      |
+-----------------------------------+-----------------------------------+
| ``^``                             | alle Nummern                      |
+-----------------------------------+-----------------------------------+
| ``^034``                          | Nummern, die mit 034 beginnen     |
+-----------------------------------+-----------------------------------+
| ``4563$``                         | Nummern, die auf 4563 enden       |
+-----------------------------------+-----------------------------------+
| ``!^(045|0164)``                  | Nummern, die **nicht** mit 045    |
|                                   | oder 0164 beginnen                |
+-----------------------------------+-----------------------------------+
| ``^0123456$``                     | nur genau die Nummer 0123456      |
+-----------------------------------+-----------------------------------+
| ``^04553...$``                    | die Nummern, bei denen nach 04553 |
|                                   | genau drei weitere Zeichen folgen |
+-----------------------------------+-----------------------------------+

Alle Regeln werden parallel abgearbeitet; eine bestimmte Reihenfolge ist
nicht garantiert.

Damit die Listeners über das Webinterface von Freetz bearbeitet werden
können, muss dessen Sicherheitsstufe auf 0 gesetzt werden. Das ist
nötig, da über die Listeners beliebiger Code ausgeführt werden kann.

.. figure:: /screenshots/20.png
   :alt: Callmonitor: Listener Konfiguration

   Callmonitor: Listener Konfiguration

.. _Format:

Format
------

Seit Version 1.0 des Callmonitors gilt folgendes Format für die
Listeners, mit dem auf bis zu acht verschiedene Ereignisse
unterschiedlich reagiert werden kann:

-  **\*:request**: Anruf kommt an (es klingelt)
-  **\*:cancel**: Anruf wurde abgebrochen, bevor eine Verbindung
   zustande kam (so kann man direkt auf "verpasste Anrufe" reagieren)
-  **\*:connect**: Verbindung beginnt
-  **\*:disconnect**: Verbindung wurde beendet

Dazu kommt die Unterscheidung zwischen

-  **in:\***: eingehenden und
-  **out:\***: ausgehenden Anrufen.

Das ergibt folgende Menge von Ereignissen:

+-----------+---------------+--------------+---------------+------------------+
| \|        | \| \*:request | \| \*:cancel | \| \*:connect | \| \*:disconnect |
+-----------+---------------+--------------+---------------+------------------+
| \| in:\*  | in:request    | in:cancel    | in:connect    | in:disconnect    |
+-----------+---------------+--------------+---------------+------------------+
| \| out:\* | out:request   | out:cancel   | out:connect   | out:disconnect   |
+-----------+---------------+--------------+---------------+------------------+

Dazu passend haben die Listeners eine zusätzliche erste Spalte bekommen,
in der (mit Hilfe von Abkürzungen und Wildcards) das gewünschte Ereignis
angegeben werden kann, auf das die betreffende Regel reagieren soll:

.. code:: bash

   in:request  ^       ^1234$  xboxmessage xbox
   in:cancel   ^       ^       mailmessage -t test@example.com
   out:cancel  ^1234$  ^0123   dboxpopup dbox-a "${DEST} geht nicht ran"
   *:dis       ^       ^       echo "Anruf beendet: ${DURATION} Sekunden" >> log

Es kann mehrere Regeln geben, die auf dasselbe Ereignis passen.

Die Präfixe "NT:", "E:" und "*:" in der *SOURCE*-Spalte gibt es nicht
mehr. Eure bisherige Listeners-Datei (vor Version 1.0) könnt ihr nicht
einfach weiterverwenden. Der CallMonitor versucht aber, beim ersten
Start eine grobe Konvertierung vorzunehmen, um euch den Umstieg zu
erleichtern. Auf jeden Fall solltet ihr aber die Listeners nach der
Umstellung einmal kontrollieren.

| Die Spalten 2 und 3 in den Listeners sind weiterhin Muster (reguläre
  Ausdrücke) für Quell- und Zielrufnummer (*SOURCE* und *DEST*).
| Dabei ist jedoch zu beachten, dass in Spalte 2 bzw. 3 die MSNs, also
  die Internet-Rufnummern, anzugeben sind und nicht wie früher bspw.
  *SIP0* oder *SIP1*.

.. _Ereignis-InformationenfürAktionen:

Ereignis-Informationen für Aktionen
-----------------------------------

Den Aktionen stehen Informationen über den auslösenden Anruf in
Umgebungsvariablen bereit. Sie werden in Shell-Scripten mit einem $
referenziert, also z.B. ``echo $SOURCE_NAME``.

+-----------------------+-----------------------+-----------------------+
| \| Variable           | \| Inhalt             | \| seit Version       |
+-----------------------+-----------------------+-----------------------+
| EVENT                 | das auslösende        | 1.0                   |
|                       | Ereignis              |                       |
+-----------------------+-----------------------+-----------------------+
| ID                    | die ID des Anrufs     | 1.0                   |
|                       | (direkt von der       |                       |
|                       | Callmonitor-Schnittst |                       |
|                       | elle)                 |                       |
+-----------------------+-----------------------+-----------------------+
| UUID                  | Global eindeutige ID  | 1.20                  |
|                       | für diesen Anruf      |                       |
|                       | (nicht für dieses     |                       |
|                       | Ereignis!)            |                       |
+-----------------------+-----------------------+-----------------------+
| TIMESTAMP             | der Zeitpunkt des     | 1.0                   |
|                       | Ereignisses (im       |                       |
|                       | Format "DD.MM.YY      |                       |
|                       | HH:MM")               |                       |
+-----------------------+-----------------------+-----------------------+
| SOURCE                | Quellrufnummer        | —                     |
+-----------------------+-----------------------+-----------------------+
| SOURCE_DISP           | "anzeigefreundlichere | 1.8                   |
|                       | "                     |                       |
|                       | Variante von SOURCE   |                       |
|                       | (Landesvorwahl weg,   |                       |
|                       | Call-by-Call-Vorwahle |                       |
|                       | n                     |                       |
|                       | weg, etc.)            |                       |
+-----------------------+-----------------------+-----------------------+
| SOURCE_NAME           | Name der Quelle,      | —                     |
|                       | falls dieser bestimmt |                       |
|                       | werden konnte         |                       |
+-----------------------+-----------------------+-----------------------+
| SOURCE_ADDRESS        | Die Adresse (Straße,  | 1.12                  |
|                       | Stadt, Land) ist seit |                       |
|                       | 1.12 separat          |                       |
|                       | verfügbar und nicht   |                       |
|                       | mehr in SOURCE_NAME   |                       |
|                       | enthalten             |                       |
+-----------------------+-----------------------+-----------------------+
| SOURCE_ENTRY          | Der ganze             | 1.12                  |
|                       | Telefonbucheintrag    |                       |
|                       | (entspricht dem       |                       |
|                       | SOURCE_NAME vor 1.12) |                       |
+-----------------------+-----------------------+-----------------------+
| DEST                  | Zielrufnummer         | —                     |
+-----------------------+-----------------------+-----------------------+
| DEST_DISP             | "anzeigefreundlichere | 1.8                   |
|                       | "                     |                       |
|                       | Variante von DEST     |                       |
|                       | (Landesvorwahl weg,   |                       |
|                       | Call-by-Call-Vorwahle |                       |
|                       | n                     |                       |
|                       | weg, etc.)            |                       |
+-----------------------+-----------------------+-----------------------+
| DEST_NAME             | Name des Ziels, falls | —                     |
|                       | dieses bestimmt       |                       |
|                       | werden konnte         |                       |
+-----------------------+-----------------------+-----------------------+
| DEST_ADDRESS          | Die Adresse (Straße,  | 1.12                  |
|                       | Stadt, Land) ist seit |                       |
|                       | 1.12 separat          |                       |
|                       | verfügbar und nicht   |                       |
|                       | mehr in DEST_NAME     |                       |
|                       | enthalten             |                       |
+-----------------------+-----------------------+-----------------------+
| DEST_ENTRY            | Der ganze             | 1.12                  |
|                       | Telefonbucheintrag    |                       |
|                       | (entspricht dem       |                       |
|                       | DEST_NAME vor 1.12)   |                       |
+-----------------------+-----------------------+-----------------------+
| EXT                   | die Nebenstelle,      | 1.0                   |
|                       | sofern bekannt        |                       |
|                       | (direkt von der       |                       |
|                       | Callmonitor-Schnittst |                       |
|                       | elle)                 |                       |
+-----------------------+-----------------------+-----------------------+
| DURATION              | bei \*:disconnect die | 1.0                   |
|                       | Dauer des Gesprächs   |                       |
|                       | in Sekunden           |                       |
+-----------------------+-----------------------+-----------------------+
| PROVIDER              | Dienstleister, über   | 1.5                   |
|                       | den der Anruf         |                       |
|                       | abgewickelt wird      |                       |
|                       | ("POTS" für Festnetz  |                       |
|                       | oder "SIP0", "SIP1",  |                       |
|                       | … für die             |                       |
|                       | verschiedenen         |                       |
|                       | SIP-Provider)         |                       |
+-----------------------+-----------------------+-----------------------+

EXT kann auf einer FritzBox 7050 folgende numerische Werte haben (bei
einem eingehenden Anruf liegt diese Information erst ab in:connect vor;
vorher ist die Zuordnung ja nicht klar):

+--------+------------------+
| \|Wert | \|Bedeutung      |
+--------+------------------+
| 0      | FON 1            |
+--------+------------------+
| 1      | FON 2            |
+--------+------------------+
| 2      | FON 3            |
+--------+------------------+
| 3      | Durchwahl        |
+--------+------------------+
| 4      | Fon S0           |
+--------+------------------+
| 5      | Fon/Fax PC       |
+--------+------------------+
| 6      | Anrufbeantworter |
+--------+------------------+
| 36     | Data S0          |
+--------+------------------+
| 37     | Data PC          |
+--------+------------------+

.. _FormatierungderAusgaben:

Formatierung der Ausgaben
-------------------------

Zur Formatierung der Ausgaben stehen folgende Funktionen bereit:

seit Version 1.8:

-  f_duration: zur Darstellung von Zeitdauern als "hh:mm:ss"

   .. code:: bash

      f_duration <ZEIT_IN_SEKUNDEN>

        ZEIT_IN_SEKUNDEN:      Zeit in Sekunden, z.B. $DURATION

Beispiel:

::

   echo "Der Anruf dauerte $(f_duration $DURATION)"

führt zu einer Ausgabe

.. code:: bash

   Der Anruf dauerte 1:05:03

falls DURATION den Wert 3903 hat.

Als nützlich kann sich auch die Konstante $LF erweisen, die einen
Zeilenumbruch enthält (line feed):

::

   dboxmessage foo.bar "Zeile 1${LF}Zeile 2"

.. _MusterfürEreignisse:

Muster für Ereignisse
---------------------

Es gibt mehrere Möglichkeiten, in den Listeners die Ereignisse
anzugeben, bei der eine Regel auslösen soll:

-  Vollständige Ereignisnamen:

   .. code:: bash

      in:request
      out:disconnect

-  Abkürzungen des vorderen und/oder hinteren Teils:

   .. code:: bash

      in:req
      out:disc
      i:r
      o:d

-  Wildcards für den vorderen Teil (Richtung), den hinteren oder beide:

   .. code:: bash

      *:req
      ou:*
      *

-  Listen dieser Bestandteile (mit Komma getrennt (Vorsicht, kein
   Whitespace); die Regel passt, wenn einer der Teile passt):

   .. code:: bash

      in:req,out:*

.. _Beispiele::

Beispiele:
----------

Verpasster Anruf (in:cancel) mailmessage an mehrere Email Adressen
versenden:

.. code:: bash

   in:cancel ^ ^ mailmessage -t user1@example.com,user2@example.com

Von einer bestimmten Rufnummer (0401234567) eine festgelegte Rufnummer
(0401234568) anrufen und den PC über WOL (Wake on Lan) einschalten:

.. code:: bash

   in:request ^0401234567 ^0401234568 ether-wake -i eth0 00:13:DE:01:A4:DE

Benachrichtigungen über Dreambox mit Enigma2 auf Fernseher anzeigen:

.. code:: bash

   in:request ^ ^ dream2message --user=root --pass=dreambox 192.168.178.104

Benachrichtigung per Email bei Faxempfang:

.. code:: bash

   in:disconnect ^ 0401234567$ mailmessage -s "Faxeingang von $SOURCE"

-  Tags
-  `callmonitor </tags/callmonitor>`__
