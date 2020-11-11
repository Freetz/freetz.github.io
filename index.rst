.. _WillkommenbeiFreetz:

Willkommen bei Freetz
=====================

| `Freetz <wiki/freetz.html>`__ ist eine Firmware-Erweiterung und
  Modifikation für `​Fritz!Box <http://www.avm.de>`__ Router und
  kompatible Geräte. Die Original-Firmware des Herstellers wird um
  zusätzliche Funktionen `erweitert <wiki/freetz.html>`__ und mit einer
  individuellen Zusammenstellung von Programmen ergänzt. Mehr zum Namen
  "Freetz" und zur Historie siehe
  `FAQ <wiki/FAQ.html#WoherkommtderNameFreetz>`__.
| Freetz ist `​freie
  Software <http://www.germany.fsfeurope.org/documents/freesoftware.de.html>`__
  und wird von Oliver Metz, Alexander Kriegisch und Team entwickelt.

|Warning| **WARNUNG:** Die Installation einer modifizierten Firmware führt
zum Verlust der Gewährleistung des Herstellers!

.. _Download:

Download
--------

Das letzte Release ist Version 2.0. Bitte folge den Anweisungen unter
`Quellcode <wiki/common/source_code.html>`__, um es zu downloaden.

Um den Trunk (Entwicklerversion) zu nutzen, einfach die Anleitung zum
`Auschecken und Aktualisieren des
Quellcodes <wiki/common/source_code.html>`__ aus dem Freetz-Repository
folgen.

Diese Versionen unterscheiden sich in der unterstützen AVM-Firmware
(Datei 'FIRMWARES') und den Erweiterungen durch Freetz (Datei
'CHANGELOG').

Eine komplette Liste aller Releases befindet sich auf der `Download
Seite <wiki/Download.html>`__.

.. _ErsteSchritte:

Erste Schritte
--------------

Diese Anleitung richtet sich in erster Linie an neue Benutzer, welche
sich erst mit Freetz vertraut machen wollen. Der Benutzer wird
schrittweise begleitet bis zur Erstellung und Flashen eines ersten
Firmware-Images.

-  `Erste Schritte mit Freetz <wiki/help/howtos/common/newbie.html>`__

.. _Installation:

Installation
------------

Für die Freetz-Installation wird Linux als Betriebssystem empfohlen. Wer
kein Linux dauerhaft auf seinem Rechner installieren will, kann sich mit
einem Linux-Live-System oder einem sog. Image für eine "virtuellen
Maschine" (VM) seiner Wahl behelfen.

-  `Voraussetzungen, notwendige Pakete und sonstige Informationen zur
   Freetz-Installation <wiki/help/howtos/common/install.html>`__

.. _HilfeundSupport:

Hilfe und Support
-----------------

-  `Wiki <wiki/freetz.html>`__:

   -  `Installation <wiki/help/howtos/common/install.html>`__
   -  `Pakete, Addons und CGI-Erweiterungen <wiki/packages.html>`__
   -  `Patches <wiki/patches.html>`__, `Aussehen <wiki/style.html>`__
   -  `Bibliotheken <wiki/libs.html>`__, Module, `FAQ <wiki/FAQ.html>`__
   -  `Kernel-Sources <wiki/kernel.html>`__
   -  Hintergrund-Infos
   -  `Howtos <wiki/help/howtos.html>`__, und `Hilfe <wiki/help.html>`__
   -  `Trouble-Shooting <wiki/help/trouble_shooting.html>`__

-  `​IP-Phone-Forum <http://www.ip-phone-forum.de/forumdisplay.php?f=525>`__

Hier findest du mehr zu `Hilfe und Support <wiki/help.html>`__.

.. _PresseundBerichte:

Presse und Berichte
-------------------

-  `Liste von Berichten über Freetz <wiki/Press.html>`__
-  `Ankündigung Entwicklertreffen Freetz-Conf
   2011 <wiki/FreetzConf2011.html>`__

.. _Machmit:

Mach mit!
---------

Interessierte Benutzer und potentielle Entwickler, die aktiv an der
Verbesserung von Freetz und deren Entwicklung mitwirken wollen, werden
durch das Trac-Systems hinreichend unterstützt. So können der komplette
Quellcode eingesehen, Änderungen verfolgt und über das Ticket-System
Fehler und Feature-Wünsche gemeldet werden. Ein aktuelles Wiki hilft
allen Beteiligten!

-  `Zeitachse </timeline>`__: Chronologie der Änderungen
-  `Roadmap </roadmap>`__: Stand und Planung der Entwicklung (in Arbeit)
-  `Quellcode-Browser </browser/>`__: SVN-Repository durchsuchen
-  `Ticket-System </report/>`__: Probleme, Fehler und neue
   Feature-Wünsche **(bitte**\ `hier <wiki/ticket.html>`__\ **nachlesen
   und evtl. im IP-Phone-Forum fragen, bevor ein Ticket eröffnet
   wird!)**
-  `Developer
   Information <wiki/help/howtos/development/developer_information.html>`__:
   Informationen für Entwickler und Howtos (englisch)
-  Interner Entwicklerbereich: Nur für Entwickler: Interner Bereich zur
   Abstimmung.

Das Bearbeiten des Wikis und Eröffnen von Tickets ist zur Vermeidung von
Spam nur nach vorheriger **Registrierung** möglich.

.. _Quellcode:

Quellcode
---------

Anleitung zum `Auschecken und Aktualisieren des
Quellcodes <wiki/common/source_code.html>`__ aus dem Freetz-Repository

.. toctree::
   :maxdepth: 1
   :caption: Generelles
   :name: sec-general

   wiki/packages_tagged
   wiki/Download
   wiki/freetz
   wiki/FAQ
   wiki/Impressum
   wiki/libs_tagged
   wiki/ticket
   wiki/style
   wiki/packages
   wiki/FreetzConf2011
   wiki/patch
   wiki/Press.en
   wiki/patches
   wiki/help
   wiki/libs
   wiki/costumscript_dublesyslog
   wiki/kernel
   wiki/Press
   wiki/freetz.en
   wiki/FAQ.en
   wiki/common/source_code.en
   wiki/common/source_code


.. toctree::
   :maxdepth: 1
   :caption: Patches
   :name: sec-patches

   wiki/patches/remove_myfritz
   wiki/patches/remove_tr069
   wiki/patches/remove_assistant
   wiki/patches/remove_help
   wiki/patches/remove_usermand
   wiki/patches/enum.en
   wiki/patches/remove_samba
   wiki/patches/signed
   wiki/patches/remove_upnp
   wiki/patches/usb_names
   wiki/patches/remove_mediasrv
   wiki/patches/remove_dsld
   wiki/patches/enum
   wiki/patches/onlinechanged
   wiki/patches/freetzmount
   wiki/patches/replace_onlinechanged
   wiki/patches/remove_capi
   wiki/patches/exec_autorun
   wiki/patches/maxdevcount
   wiki/patches/remove_minid
   wiki/patches/multpile_printers
   wiki/patches/alarmclock
   wiki/patches/freetzmount.en
   wiki/patches/remove_vpn
   wiki/patches/remove_support
   wiki/patches/remove_ftpd
   wiki/patches/remove_aura_usb
   wiki/patches/custom_udev_rules


.. toctree::
   :maxdepth: 1
   :caption: Hilfe
   :name: sec-help

   wiki/help/howtos
   wiki/help/trouble_shooting
   wiki/help/fritz_faq
   wiki/help/irc
   wiki/help/wikiedit
   wiki/help/howtos/common
   wiki/help/howtos/security
   wiki/help/howtos/troubleshoot
   wiki/help/howtos/development
   wiki/help/howtos/common/freetz_linux
   wiki/help/howtos/common/shutdown
   wiki/help/howtos/common/newbie.en
   wiki/help/howtos/common/first_trunk
   wiki/help/howtos/common/install.en
   wiki/help/howtos/common/external
   wiki/help/howtos/common/create_swap
   wiki/help/howtos/common/install
   wiki/help/howtos/common/newbie
   wiki/help/howtos/common/wol
   wiki/help/howtos/common/user
   wiki/help/howtos/common/busybox_httpd
   wiki/help/howtos/common/install/menuconfig
   wiki/help/howtos/common/newbie/other
   wiki/help/howtos/common/newbie/errors
   wiki/help/howtos/troubleshoot/repair_phonebook
   wiki/help/howtos/troubleshoot/recover_firmware
   wiki/help/howtos/troubleshoot/reboots
   wiki/help/howtos/security/switch_config
   wiki/help/howtos/security/router_and_firewall
   wiki/help/howtos/security/user_management
   wiki/help/howtos/security/split_wlan_lan
   wiki/help/howtos/development/sign_image
   wiki/help/howtos/development/integrate_patches
   wiki/help/howtos/development/bandwidth_svg
   wiki/help/howtos/development/create_cross-compiler_toolchain
   wiki/help/howtos/development/release_management
   wiki/help/howtos/development/package_creation
   wiki/help/howtos/development/save_mtd_2
   wiki/help/howtos/development/developer_information
   wiki/help/howtos/development/create_gui
   wiki/help/howtos/development/manipulation_detection
   wiki/help/howtos/development/freetz_make
   wiki/help/howtos/development/urlader_flags
   wiki/help/howtos/development/flash
   wiki/help/howtos/development/firmware_update_details
   wiki/help/howtos/development/repack_fw
   wiki/help/howtos/development/install_addon
   wiki/help/howtos/development/make_busybox
   wiki/help/howtos/development/adam2
   wiki/help/howtos/development/save_mtd_1
   wiki/help/howtos/development/integrate_own_files
   wiki/help/howtos/development/analyse_image_names
   wiki/help/howtos/development/menuconfig
   wiki/help/howtos/development/compile_own_progs
   wiki/help/howtos/development/make_kernel
   wiki/help/howtos/development/make_room
   wiki/help/howtos/development/developer_information/package_development
   wiki/help/howtos/development/developer_information/post_commit_hook
   wiki/help/howtos/development/developer_information/shell_coding_conventions
   wiki/help/howtos/development/developer_information/package_development_advanced
   wiki/help/howtos/development/developer_information/package_development_dynamic
   wiki/help/howtos/development/developer_information/package_development_start
   wiki/help/howtos/development/developer_information/package_development_start/example_2
   wiki/help/howtos/development/developer_information/package_development_start/example_1
   wiki/help/howtos/development/developer_information/package_development_start/.language
   wiki/help/howtos/development/developer_information/package_development_start/webinterface_example_1
   wiki/help/howtos/development/developer_information/package_development_start/example_3
   wiki/help/howtos/development/developer_information/webif/libmodcgi
   wiki/help/wikiedit/screenshots
   wiki/help/wikiedit/toc
   wiki/help/wikiedit/tagging
   wiki/help/wikiedit/tables
   wiki/help/wikiedit/formatting_guide
   wiki/help/wikiedit/goodies
   wiki/style/tagging
   wiki/style/skins
   wiki/style/favicons
   wiki/style/mounted
   wiki/libs/ftdi
   wiki/libs/ftdi.en


.. toctree::
   :maxdepth: 1
   :caption: Pakete
   :name: sec-packages

   wiki/packages/bridge-utils
   wiki/packages/sispmctl
   wiki/packages/empty
   wiki/packages/apache
   wiki/packages/polipo.en
   wiki/packages/autofs
   wiki/packages/strace
   wiki/packages/syslogd
   wiki/packages/lsof
   wiki/packages/dns2tcp
   wiki/packages/tinyproxy
   wiki/packages/davfs2
   wiki/packages/s3fslite
   wiki/packages/dropbear.en
   wiki/packages/ctorrent
   wiki/packages/irssi
   wiki/packages/hplip
   wiki/packages/lighttpd
   wiki/packages/privoxy
   wiki/packages/radvd.en
   wiki/packages/usbroot
   wiki/packages/vim
   wiki/packages/bluez-utils
   wiki/packages/sane-backends
   wiki/packages/usbip
   wiki/packages/dropbear
   wiki/packages/iptables-cgi
   wiki/packages/hd-idle
   wiki/packages/fhem
   wiki/packages/igmpproxy
   wiki/packages/usbutils
   wiki/packages/inotify-tools
   wiki/packages/authorized-keys.en
   wiki/packages/rrdstats
   wiki/packages/mcabber
   wiki/packages/dtmfbox
   wiki/packages/nfsd.en
   wiki/packages/espeak
   wiki/packages/dnsd
   wiki/packages/tor
   wiki/packages/spindown
   wiki/packages/ncftp
   wiki/packages/lynx
   wiki/packages/smstools3
   wiki/packages/debootstrap
   wiki/packages/ppp
   wiki/packages/xmail
   wiki/packages/sundtek
   wiki/packages/iptables
   wiki/packages/subversion
   wiki/packages/dtach
   wiki/packages/vsftpd
   wiki/packages/ziproxy
   wiki/packages/ntfs-3g
   wiki/packages/ruby
   wiki/packages/aiccu
   wiki/packages/mc
   wiki/packages/nfs
   wiki/packages/streamripper
   wiki/packages/htpdate
   wiki/packages/lua
   wiki/packages/emailrelay
   wiki/packages/madplay
   wiki/packages/nhipt
   wiki/packages/wput
   wiki/packages/netsnmp
   wiki/packages/transmission.en
   wiki/packages/imapproxy.en
   wiki/packages/fuse
   wiki/packages/hiawatha
   wiki/packages/cifsmount
   wiki/packages/matrixtunnel
   wiki/packages/ndas.en
   wiki/packages/nfs-utils
   wiki/packages/vpnc
   wiki/packages/haserl
   wiki/packages/obexftp
   wiki/packages/nmap
   wiki/packages/httptunnel
   wiki/packages/onlinechanged
   wiki/packages/mini_fo
   wiki/packages/pingtunnel
   wiki/packages/tcp_wrappers
   wiki/packages/netsnmp.en
   wiki/packages/wol
   wiki/packages/cpmaccfg
   wiki/packages/syslogd.en
   wiki/packages/checkmaild
   wiki/packages/portmap
   wiki/packages/digitemp
   wiki/packages/downloader
   wiki/packages/bip
   wiki/packages/fortune
   wiki/packages/xrelayd
   wiki/packages/tinc
   wiki/packages/bird
   wiki/packages/onlinechanged_cgi
   wiki/packages/php
   wiki/packages/pptp
   wiki/packages/mediatomb
   wiki/packages/inetd
   wiki/packages/owfs
   wiki/packages/unbound
   wiki/packages/fstyp
   wiki/packages/prosody.en
   wiki/packages/bftpd
   wiki/packages/mod
   wiki/packages/br2684ctl.en
   wiki/packages/deco
   wiki/packages/trickle
   wiki/packages/radvd
   wiki/packages/opendd
   wiki/packages/pptpd
   wiki/packages/mediaserver
   wiki/packages/iptables.en
   wiki/packages/dnsd.en
   wiki/packages/hp-utils
   wiki/packages/screen
   wiki/packages/ndas
   wiki/packages/dnsmasq
   wiki/packages/wget
   wiki/packages/e2fsprogs
   wiki/packages/bind
   wiki/packages/tcpdump
   wiki/packages/gw6
   wiki/packages/nhipt.en
   wiki/packages/openntpd
   wiki/packages/rudi-shell
   wiki/packages/nano
   wiki/packages/nfsd
   wiki/packages/stunnel
   wiki/packages/rrdtool
   wiki/packages/ldd
   wiki/packages/prosody
   wiki/packages/fhzctrl
   wiki/packages/aiccu.en
   wiki/packages/authorized-keys
   wiki/packages/pciutils
   wiki/packages/vtund
   wiki/packages/fritzload
   wiki/packages/jamvm
   wiki/packages/callmonitor
   wiki/packages/br2684ctl
   wiki/packages/netcat
   wiki/packages/quagga
   wiki/packages/samba
   wiki/packages/iodine
   wiki/packages/nagios
   wiki/packages/smartmontools
   wiki/packages/mtr
   wiki/packages/avm-firewall
   wiki/packages/bash
   wiki/packages/asterisk
   wiki/packages/microperl
   wiki/packages/nano-shell
   wiki/packages/m-i-t
   wiki/packages/minidlna
   wiki/packages/inadyn-mt
   wiki/packages/bluez
   wiki/packages/DemoPackageA
   wiki/packages/openvpn
   wiki/packages/knock
   wiki/packages/ltrace
   wiki/packages/curl
   wiki/packages/inadyn-mt.en
   wiki/packages/virtualip
   wiki/packages/socat
   wiki/packages/transmission
   wiki/packages/netsnmp/mrtg.en

.. |Warning| image:: /chrome/wikiextras-icons-16/exclamation.png
