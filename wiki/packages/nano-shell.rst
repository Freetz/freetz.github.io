.. _Nano-Shell:

Nano-Shell
==========

Die **Nano-Shell** führt beliebige Shell-Komandos via URL aus, d.h. an
eine Webadresse angehängte Parameter werden von einem kleinen CGI-Skript
ausgewertet. Die Nano-Shell ist noch kleiner und leichtgewichtiger als
die `Rudi-Shell <rudi-shell.html>`__, denn sie kommt ohne
Einstiegs-Oberfläche aus. Im Folgenden wird der ins Deutsche übersetzte
Hilfetext aus ``make menuconfig`` zitiert, ergänzt um einige zusätzliche
Informationen:

Dieses kleine Paket ermöglicht es sowohl der AVM- als auch der
Freetz-Weboberfläche, benutzerdefinierte Shell-Kommandos auszuführen und
ihre Befehls- bzw. Fehlerausgaben anzuzeigen, falls vorhanden.

.. _Sicherheitshinweis:

Sicherheitshinweis
------------------

|Warning| **ACHTUNG!** Die Nano-Shell sollte nur für Debugging-Zwecke
(Entwicklung, Fehlersuche) verwendet werden, z.B. wenn *telnetd, sshd
(Dropbear)* oder *Rudi-Shell* aus irgendeinem Grund nicht verfügbar bzw.
nicht zugreifbar sind. Sie ist eine Art Reservefallschirm oder letzter
Ausweg, um Kommandos auf der Router-Box auszuführen, wenn alles andere
scheitert, aber zumindest eine der beiden Weboberflächen (AVM oder
Freetz) noch zugreifbar sind. |Warning|

Da die Nano-Shell in der AVM-Oberfläche die Paßwortabfrage umgeht,
handelt es sich hierbei um ein |Warning| **potentielles Sicherheitsrisiko**
|Warning|, sofern Ihre Router-Box aus dem LAN/WAN für Fremde zugreifbar
ist. Das Freetz-Paßwort wird allerdings abgefragt, da es bereits auf
Webserver-Ebene greift und nicht wie bei AVM in der
Web-Applikationslogik implementiert ist.

.. _Benutzung:

Benutzung
---------

Schicken Sie einfach ein URL-kodiertes Kommando an das Nano-CGI, welches
z.B. folgende Basisadressen haben kann:

-  `​http://fritz.box/cgi-bin/shell.cgi <http://fritz.box/cgi-bin/shell.cgi>`__
   (AVM-Weboberfläche)
-  `​http://speedport.ip/cgi-bin/shell.cgi <http://speedport.ip/cgi-bin/shell.cgi>`__
   (AVM)
-  `​http://192.168.0.1/cgi-bin/shell.cgi <http://192.168.0.1/cgi-bin/shell.cgi>`__
   (AVM)
-  `​http://fritz.box:81/cgi-bin/shell.cgi <http://fritz.box:81/cgi-bin/shell.cgi>`__
   (Freetz-Weboberfläche)
-  `​http://speedport.ip:81/cgi-bin/shell.cgi <http://speedport.ip:81/cgi-bin/shell.cgi>`__
   (Freetz)
-  `​http://192.168.0.1:81/cgi-bin/shell.cgi <http://192.168.0.1:81/cgi-bin/shell.cgi>`__
   (Freetz)

oder allgemein eben der Name bzw. die IP-Adresse, unter der Ihre
Router-Box im Netz zu erreichen ist.

Einige Beispiel-Kommandos samt zugehöriger kodierter URLs:

+-----------------------------------+-----------------------------------+
| Kommando                          | URL                               |
+-----------------------------------+-----------------------------------+
| ls -l /var/tmp                    | `​http://fritz.box/cgi-bin/shell. |
|                                   | cgi?ls%20-l%20%2Fvar%2Ftmp <http: |
|                                   | //fritz.box/cgi-bin/shell.cgi?ls% |
|                                   | 20-l%20%2Fvar%2Ftmp>`__           |
+-----------------------------------+-----------------------------------+
| /usr/sbin/telnetd -p 2323 -l      | `​http://fritz.box/cgi-bin/shell. |
| /bin/sh                           | cgi?%2Fusr%2Fsbin%2Ftelnetd%20-p% |
|                                   | 202323%20-l%20%2Fbin%2Fsh <http:/ |
|                                   | /fritz.box/cgi-bin/shell.cgi?%2Fu |
|                                   | sr%2Fsbin%2Ftelnetd%20-p%202323%2 |
|                                   | 0-l%20%2Fbin%2Fsh>`__             |
+-----------------------------------+-----------------------------------+
| echo "Erster Befehl"; cat         | `​http://fritz.box/cgi-bin/shell. |
| /etc/motd; echo "Dritter Befehl"  | cgi?echo%20%22Erster%20Befehl%22% |
|                                   | 3B%20cat%20%2Fetc%2Fmotd%3B%20ech |
|                                   | o%20%22Dritter%20Befehl%22 <http: |
|                                   | //fritz.box/cgi-bin/shell.cgi?ech |
|                                   | o%20%22Erster%20Befehl%22%3B%20ca |
|                                   | t%20%2Fetc%2Fmotd%3B%20echo%20%22 |
|                                   | Dritter%20Befehl%22>`__           |
+-----------------------------------+-----------------------------------+

Es gibt **Online-Kodierer/-Dekodierer** für URLs im WWW, z.B. diesen
`​URL-En-/Decoder <http://netzreport.googlepages.com/online_tool_zur_url_kodierung_de.html#kodieren>`__,
der ASCII und UTF-8 kann, oder auch diesen
`​Encoder <http://www.simplelogic.com/Developer/InetEncode.asp>`__ bzw.
`​Decoder <http://www.simplelogic.com/Developer/URLDecode.asp>`__, der
Sonderzeichen in Latin-1 (ISO-8859-1) (de)kodiert. Außerdem kann man mit
``httpd -d STRING`` via BusyBox ebenfalls URL-Dekodierung machen.

**Usability-Tip** (getestet in IE 7, Opera 9.23, Firefox 2.0.6,
Konqueror 3.5.8): Viele Browser akzeptieren auch unkodierte
CGI-Parameter, also Befehler im Klartext, d.h. normalerweise kann man
anstatt der kodierten Befehle oben auch Folgendes schreiben:

.. code:: bash

   http://fritz.box/cgi-bin/shell.cgi?ls -l /var/tmp
   http://fritz.box/cgi-bin/shell.cgi?/usr/sbin/telnetd -p 2323 -l /bin/sh
   http://fritz.box/cgi-bin/shell.cgi?echo "Erster Befehl"; cat /etc/motd; echo "Dritter Befehl"

Viel Spaß beim Ausprobieren!

`​Alexander Kriegisch
(kriegaex) <http://www.ip-phone-forum.de/member.php?u=117253>`__

-  Tags
-  `cgi </tags/cgi>`__
-  `packages <../packages.html>`__
-  `tools </tags/tools>`__

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

