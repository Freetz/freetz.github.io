.. _AnpassenderBenachrichtigungstexte:

Anpassen der Benachrichtigungstexte
===================================

Um den Inhalt einer Benachrichtigung an die eigenenen Bedürfnisse
anpassen, gibt es folgenden Weg:

#. Verzeichnis ``/tmp/flash/callmonitor/actions.local.d`` erstellen
#. darin eine Datei ``foobar.sh`` anlegen (oder irgendetwas anderes mit
   Endung ``.sh``)
#. dorthinein nur die zu überschreibende Funktion kopieren (z.B.
   ``mail_body() { ... }``) und anpassen (oder nur Variablen setzen wie
   z.B. ``RELOOK_TIMEOUT``)
#. ``modsave flash`` aufrufen, um die Datei im Flash zu sichern
#. Callmonitor neustarten

Bei den meisten `Aktionen <actions.html>`__ ist eine Funktion
``default_foomessage`` vorgesehen, die die Standardnachricht für diesen
Typ Aktion erzeugt; diese Funktion kann also einfach überschrieben
werden. Bei `mailmessage <actions/mail.html>`__ mail gibt es z.B.
``mail_subject`` und ``mail_body``; bei anderen Aktionen hilft nur ein
Blick in den Quelltext (oder eine Nachfrage), solange bis deren
Funktionen auch im Wiki beschrieben sind.
