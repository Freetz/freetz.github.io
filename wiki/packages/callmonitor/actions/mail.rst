.. _E-Mail-Benachrichtigung:

E-Mail-Benachrichtigung
=======================

Die Funktion ``mailmessage`` verschickt eine E-Mail mit Hilfe der Daten,
die für den Push-Service eingerichtet sind (falls man nicht beim Aufruf
etwas anderes befiehlt (mailer-Optionen)). Der Push-Service selbst kann
ruhig ausgeschaltet bleiben, wichtig sind die Einstellungen für
Adressen, Mailserver & Co. Beispiele zum Einsatz in Listeners:

.. code:: bash

   mailmessage
   mailmessage -t me@my.self
   mailmessage -s "Oh, oh ... ($SOURCE)"

-  Mailadressen, Servereinstellungen, Passwörter & Co. werden aus der
   Konfiguration des Push Service der FritzBox übernommen. Einzelne
   Teile können durch Optionen überschrieben werden (im Beispiel zum
   Beispiel die Zieladresse mit ``-t``).
-  Die Optionen werden an ``mail`` durchgereicht; diese wiederum
   größtenteils an ``mailer``. Deswegen können folgende Optionen
   verwendet werden:

   .. code:: bash

        -s STRING          - Subject. ("FRITZ!Box")
        -f STRING          - From. (NULL)
        -t STRING          - To. (NULL)
        -m STRING          - mailserver. (NULL)
        -a STRING          - authname. (NULL)
        -w STRING          - passwd. (NULL)
        -d STRING          - attachment. (NULL)
        -i STRING          - inline attachment. (NULL)

-  Zur Anpassung der Mails: siehe ``mail_subject`` und ``mail_body`` in
   ``mail.sh`` (zum Überschreiben am besten
   ``/tmp/flash/callmonitor/actions.local.d/`` verwenden, siehe
   `Anpassen der Benachrichtigungstexte <../adapt_messages.html>`__).

mail
----

``mail`` ist ein Skript, um Mails bei Mailserverfehlern
zwischenzuspeichern und erneut zu schicken (alle Parameter und
Attachments werden gepackt in ``/var/spool/mail/`` abgelegt).

-  Es wird von der Aktion mailmessage verwendet.
-  Ihr solltet regelmäßig (mit cron) ein ``mail process`` ausführen, um
   evtl. wartende Mail zu versenden.
-  ``mail`` gehört streng genommen nicht unbedingt zum Callmonitor, weil
   auch andere Dienste es brauchen könnten; vielleicht wird in Zukunft
   mal ein eigenes Paket daraus.

.. _Ersatzfürmail_missed_call:

Ersatz für mail_missed_call
---------------------------

Die Funktion ``mail_missed_call`` existiert seit Version 1.0 nicht mehr.
An ihre Stelle tritt eine allgemeine Benachrichtigungsfunktion per
E-Mail (``mailmessage``), die (auch) in Kombination mit dem Ereignis
``in:cancel`` genutzt werden kann, um bei verpassten Anrufen eine Mail
zu verschicken:

.. code:: bash

   in:cancel   ^   ^   mailmessage

Das schöne ist, dass die Mail sofort rausgeschickt wird, wenn der
Gesprächspartner aufgibt; es gibt keine Wartezeit von einer Minute mehr
wie in den Vorversionen. Außerdem kann jetzt zuverlässiger bestimmt
werden, wann ein Anruf verpasst wurde.

Aber natürlich kann man sich so auch per Mail über alle eingehenden
Anrufe informieren lassen, oder über alle ausgehenden an eine bestimmte
Nummer oder oder oder …
