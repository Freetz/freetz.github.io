`​Snarl <http://www.fullphat.net/index.php>`__ ist ähnlich wie Growl,
welches einigen vielleicht bekannt ist, ist ein
Benachrichtigungs-Programm ("notification"), welches im Hintergrund
läuft und von verschiedenen Programmen etc. angesprochen werden kann.
Vorteil ist, dass man so benutzerdefinierte, systemweit einheitliche
Benachrichtigungen erhält.

Snarl verwendet ein eigenes Protokoll, welches sich SNP (`​Snarl Network
Protocol <http://www.fullphat.net/dev/snp/index.htm>`__) nennt.

Mittels "rawmsg" wird an eine IP (Port 9887) im Netzwerk, an dem Snarl
wiederum selbst lauschen muss, eine Nachricht gesendet. Snarl zeigt
diese vom Callmonitor über SNP übermittelte Benachrichtigung dann an.

Also z. B. so:

.. code:: bash

   echo -n "type=SNP#?version=1.0#?action=notification#?title=Anruf#?text=${SOURCE}#?timeout=20"$'\r\n' | nc IP 9887

(buehmann hat in diesem
`​Thread <http://www.ip-phone-forum.de/showthread.php?t=216938>`__
gezeigt, wie es geht. Danke!)

.. _Listener-Eintrag::

Listener-Eintrag:
-----------------

Der Listener-Eintrag im Callmonitor kann dazu z.B. so aussehen:

.. code:: bash

   in:request ^ ^ echo -n "type=SNP#?version=1.0#?action=notification#?title=eingehender Anruf#?text=von ${SOURCE} - ($SOURCE_NAME)${LF}für ${DEST_NAME} - (${DEST_DISP})${LF}#?timeout=20#?icon=C:\pic.png"$'\r\n' | nc 192.168.178.20 9887

.. _Screenshots::

Screenshots:
------------

So könnte eine Benachrichtung von Snarl dann aussehen. Die Angaben
betreffend Anrufer, Rufnummer, Ereignis etc., lassen sich ja mittels des
Callmonitor entsprechend anpassen bzw. erweitern.

   .. figure:: /screenshots/171.png
      :alt: Snarl Beispiel

      Snarl Beispiel

   .. figure:: /screenshots/167.png
      :alt: Snarl Beispiel

      Snarl Beispiel

   .. figure:: /screenshots/173.png
      :alt: Snarl Beispiel

      Snarl Beispiel

..

   Wichtig: "Curl" oder "getmsg" können nicht benutzt werden, diese sind
   nur für das HTTP (Protokoll) geeignet und funktionieren nicht mit dem
   SNP von Snarl.
