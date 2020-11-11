knockd
======

*"Wer klopfet, dem wird aufgetan"* - so könnte man dieses Paket
überschreiben. *knockd* bietet eine gute Möglichkeit, Dienste von Remote
zu starten. Läuft der (übrigens sehr resourcenschonende) Knock-Daemon
auf der Fritzbox, so kann man z.B. - bei entsprechender Konfiguration -
durch das korrekte "Klopfzeichen" signalisieren, dass man "rein möchte".
Wurde der richtige "Knock Code" gesendet, startet knockd das zugehörige
Programm (z.B. den SSH Daemon). Ein weiteres "Klopfen" beendet ihn dann
später wieder. Dieses Vorgehen bietet zusätzliche Sicherheit, da Ports
nur dann offen sind, wenn man sie auch wirklich braucht - der Portscan
eines Hackers läuft also damit meist ins Leere.

.. _WeiterführendeLinks::

Weiterführende Links:
---------------------

-  `​Ein kurzer Workshop zu
   knockd <http://wiki.hetzner.de/index.php/Knockd>`__
-  `​Artikel zu
   "Portknocking" <http://blog.roothell.org/archives/146-Portknocking-Tools-Teil-1-knockd.html>`__
-  `​Knockd Demo auf
   Youtube <http://www.youtube.com/watch?v=EbzrLPf6D7Y>`__

-  Tags
-  `daemons </tags/daemons>`__
-  `network </tags/network>`__
-  `packages <../packages.html>`__
-  `security </tags/security>`__
-  `server </tags/server>`__
