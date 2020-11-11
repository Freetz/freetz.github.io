.. _Aiccu:

Aiccu
=====

.. _FirmwareImageerstellen:

Firmware Image erstellen
------------------------

Zunächst rufen wir das Menuconfig auf:

.. code:: bash

   make menuconfig

Es muss zunächst euer Router ausgewählt sein, auch "Show advanced
options" und das darunter erscheinende "Enable IPv6 support". Zudem
werden folgende Pakte benötigt:

.. code:: bash

   Standard Packages -> Dnsmasq
   Web Interface -> NHIPT Iptables CGI
   Web Interface -> NHIPT->Select kernel modules (IPv6) -> ip6_tables.ko
   Web Interface -> NHIPT->Select kernel modules (IPv6) -> ip6table_filter.ko
   Web Interface -> NHIPT->Select shared libraries (IPv6) -> libip6t_icmp6.so
   Unstable -> aiccu
   Unstable -> radvd
   Unstable -> traceroute6

Jetzt speichert und verlasst ihr die Konfiguration. Falls dies die erste
Erstellung eines Images ist, müsst ihr nun zunächst mit ``make`` die für
den nächsten Schritt benötigten Dateien erstellen.

Nachdem der Vorgang abgeschlossen ist, gebt ihr in die Konsole diesen
Befehl ein:

.. code:: bash

   make kernel-menuconfig

In diesem Menü aktiviert ihr nun folgende Optionen:

.. code:: bash

   Loadable module support > Automatic kernel module loading (CONFIG_KMOD=y)
   Networking  > Networking options > IPv6: IPv6-in-IPv4 tunnel (SIT driver) (CONFIG_IPV6_SIT=y)

Auch hier müsst ihr danach die Menüs mit "Exit" verlassen und die Frage,
ob ihr das Speichern wollt, mit "Yes" beantworten.

| Hinweis CONFIG_KMOD:
| Option ist nicht als Default aktiviert, da manche Module nicht geladen
  werden, sobald kein "Replace Kernel" benutzt wird.
| Bessere Alternative: In der Freetz-Weboberfläche kann über
  "Einstellungen > Freetz: modules" Modul XXX hinzugefügt werden.
| Vorsicht: FREETZ_SECURITY_LEVEL=1 (Default) reicht nicht, siehe auch
  `Security
  Levels <../FAQ.en.html#Settingsarenotavailableatcurrentsecuritylevel>`__.
| (Quellcode: 7170: make/linux/Config.ohio-8mb.04.80:59:# CONFIG_KMOD is
  not set)

| Hinweis CONFIG_IPV6_SIT:
| Für Kernel 2.6.19.2 (z.B. 7270) is Option bereits aktivert und für
  2.6.13.1 (z.B. 7170) nicht auswählbar.
| (Quellcode: 7270:
  make/linux/Config.ur8-16mb.7270_04.86:344:CONFIG_IPV6_SIT=y)

Zum Schluss führt nochmal den Befehl ``make`` aus.

Das entstandene Image im Ordner "images" kann nun über das Webinterface
eingespielt werden.

.. _Netzwerksetup:

Netzwerksetup
-------------

Wählt den Punkt "Pakete" aus, um aiccu und radvd zu konfigurieren.
Zuerst aiccu:

.. code:: bash

   Starttyp: Automatisch
   Benutzername: Euer SixXS Benutzername
   Passwort: Euer SixXS Passwort
   Tunnel ID: ID des dynamischen Tunnels (z.B. T1234)
   Name des virt. IPv6 Interface: sixxs

Klickt anschließend auf "Übernehmen", um die Einstellungen zu speichern.
Als nächstes wird radvd konfiguriert. Dazu benötigt ihr ein aktives
Subnet, dass zu eurem Tunnel geroutet wird. Lautet euer Prefix
beispielsweise !2001:6f8:1234::/48, so muss die Konfiguration
folgendermaßen aussehen:

.. code:: bash

   Starttyp: Automatisch
   IPv6 Schnittstelle: lan
   IPv6 Adresse: 2001:6f8:1234::1/64
   IPv6 Prefix: 2001:6f8:1234::/64

Achtung: Dies ist kein Tippfehler! In der Konfiguration muss hinter dem
Prefix /64 stehen, auch wenn eurer Prefix ein /48 Subnet hat! Auch hier
durch klick auf "Übernehmen" die Einstellung speichern. Abschließend
geht auf "Dienste" und startet nacheinander die Dienste "aiccu" und
"radvd".

.. _IPv6Sicherheit:

IPv6 Sicherheit
---------------

Um jetzt noch die Clients gegen Verbindungen von außen abzuschotten,
klicken wir im Freetzmenü auf Pakete→NHIPT, tragen bei "Admin IP" das
Subnetz eures LAN ein (beispielsweise 192.168.178.0/24) und setzt den
Status auf "running". Das ganze übernehmen und auf "Edit Firewall Rules"
klicken. Hier müsst ihr euch mit euren Freetzinterface Logindaten
(Standarduser: admin, Standardpasswort: freetz) anmelden.

Auf der folgenden Seite seht ihr dann die Konfigurationsseite für die
IPv6 Firewall ip6tables. Lasst euch nicht von den vielen Feldern
erschlagen und scrollt direkt zu den Feldern, über denen "RULES FOR
CHAIN INPUT [ filter ] [ IPv6 ]" steht. Tragt jetzt in die Felder
folgende Werte ein:

.. code:: bash

   "In IFC" = "sixxs"
   "Prot" = "ipv6"
   "Module" = "state"
   "Param" = "RELATED,ESTABLISHED"

und klickt auf "Insert". Das ganze wiederholt ihr dann noch (wieder in
den gleichen Feldern) mit den Werten

.. code:: bash

   "In IFC" = "sixxs"
   "Prot" = "ipv6-icmp"

.. code:: bash

   "In IFC" = "sixxs"
   "Action" = "DROP"

Zum Schluss auf "persist rules" klicken.

Jetzt ist euer Netzwerk auch unter IPv6 geschützt, wobei es trotzdem die
Pings durchlässt (für Credits).

Hinweis: Das Modul "state" bzw conntrack funktioniert mit zu altem
Kernel (7270 hat 2.6.19.2) für IPv6 nicht, kann also weggelassen werden.
Quelle: `​SixXS <http://www.sixxs.net/wiki/IPv6_Firewalling>`__

DNS trage ich nach, soweit ich mich damit mehr beschäftigt habe.

aiccu.sh
--------

Falls aktiviert, wird dieses Skript nach Verbindungsaufbau ausgeführt.
Es können z. B. ip6tables Regeln eingetragen werden.

.. _Links:

Links
-----

-  `​IPv6 <http://de.wikipedia.org/wiki/IPv6>`__
-  `​AICCU <http://en.wikipedia.org/wiki/AICCU>`__
-  `​radvd <http://en.wikipedia.org/wiki/Radvd>`__
-  `​SixXS <http://www.sixxs.net/>`__
-  `​Forum
   Post <http://www.ippf.eu/showpost.php?p=1488444&postcount=74>`__

--------------

.. _CommentbyoliveronSa12Jun201020:02:08CEST:

Comment by oliver on Sa 12 Jun 2010 20:02:08 CEST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Welche Kernel Version brauchen wir denn? 2.6.20 oder 2.6.21? Wenn
conntrack wichtig ist, dann könnten wir schauen, ob wir die Änderungen
backporten können.

.. _CommentbycumaonSa12Jun201020:55:43CEST:

Comment by cuma on Sa 12 Jun 2010 20:55:43 CEST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.6.20 reicht:
`​http://www.bieringer.de/linux/IPv6/status/IPv6+Linux-status-kernel.html <http://www.bieringer.de/linux/IPv6/status/IPv6+Linux-status-kernel.html>`__

.. _CommentbymikeonMo26Jul201020:34:33CEST:

Comment by mike on Mo 26 Jul 2010 20:34:33 CEST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Schaut euch bitte mal diese stateless Firewall Regeln für ipv6 mit sixxs
Tunnel auf der FritzBox an. Habe ich gerade aus Mangel am conntrack
Modul für meinen alten 2.6.19er Kernel auf der 7170 geschrieben. Über
Kommentare und Verbesserungsvorschläge freue ich mich. Ich weiß selbst
dass es nicht perfekt ist, aber besser so als gar keinen Schutz.

.. code:: bash

   # Flush rules
   ip6tables -F

   # Set the default policy
   ip6tables -P INPUT DROP
   ip6tables -P FORWARD DROP
   ip6tables -P OUTPUT ACCEPT

   # Allow anything on the local link
   ip6tables -A INPUT -i lo -j ACCEPT
   ip6tables -A OUTPUT -o lo -j ACCEPT

   # Allow Link-Local addresses
   ip6tables -A INPUT -s fe80::/10 -j ACCEPT

   # Allow multicast
   ip6tables -A INPUT -s ff00::/8 -j ACCEPT

   # Allow ICMP
   ip6tables -A INPUT -p icmpv6 -j ACCEPT

   # Allow INPUT   ports from 1-1024 to destination ports 1024-65535
   # Allow FORWARD ports from 1-1024 to destination ports 1024-65535
   # on the sixxs interface
   ip6tables -A INPUT -i sixxs -p tcp --sport 1:1024 --dport 1024:65535 -j ACCEPT
   ip6tables -A INPUT -i sixxs -p udp --sport 1:1024 --dport 1024:65535 -j ACCEPT
   ip6tables -A FORWARD -i sixxs -p tcp --sport 1:1024 --dport 1024:65535 -j ACCEPT
   ip6tables -A FORWARD -i sixxs -p udp --sport 1:1024 --dport 1024:65535 -j ACCEPT

   # Allow forwarding of everything coming from _OUR_
   # subnet. In this case: 2a01:aaa:bbb::/48
   # You have to replace this for your config!!!
   ip6tables -A FORWARD -s 2a01:aaa:bbb::/48 -j ACCEPT

AddComment?

-  Tags
-  `network </tags/network>`__
-  `packages <../packages.html>`__
