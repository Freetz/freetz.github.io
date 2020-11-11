.. _ImapProxy:

ImapProxy
=========

"*ImapProxy is a caching IMAP proxy server intended for use with WebMail
clients that cannot maintain persistent connections to an IMAP server.*"

.. _Setup:

Setup
-----

Just start it and point your IMAP (web) client to fritz.box:143.

If you want to use the proxy remote, you have to forward port 143 using
the `AVM-Firewall <avm-firewall.html>`__. Beware that if you don't
restrict the ip addresses everyone can use your proxy.

One of the features is that ImapProxy is patched to use Yahoo! IMAP.
This feature is automatically used if your email address contains lower
case "yahoo".

.. _Links:

Links
-----

-  `​ImapProxy homepage <http://imapproxy.org/>`__
-  `​Ticket with patch <http://trac.freetz.org/ticket/847>`__
-  `​IPPF
   thread <http://www.ip-phone-forum.de/showthread.php?t=216517>`__
-  `​Free IMAP and SMTPs
   access <http://en.wikipedia.org/wiki/Yahoo!_Mail#Free_IMAP_and_SMTPs_access>`__
   (wikipedia about Yahoo!)

-  Tags
-  `mail </tags/mail>`__
-  `network </tags/network>`__
-  `packages <../packages.html>`__
-  `proxy </tags/proxy>`__
