.. _SundtekDVBTreiber:

Sundtek DVB Treiber
===================

.. figure:: /screenshots/256.jpg
   :alt: Sundtek DVB driver

   Sundtek DVB driver

Dieses Package stellt den Treiber für USB-Sticks von Sundtek bereit, mit
denen DVB (c/s/t) empfangen werden kann.

| |Warning| Die Fritzbox sollte mindestens USB 2.0 haben, 11 MBit/s reichen
  nicht aus.
| |Warning| Mit Kernel 2.6.19.2 (Fritzbox 7270v1 und 7570) gibt es momentan
  ein Memoryleak, siehe `#472 </ticket/472>`__.

.. _Parameterfürmediaclient:

Parameter für 'mediaclient'
---------------------------

In dieses Textfeld können Parameter zum initialisieren für den
``mediaclient`` eingetragen werden. Wenn dies genutzt wird, wird die
Hardwareerkennung vom ``mediasrv`` abgewartet was etwa 10 Sekunden
benötigt

.. _Treiberverwenden:

Treiber verwenden
-----------------

Um den Treiber benutzen zu können muss vorher dieser Befehl ausgeführt
werden:

.. code:: bash

   export LD_PRELOAD=/usr/lib/libmediaclient.so

.. _USB-Stickinitialisieren:

USB-Stick initialisieren
------------------------

Der USB-Stick muss für die Fritzbox in den Übertrangungsmodus "bulk"
versetzt werden:

.. code:: bash

   mediaclient --dtvtransfermode=bulk

Dies ist nur einmalig nötig und der Stick muss danach neu angesteckt
werden.

.. _Weiteres:

Weiteres
--------

Nutzbar z.B. zur Aufzeichnung der Auslastung des Segmentes von
Kabelinternet mit `RRDstats <rrdstats.html#segment>`__. Es soll damit
auch Streaming zu einem Windows PC mit einer aktuellen Betaversion des
DVB-Viewer via SAT>IP möglich sein.

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

