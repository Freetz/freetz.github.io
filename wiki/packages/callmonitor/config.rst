.. _Konfiguration:

Konfiguration
=============

Die Konfiguration des Callmonitors nimmt man sinnvollerweise in mehreren
Schritten vor, die sich auf verschiedene Seiten im Web-Interface von
Freetz verteilen:

#. Basiskonfiguration durchführen (im Folgenden beschrieben)
#. Listeners für bestimmte Aktionen definieren
#. mit einem Testanruf die Konfiguration testen

.. _Basiskonfiguration:

Basiskonfiguration
------------------

Auf der Seite Pakete-Callmonitor des Web-Interfaces lassen sich einige
grundlegende Einstellungen vornehmen.

Als erstes wählt man den Starttyp - normalerweise "Automatisch", da der
Callmonitor sonst nach jedem Neustart der FritzBox per Hand gestartet
werden muss. Sollte es Probleme geben, kann man noch zusätzlich die
Debug-Ausgaben aktivieren, was jedoch normalerweise unnötig ist.

Der nächste Block bietet lediglich Links zu den Listeners und zur
Durchführung von Testanrufen.

Im folgenden Block lassen sich die Standort-Angaben (Landes- und
Ortsvorwahl) noch einmal überprüfen und über einen Link zum AVM-WebGUI
auch anpassen. Es ist zu beachten, dass Änderungen der Landes- und/oder
Ortsvorwahl erst auf der Callmonitor-Seite angezeigt werden, wenn der
Callmonitor neu gestartet wurde.

So weit sind wir aber noch nicht, vorher sind noch die Einstellungen zur
Rückwärtssuche im dritten Block zu überprüfen. Sie kann komplett
deaktiviert werden, dafür ist die Checkbox vor "Rückwärtssuche
durchführen bei" zuständig. Möchte man sie benutzen, kann der `Dienst
für die Rückwärtssuche <reverse_search.html>`__ ausgewählt werden, an
den die Anfragen geschickt werden. **Achtung:** Diese Funktion setzt
eine bestehende Internetverbindung voraus - es empfiehlt sich also
irgendeine Art von always-on Flatrate für den Internetzugang zu
verwenden (z.B. Volumentarif, komplette Flat).

Falls die Telefonnummer nicht gefunden werden kann (z.B. weil der
Teilnehmer der Rückwärtssuche widersprochen hat), wird ersatzweise die
Vorwahl bei dem dort ausgewählten Dienst nachgeschlagen. Dadurch kann
zumindest der Ort angezeigt werden. Zum Schluss kann noch ausgewählt
werden, ob die Ergebnisse der Rückwärtssuche dauerhaft im Telefonbuch
(also im Flash der Box) oder flüchtig (d.h. bis zum Neustart) im
Speicher abgelegt werden. Es ist auch möglich, die Zwischenspeicherung
ganz abzuschalten. Dann wird die Rückwärtssuche immer wieder neu
durchgeführt, selbst wenn dieselbe Rufnummer schon einmal nachgeschlagen
wurde.

Die Einstellung "Vorwahl für lokale Rufnummern" wird benötigt, da im
Ortsnetz nicht (immer) die Vorwahl mit übertragen wird. In aktuellen
Versionen wird die Vorwahl automatisch aus den Einstellungen zur
Internettelefonie übernommen (in der Weboberfläche von AVM).

.. _Listenersdefinieren:

Listeners definieren
--------------------

Als nächstes müssen sogenannte Listeners definiert werden, die dann bei
eingehenden Anrufen die gewünschte Aktion starten. Genaueres hierzu auf
einer `speziellen Seite für die Listeners <listeners.html>`__.

.. _Testanruf:

Testanruf
---------

Sind die Listeners einmal definiert, kann und sollte man sie mit einem
Testanruf ausprobieren. Dafür kann man natürlich einen echten Anruf
machen - allerdings hat man oft nicht die Möglichkeit, spezielle Regeln
zu testen. Daher gibt es die Möglichkeit, einen Testanruf über das
Web-Interface zu generieren - eine genaue Beschreibung findet sich
`hier <testcall.html>`__.

.. _Fehlersuche:

Fehlersuche
-----------

Die Ausgaben des Testanrufs und ggf. die Debug-Meldungen (siehe oben, um
das log zu sehen vorher in freetz-konfig diese option aktivieren um sie
in das image einzubauen) geben in den meisten Fällen ausreichend
Hinweise, warum die Aktion nicht ausgeführt wurde bzw. der Callmonitor
nicht startet. Außerdem lohnt sich auch ein Blick auf die
`Wartungsseite <maintenance.html>`__ - falls die
Callmonitor-Schnittstelle deaktiviert ist, kann dieser auch nicht
funktionieren. Einschalten mit einem Anruf der Fritzbox von einem
angeschlossenem Telefon aus mit der Nummer: `#96 </ticket/96>`__\ \*5\*
kann helfen. Wenn das alles nicht weiterhilft, kann man auf der
`​Forumsseite für Fragen und
Diskussionen <http://www.ip-phone-forum.de/showthread.php?t=100706>`__
Unterstützung bekommen.

-  Tags
-  `callmonitor </tags/callmonitor>`__
