iptables
========

.. _Wasistiptablesundwerbrauchtesüberhaupt:

Was ist iptables und wer braucht es überhaupt?
----------------------------------------------

| **iptables** ist ein Kommandozeilen User Interface zur Konfiguration /
  Verwaltung der im jeweiligen Linux Kernel eingebauten sehr mächtigen
  `​netfilter <http://de.wikipedia.org/wiki/Netfilter/iptables>`__ -
  Firewall Funktionen.

| Zielgruppe sind Anwender, die die volle Kontrolle über ihren Netzwerk
  Verkehr erlangen wollen und sich so effektiv vor Attacken und
  unliebsamem Ausspähen schützen möchten.

Der Linux Paketfilter iptables / netfilter schützt bei richtiger
Konfiguration gegen viele Bedrohungen aus dem Netz. Er kann intelligent
Daten Pakete prüfen, verwerfen, abweisen, weiterleiten, priorisieren
oder manipulieren und schützt so vor den meisten bekannten DoS Atacken,
Portscans und unerlaubten Zugriffen. Gezielt eingesetzt kann er z.B.
auch das lästige "nach Hause telefonieren" von vielen Anwendungen
unterbinden. Mit Hilfe von iptables kann der kundige Anwender aus seiner
FritzBox eine leistungsfähige Firewall machen, die den Vergleich mit
teuren professionellen Lösungen nicht scheuen muss.

Da die Basis für iptables / netfilter im Linux Kernel steckt, ergibt
sich für Freetz und die FritzBox folgende Problematik: die aktuelle 7270
hat unter Anderem einen neueren Kernel als die älteren Boxen der 7170er
Generation, was Auswirkungen auf iptables hat.

-  die älteren Modelle (vor der 7270) hatten auf Grund des alten Kernels
   und der beschränkten HW Probleme mit conntrack (Überläufe der
   Tracking - Tabellen und daraus resultierende Reboots der Box)
-  Für die 7270 gibt es noch kein Web-Interface (kein firewall-cgi)
-  Die 7270 hat mehr Arbeitsspeicher und einen neueren Kernel, und damit
   keine Probleme mehr mit mit conntrack (connection tracking Modul,
   benötigt um stateful Firewall Regeln z.B. für ftp, VoIP etc. zu
   erstellen).
-  Die Syntax der iptables Anweisungen / Fähigkeiten von iptables auf
   der 7270 und 71xx können von einander abweichen.
-  Welcher Befehl mit welcher Syntax im Endeffekt akzeptiert wird hängt
   von den **geladenen** Modulen ab, werden Module "vergessen", bekommt
   man nur zum Teil aussagefähige Fehlermeldungen.

.. _WasistderUnterschiedzurAVMFirewallwievertragensichbeide:

Was ist der Unterschied zur AVM Firewall, wie vertragen sich beide?
-------------------------------------------------------------------

-  Die `AVM Firewall <avm-firewall.html>`__ ist Bestandteil des **dsld**
   von AVM (der dsl deamon). Sie "sitzt" sozusagen auf dem DSL Modem und
   kümmert sich ausschließlich um den Verkehr, der durch dieses
   Interface fließt. Intern kann sie connection tracking, port
   forwarding, traffic shaping und filtern von Paketen. Nach dem
   Firewall-Modul landen die Pakete auf die FritzBox und gehen ohne
   weitere Kontrolle an alle internen Interfaces, sowie Dienste der Box.
   Die Default- IN/OUT Regeln der AVM Firewall sind "PERMIT": also
   alles, was nicht verboten wird, wird durchgelassen. Verboten wird
   lediglich NetBIOS Verkehr und ein Port, welches ein bekannter Virus
   mal missbraucht hat. Jeder abgehende Verkehr von Box & Netzwerk ist
   erlaubt. Ungebetener ankommender Verkehr ins LAN scheitert nur am
   NAT, die Box selbst ist weitestgehend ungeschützt (dsld als einzige
   Hürde). Mit geeigneten Regeln und dem AVM Firewall Paket in Freetz
   kann diese Firewall für den Internet Verkehr weiter eingeschränkt
   werden. Das Modul ist closed source, was es genau macht, weiss nur
   AVM, es gibt keine LOG Möglichkeit. Die Box ist offen für diverse
   Multimedia Ports, sowie Fernwartung über TR069.

-  Die iptables Firewall kontrolliert den gesamten Netzwerkverkehr auf
   unterster Betriebssystem Ebene. Jedes Interface wird überwacht und
   jedes Paket, dass zur Box, von der Box weg oder durch die Box von
   einem zum anderen Interface will, kommt an iptables nicht vorbei.
   Diese Firewall ist der ultimative Schutz für die Box vor Angriffen
   von außen **und** innen. Mit ihr lassen sich sinnvoll z.B. DMZ
   Segmente und Sicherheitszonen realisieren. Sie bietet auch die
   Möglichkeit DoS Attacken und Portscans wirksam zu bekämpfen. Auch
   Deep Inspections von Paketen sind möglich. Darüber hinaus lassen sich
   virtuelle Hosts realisieren, und source oder destination NAT
   Scenarien umsetzen. Mit iptables lassen sich natürlich auch Regeln
   für VPN - Tunnel Interfaces und virtuelle Interfaces definieren. Mit
   anderen Worten iptables ist viel mächtiger und leistungsfähiger,
   ausserdem ist es Open Source und es kann den Verkehr loggen.

-  Beide Firewalls wirken auf völlig unterschiedliche Bereiche und
   operieren unabhängig voneinander. Auch ihre Konfiguration ist
   unabhängig, bis auf die Tatsache, dass **beide nacheinander** auf den
   Internet Verkehr Anwendung finden. Das bedeutet, dass *Freigaben* der
   einen nicht die *Sperren* der anderen umgehen können. Folgende Bilder
   sollen den Fluss veranschaulichen:

..

      | Verkehr von und zur FritzBox:
      | **DSL < — > AVM Firewall (NAT) < — > iptables Firewall < — >
        (FritzBox) < — > iptables Firewall < — > LAN / WLAN**

      | Verkehr zwischen Internet und LAN Interfaces:
      | **DSL < — > AVM Firewall (NAT) < — > iptables Firewall < — > LAN
        / WLAN**

..

      | Verkehr in einer DMZ oder VPN Tunnel zum LAN/WLAN :
      | **DMZ / Tunnel Interfaces < — > iptables Firewall < — > LAN /
        WLAN**

-  da die AVM Firewall (**dsld**) ja auch für die DSL Protokolle
   verantwortlich ist, kann man in der Betriebsart **DSL Router** ohne
   Ersatz nicht darauf verzichten.
-  Man kann **problemlos beide gleichzeitig** betreiben, die Regeln
   sollten entsprechend bei **beiden** für die gewünschten Protokolle
   durchlässig sein.
-  Da sie kaskadiert sind, bieten sie in Kombination einen zusätzlichen
   wirksamen Schutz vor Hacker und Ausspäher, selbst wenn die AVM
   Firewall durch eine Hintertür (z.B. mit TR069 Um-Konfiguration der
   AVM Firewall durch Provider) ausgehebelt wird, bleiben alle Systeme
   (FritzBox + Geräte im LAN / WLAN) sicher vor unliebsamen Gästen
   geschützt.
-  die sicherste, optimale Konfiguration ist, wenn beide Firewalls
   vollständig konfiguriert werden, so dass jede für sich den vollen
   Schutz des Systems garantieren kann und nur gewünschten Verkehr
   zulässt.

.. _Wiebautmaniptables:

Wie baut man iptables?
----------------------

-  iptables und alle gewünschten Module müssen mit `make
   menuconfig <../help/howtos/common/install/menuconfig.html>`__ beim
   Bauen der Firmware ausgewählt werden (unter packages→unstable, die
   Option ist nur sichtbar wenn "Show Advanced Options" aktiviert ist)
-  wenn benötigte Module nicht angeboten werden (z.B. ULOG Ziel etc.),
   kann man diese mit `replace
   kernel <../help/howtos/development/make_kernel.html>`__ / **make
   kernelconfig** im Kernel hinzufügen und durch geeignete Patches
   dazubauen (Nur für erfahrene Entwickler!)
-  Die Verfügbarkeit der einzelnen Module hängt von den Fähigkeiten der
   jeweiligen Kernel Version ab.

.. _Konfiguration:Firmwareerfolgreicherstelltundaufgespieltsogehtesweiter:

Konfiguration: Firmware erfolgreich erstellt und aufgespielt, so geht es weiter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  zunächst mal empfiehlt es sich interaktiv die Regeln zu erstellen und
   zu testen
-  bevor man damit beginnen kann, müssen die für die jeweiligen Regeln
   benötigten Module in das System geladen werden.

| Hier ein Beispiel - Script für das Laden der Module:

.. code:: bash

   # Die wichtigsten Module, ohne die nichts geht:
   modprobe ip_tables
   modprobe iptable_filter
   modprobe x_tables
   modprobe xt_tcpudp

   # Alternative Ziele LOG und REJECT:
   modprobe ipt_LOG
   modprobe ipt_REJECT

   # Bei Verwendung von IP Adressbereichen:
   modprobe ipt_iprange

   # Bei Verwendung von Port Bereichen
   modprobe xt_multiport

   # Fuer stateful firewall Regeln (conntrack):
   modprobe xt_state
   modprobe xt_conntrack
   modprobe ip_conntrack
   modprobe ip_conntrack_ftp
   modprobe ip_conntrack_tftp

-  Danach werden die Regeln / Ketten erstellt (hier ein Beispiel für
   diverse Regeln):

.. code:: bash

   # # # FIREWALL RULES

   iptables -N TRANS
   # Ausgehende Regeln für Internet Surfen:
   iptables -A TRANS -p tcp  -s 192.168.0.0/24 -m multiport --dport 20,21,22,25,80,110,443,465,995,5060 -j ACCEPT
   iptables -A TRANS -p udp  -s 192.168.0.0/24 -m multiport --dport 53,67,68,80,123,5060 -j ACCEPT
   iptables -A TRANS -p icmp -s 192.168.0.0/24 -j ACCEPT

   # conntrack für eingehende Antwortpakete:
   iptables -A TRANS -m state --state RELATED,ESTABLISHED -j ACCEPT

   # ... Eigene Regeln für bekannte hosts
   # ...

   iptables -A TRANS -j LOG --log-prefix "[IPT] DENY-LAN-ACCESS "          # abgewiesene Pakete Loggen
   iptables -A TRANS -j DROP                                               # PARANOIA LINK

   # # # Rules for Fritz Device

   iptables -A INPUT -p udp -s 0.0.0.0 -d 255.255.255.255 --sport 68 --dport 67 -j ACCEPT
   iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT                 # LOCALHOST
   iptables -A INPUT -s 192.168.0.0/24 -j ACCEPT                         # LAN
   iptables -A INPUT -s 169.254.0.0/16 -i lan -j ACCEPT                  # EMERGENCY LAN
   iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
   iptables -A INPUT -p tcp --dport 5060 -j ACCEPT                       # VoIP
   iptables -A INPUT -p udp --dport 5060 -j ACCEPT                       # VoIP
   iptables -A INPUT -j LOG --log-prefix "[IPT] DENY-FRITZ-ACCESS "      # Log other traffic
   iptables -A INPUT -j DROP                                             # PARANOIA IN
   iptables -P INPUT DROP                                                # Default policy DROP

   iptables -A OUTPUT -d 192.168.0.0/24 -j ACCEPT                        # Allow LAN
   iptables -A OUTPUT -d 224.0.0.1/24 -j ACCEPT                          # UPnP
   iptables -A OUTPUT -d 239.255.255.250 -j ACCEPT
   iptables -A OUTPUT -d 127.0.0.1 -j ACCEPT                             # Local Host
   iptables -A OUTPUT -p udp -m multiport --dport 53,123,5060 -j ACCEPT  # DNS, TIME, VoIP
   iptables -A OUTPUT -p tcp --dport 5060 -j ACCEPT                      # VoIP
   iptables -A OUTPUT -p tcp --dport 80 -d 63.208.196.0/24 -j ACCEPT     # DynDNS
   iptables -A OUTPUT -d myMailServer.com -j ACCEPT                      # e-Mail OUT
   iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT     # stateful conntrack
   iptables -A OUTPUT -d 212.42.244.73 -p tcp --dport 80 -j ACCEPT       # Plugins Server AVM

   # iptables -A OUTPUT -d www.dasoertliche.de    -p tcp --dport 80 -j ACCEPT # Für Telefonbuch Abfrage durch die Box
   # iptables -A OUTPUT -d www.dastelefonbuch.de  -p tcp --dport 80 -j ACCEPT
   # iptables -A OUTPUT -d www.goyellow.de        -p tcp --dport 80 -j ACCEPT
   # iptables -A OUTPUT -d www.11880.com          -p tcp --dport 80 -j ACCEPT
   # iptables -A OUTPUT -d www.google.de          -p tcp --dport 80 -j ACCEPT
   # iptables -A OUTPUT -d www.das-telefonbuch.at -p tcp --dport 80 -j ACCEPT
   # iptables -A OUTPUT -d www.search.ch          -p tcp --dport 80 -j ACCEPT
   # iptables -A OUTPUT -d www.anywho.com         -p tcp --dport 80 -j ACCEPT

   iptables -A OUTPUT -j LOG --log-prefix "[IPT] WARNING-CALL-HOME "      # Nicht Erlaubten ausgehenden Traffic Loggen
   iptables -P OUTPUT DROP                                                # und Sperren

   # # # Rules for FORWARD

   iptables -P FORWARD DROP
   iptables -A FORWARD -j TRANS                                           # Regeln für LAN - WAN Verkehr
   iptables -A FORWARD -j LOG --log-prefix "[IPT] DENY-FWD-ACCESS "

-  Im Gegensatz zur AVM-Firewall werden iptables Regeln sofort wirksam,
   bei Regeländerungen in der AVM Firewall ist ein Restart vom dsld
   nötig.
-  Wenn man alle gewünschten Regeln definiert und getestet hat, kann man
   sie als Batch in die **/var/flash/debug.cfg** schreiben beim Start
   der Box automatisch aktivieren.
-  Zunächst alle benötigten Module mit **modprobe** laden
-  danach die **iptables** Anweisungen in der richtigen Reihenfolge
   eintragen. (Die Ketten werden immer von oben nach unten abgearbeitet!
   )
-  im Kernel Log / auf Konsole1 sieht man alle LOG Einträge der Pakete,
   die die entsprechenden LOG Anweisungen passieren.
-  Und
   `​hier <http://www.chiark.greenend.org.uk/~peterb/network/drop-vs-reject>`__
   noch ein lesenswerter Artikel, der sich mit den Vor- bzw. Nachteilen
   von REJECT bzw. DROP beschäftigt.

.. _AnmerkungzuKernelLogs:

Anmerkung zu Kernel Logs
~~~~~~~~~~~~~~~~~~~~~~~~

AVM hat Änderungen im System eingebaut, die das Protokollieren von
Kernel Meldungen im Syslog verhindern. Um die LOG Einträge im Syslog zu
schreiben kann man mit :

   **echo STD_PRINTK > /dev/debug**

den AVM_PRINTK (und damit DECT) temporär abschalten. Mit der Anweisung:

   **echo AVM_PRINTK > /dev/debug**

wird der ursprüngliche Zustand wiederhergestellt und DECT funktioniert
wieder; die LOG Einträge werden wieder nur noch auf Konsole1 ausgegeben.

You can also try a patch from `this ticket </ticket/254>`__, but first
read the comments carefully.

.. _WasistderUnterschiedvonINPUTOUTPUTundFORWARD:

Was ist der Unterschied von INPUT, OUTPUT und FORWARD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  INPUT Kette filtert nur den eingehenden Verkehr zum localhost
   (FritzBox), damit werden Dienste die die FritzBox bereitstellt
   freigeschaltet.
-  OUTPUT Kette filtert nur den Verkehr, der von der FritzBox
   (localhost) in andere Netze geht, also Dienste, die die FritzBox
   benötigt.
-  FORWARD Kette filtert den Verkehr zwischen den Interfaces, also z.B.
   Internet < — > LAN / WLAN, also Dienste, die die Box "durchschleust".
-  conntrack Regeln dienen dem Daten-Rückfluss und sind deshalb immer im
   komplementären Zweig der Regel angesiedelt für INPUT Regel im OUTPUT
   Zweig etc.)

.. _HinweisezumCodeBeispiel:

Hinweise zum Code Beispiel
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Die erste / oberste Regel der INPUT / OUTPUT Ketten sollte immer ein
   ausreichendes ACCEPT für den Admin Zugang beinhalten, damit man sich
   nicht aus Versehen selbst aussperrt.
-  Die default Policy sollte erst dann auf DENY gestellt werden, wenn
   man alles erfolgreich getestet hat, man kann auch darauf verzichten
   wenn man als letzte Regel der jeweiligen Kette eine DENY oder REJECT
   Regel für alle Pakete formuliert.
-  im Beispiel wurde auch eine eigene Kette TRANS definiert und im
   FORWARD Zweig eingehängt, um die Fähigkeiten zu demonstrieren.
-  Das Beispiel beinhaltet keine Regeln für VoIP / Portforwarding etc.
   Es ist ein auf der 7270 getesteter minimaler Satz für die
   Basis-Internet Funktionalität und kann natürlich beliebig erweitert
   werden.
-  Es sind keine NAT Regeln enthalten, da der **dsld** (AVM-Firewall &
   DSL Interface) im System belassen wurde und diese Aufgabe bestens
   vorher erfüllt.
-  Es wurden nur die Module beschrieben / geladen, die für das Beispiel
   relevant sind, bei Bedarf können weitere Module per *modprobe*
   geladen werden.
-  Das Beispiel ist sehr restriktiv, was den Verkehr der FritzBox ins
   Internet betrifft; es verbietet alles, was nicht explizit per Regel
   erlaubt wird.
-  Das Beispiel zeigt einen sehr kleinen Teil der Fähigkeiten von
   iptables, wer mehr will findet im `​Linux-Kompendium: Linux-Firewall
   mit
   IP-Tables <http://de.wikibooks.org/wiki/Linux-Kompendium:_Linux-Firewall_mit_IP-Tables>`__
   jede Menge nützliches Wissen vermittelt.

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

-  `iptables-cgi <iptables-cgi.html>`__ - Eine Weboberfläche für
   iptables (freetz paket)
-  `NHIPT - iptables CGI <nhipt.html>`__ - Weboberfläche für iptables
   (unterstützt IPv4 & IPv6; Als freetz Paket oder direkt von USB
   nutzbar)
-  `cpmaccfg <../help/howtos/security/switch_config.html>`__ - Trennen
   der LAN Interface Bridge und Konfiguration einer DMZ
-  `OpenVPN <openvpn.html>`__ - VPN Tunnel mit der FritzBox
-  `AVM Firewall <avm-firewall.html>`__ - Der kleine Bruder von iptables
-  `Freetz als interner Router mit
   Firewall <../help/howtos/security/router_and_firewall.html>`__
-  `WLAN und LAN trennen mit
   iptables <../help/howtos/security/split_wlan_lan.html>`__
-  Die Suchfunktion im `​Freetz -
   Forum <http://www.ip-phone-forum.de/forumdisplay.php?f=525>`__ bietet
   auch weitere Hilfe zu speziellen Fragen

— cando

.. _ÄltereBeiträgebetreffenFritzBoxenvorder72xxSerie:

Ältere Beiträge (betreffen FritzBoxen vor der 72xx Serie)
=========================================================

Damit man **iptables** verwenden kann, müssen die entsprechenden
Kernel-Module in Freetz einkompiliert sein. Bei der Auswahl der Module
aus der Unzahl der Möglichkeiten kann hilfreich sein, firewall-cgi? zu
aktivieren, auch wenn es dann nicht benutzt wird. Die wichtigsten
iptables-Module werden dann automatisch einkompiliert.

.. code:: bash

   host# scp ../ds-0.2.5/kernel/root/usr/lib/iptables/libipt_limit.so root@fritz:/mod/lib
   fritz# iptables -m limit -h
   host# scp
   ../ds-0.2.5/kernel/modules-4mb/lib/modules/2.4.17_mvl21-malta-mips_fp_le/kernel/net/ipv4/netfilter/iptable_nat.o root@fritz:/mod/lib
   fritz# insmod insmod  /mod/lib/iptable_nat.o

Siehe auch Howto: `WLAN und LAN trennen mit
iptables <../help/howtos/security/split_wlan_lan.html>`__

.. _KnownBugFritzBoxvor7270:

Known Bug (FritzBox vor 7270)
-----------------------------

|Warning| Nach Laden des Conntack-Moduls weist der Kernel immer wieder
Pakete mit ``...ip_conntrack_tcp: INVALID: invalid TCP flag combinat``
o.ä. ab. Das ist ja gut so. Aber warum kommen die nicht an den
iptables-Chains vorbei? Das scheint vorher zu passieren.

danisahne schreibt dazu:

   Das ist schon mehreren aufgefallen. Ich habe keine Ahnung (hab mich
   noch nicht genauer damit beschäftigt, warum diese Pakete als INVALID
   erkannt werden. Tatsache ist, dass deswegen das forewall-cgi Paket
   nicht zusammen mit der Telefonie funktioniert. Ist quasi noch ein
   offener Bug.

..

   UPDATE: Das Problem sollte ab Version 0.2.7 gelöst sein.
   Verbindungen, die vor dem Laden des iptables conntrack Moduls
   aufgebaut wurden, werden dann als INVALID erkannt. Der Workaround in
   0.2.7 läd diese Module im Skript modload, falls sie mitinstalliert
   wurden. — danisahne

|Warning| ds26: Die Module werden nicht automatisch geladen. Mit geladenem
ip_conntrack stürzt meine Box nach ca. 3h ab. Ich hab den dsld im
Verdacht. Aber hier müsste mal jemand weiterforschen… — olistudent

|Warning| Ich habe festgestellt, dass es sich erheblich bessert, wenn man
folgendes macht:

.. code:: bash

   # 32MB RAM
   CONNTRACK_MAX=2048
   # CONNTRACK_MAX/8
   CONNTRACK_HASH=256

   modprobe ip_tables
   modprobe ip_conntrack hashsize=$CONNTRACK_HASH
   modprobe ipt_state
   modprobe iptable_filter
   modprobe iptable_nat
   echo $CONNTRACK_MAX > /proc/sys/net/ipv4/netfilter/ip_conntrack_max

Hier führten diese Einstellungen zu Uptimes von ~ 2 Tagen statt
mindestens 5x Reboot am Tag (W900V) (`Ticket 260 </ticket/260>`__)

   — crissi

-  Tags
-  `firewall </tags/firewall>`__
-  `network </tags/network>`__
-  `packages <../packages.html>`__
-  `routing </tags/routing>`__
-  `security </tags/security>`__
-  `überarbeiten </tags/%C3%BCberarbeiten>`__

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

