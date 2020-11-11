.. _TelefonbuchCallers:

Telefonbuch (Callers)
=====================

Format:

   <Rufnummer mit Vorwahl>\ ````\ <Name>(``;`` <Adresse>)

Ergebnisse der `Rückwärtssuche <reverse_search.html>`__ können hier
gespeichert werden für schnelleren Zugriff in der Zukunft; natürlich
können auch von Hand Nummer-Name-Paare eingetragen oder geändert werden

-  49er-Rufnummern (ohne 00, länger als 10 Zeichen) werden erkannt
-  Name des Angerufenen steht zur Verfügung (vor allem für SIP0 bis
   SIP9); man kann die Zuordnung zu Namen im Telefonbuch (Callers)
   vornehmen, entweder direkt für SIP0 bis SIP9 oder für Adressen der
   Form "username@registrar" (das zweite hat den Vorteil, dass man im
   Telefonbuch nichts anpassen muss, wenn man seine SIP-Accounts in
   anderer Reihenfolge einträgt). Beim Start werden Kurznamen für alle
   Accounts generiert und als Vorgabe in die Callers eingetragen.
-  Suchstrategie: Erst Nummer unverändert in den lokalen Telefonbüchern
   (Callers, AVM-Telefonbuch) nachschlagen, dann normalisieren (evtl.
   Orts- /Landesvorwahl davor; SIP[0-9] wird zu username@registrar) und
   noch einmal lokal probieren. Dann erst über Rückwärtssuche im
   Internet probieren.

.. figure:: /screenshots/216.png
   :alt: Callmonitor Callers

   Callmonitor Callers

| 

-  Tags
-  `callmonitor </tags/callmonitor>`__
