.. _DreamBox:

DreamBox
========

.. _DreamboxmitEnigma1:

Dreambox mit Enigma 1
---------------------

.. code:: bash

     dreammessage [user[:password]@]host[:port] ["Alternative Nachricht"]

.. figure:: /screenshots/1.jpg
   :alt: CallMonitor: Dreambox Auth abschalten

   CallMonitor: Dreambox Auth abschalten

Wie zu sehen ist, ist "host" (also Rechnername oder IP-Adresse) der
einzige Pflichtparameter. Damit die Nachricht aber auch wirklich
ankommt, muss die Authentifizierung berücksichtigt werden. Eine Lösung
ist es, wie beigefügter Screenshot aufzeigt, das Abschalten der
Nachrichten-Authentifizierung auf der Box selbst. Wer das nicht will,
dem bleibt zur Zeit nur, ``user:password@`` vor den Host zu setzen - was
dann allerdings bei den Listeners im Klartext angezeigt wird.

``dreammessage`` kennt ein Standard-Nachrichten-Template, was
normalerweise verwendet wird. Wer die Nachricht lieber selbst
formatieren will, findet
`hier <../listeners.html#Ereignis-InformationenfürAktionen>`__ eine
Liste mit verwendbaren Platzhaltern für Telefonnummer, Zeilenumbrüche,
usw.

Desweiteren gibt es drei Umgebungsvariablen, die das Verhalten von
``dreammessage`` beeinflussen. Sie sind hier in einem typischen Aufruf
mit ihren Standardwerten gezeigt:

.. code:: bash

     DREAM_TIMEOUT=10 DREAM_CAPTION="Telefonanruf" DREAM_ICON=1 dreammessage box1

.. _StandByCheck:

StandBy Check
~~~~~~~~~~~~~

Befindet sich die zu benachrichtigende Dreambox im StandBy, werden die
Nachrichten solange zwischengespeichert, bis sie wieder aus selbigem
aufwacht. An und für sich ganz nett - nur wenn man sie gerade mal ein
paar Tage nicht benutzt hat, und dann nach dem Anschalten erstmal
hunderte von "verpassten" Anrufen zu sehen bekommt. Daher wäre es für
manchen sicher praktisch, würden die Nachrichten nur dann (und zwar
sofort) zugestellt, wenn die Dreambox sich zum Zeitpunkt des Anrufes
*nicht* im StandBy befindet - während andernfalls die Benachrichtigung
komplett unterbliebe.

Glücklicherweise ist das machbar (getestet mit DM600, DM 7000 und
DM7020). Auf folgende Weise lässt sich nämlich der Status ermitteln:

::

   # keine Passwort-Authentifizierung aktiv:
   standby=`wget -O- "http://dreambox/cgi-bin/status" | awk '/Standby/' | sed -e 's/<[^>]*>//g'`
   # mit Passwort-Authentifizierung:
   standby=`wget -O- --http-user=root --http-passwd=dreambox "http://dreambox/cgi-bin/status" | awk '/Standby/' | sed -e 's/<[^>]*>//g'`

Je nachdem, ob das WebIF für Passwort-Authentifizierung konfiguriert ist
oder nicht, kann man also die entsprechende Variante nutzen. Das
busybox-wget unterstützt allerdings keine Authentifizierung. Daher muss
beim Bauen von freetz das Paket 'wget' installiert werden. Die Variable
``$standby`` ist anschließend entweder mit ``STANDBY:ON`` oder
``STANDBY:OFF`` belegt. Für unsere Benachrichtigungs-Aktion können wir
uns das wie folgt nutzbar machen:

::

   [ "$(wget -O- "http://dreambox/cgi-bin/status" | awk '/Standby/' | sed -e 's/<[^>]*>//g')" = "Standby:OFF" ] && DREAM_TIMEOUT=10 dreammessage dreambox "${SOURCE_DISP} ruft an.${LF}${SOURCE_NAME}"

wobei natürlich *dreambox* mit dem Hostnamen bzw. der IP-Adresse der
Dreambox ersetzt, sowie ggf. die Passwort-Authentifizierung mit
eingebaut werden muss.

*Quelle:*\ `​IPPF
Thread <http://www.ip-phone-forum.de/showthread.php?t=100706&page=55>`__

.. _DreamBoxmitEnigma2:

DreamBox mit Enigma 2
---------------------

.. code:: bash

     dream2message (default_dream2message)

``DREAM_TIMEOUT`` und ``DREAM_ICON`` werden auch hier unterstützt.

| Beispiel für ein Popup das nur den Namen (sofern in der Callers
  vorhanden) und die Telefonnummer des Anrufers anzeigt:

.. code:: bash

   in:request ^ ^ dream2message 192.168.178.25 "${SOURCE_NAME} ${SOURCE} ruft an."
