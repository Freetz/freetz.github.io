.. _ProsodyIM:

Prosody IM
==========

"*Prosody is a flexible communications server for Jabber/XMPP written in
Lua. It aims to be easy to use, and light on resources. For developers
it aims to be easy to extend and give a flexible system on which to
rapidly develop added functionality, or prototype new protocols.*"

**This package is a work in progress!**

.. _Configuration:

Configuration
-------------

-  Forward TCP ports 5222 (client-to-server) and 5269 (server-to-server)
   using the `AVM-Firewall <avm-firewall.html>`__ package
-  Define a virtual host for your (sub)domain

   -  The (sub)domain should point to your FritzBox

-  Creating users:

   -  Check *Allow registration* (temporarily) to create your account(s)
      from a XMPP client
   -  Or use *prosodyctl adduser [user]@[domain]*

-  Generate and configure a private key and belonging server certificate
   (free at `​cacert.org <http://www.cacert.org/>`__)

.. _Links:

Links
-----

-  `​Prosody IM homepage <http://prosody.im/>`__
-  `​Ticket with patches <http://trac.freetz.org/ticket/858>`__
-  `​Lua homepage <http://www.lua.org/>`__
-  `Lua package <lua.html>`__
-  `​Wikipedia:
   XMPP <http://en.wikipedia.org/wiki/Extensible_Messaging_and_Presence_Protocol>`__
   (Jabber)
-  `​OpenWrt thread <http://open-wrt.ru/forum/viewtopic.php?id=21643>`__
