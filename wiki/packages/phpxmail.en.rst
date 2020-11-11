.. _Introduction:

Introduction
============

The mail to/from my hosting provider got interrupted now and then and
the support wasn't that good. Setting up a mail server using Freetz and
PHPXMail was very simple. Now I can select my own blocklists and see in
the logs what is (not) happening.

.. _Basicsetupguide:

Basic setup guide
=================

#. To prevent disappointment: check if your internet provider allows
   SMTP (port 25) traffic
#. Build and install Freetz with PHPXMail and
   `AVM-firewall-cgi <avm-firewall.html>`__

   #. PHPXMail selects XMail and PHP
   #. Be prepared for the space requirements …

#. Setup Firewall (Freetz menu Packages > AVM-Firewall)

   #. Select port forwarding
   #. Forward TCP port 25 to Fritz!Box port 10025 (SMTP)
   #. Forward TCP port 110 to Fritz!Box port 10110 (POP3)
   #. Apply settings
   #. Reboot

#. Setup XMail (Freetz menu Packages > XMail)

   #. Set start type to automatic
   #. Fill in a **existing** directory for settings & storage, for
      example

      .. code:: bash

         /var/media/ftp/uStor01/XMail

#. Activate SMTP & POP3
#. Activate unencrypted admin access
#. Activate all logging for the time being
#. Apply
#. Start XMail (freetz menu Services > XMail > Start)
#. Change the user name of the web interface to set XMail password
   (Freetz menu Settings > webcfg > change password)
#. Open PHPXMail configuration site (Freetz menu Packages > PHPXMail >
   here)

   #. Login with user *admin* and the set web interface password
   #. Goto server config

      #. Enable *DefaultSMTPGateways*
      #. Fill in your provider's smtp server address
      #. Save values
      #. Read
         `​this <http://www.xmailserver.org/Readme.html#smtp_client_authentication>`__
         if you need to authenticate

   #. Goto server domains > new domain
   #. Enter your domain name, for example *your-domain.com*
   #. Submit
   #. Goto server config

      #. Enable and set *CustMapsList* to (see
         `​here <http://xmailforum.homelinux.net/index.php?showtopic=4620>`__):

         .. code:: bash

            zen.spamhaus.org.:0

#. Create an MX record that points to the external IP of your FritzBox

   #. See for example
      `​here <http://www.dyndns.com/support/kb/email_mail_exchangers_and_dns.html>`__
      for information
   #. Use `​DynDNS <http://www.dyndns.com/>`__ or similar if you have a
      dynamic IP address
   #. I created an MX record with a higher priority than the existing
      records, so in case of problems mail will be handled by my hosting
      provider as usual

#. Setup your preferred e-mail client

   #. Server: external IP of your FritzBox
   #. User name: *postmaster @ your-domain.com*

#. Test your configuration

   #. Send a test mail to *postmaster @ your-domain.com* (check server
      logs > smtp)
   #. Receive the test mail with your e-mail client (check server logs >
      pop3)
   #. Check for open mail relaying for example
      `​here <http://www.abuse.net/relay.html>`__

#. Setup as many other domains and accounts as you like …

If you want to forward e-mail:

#. Goto the domain user you want to forward mail for
#. Select the link user mail proc
#. Enter redirect|<forwarding e-mail address>
#. Submit

It is not a bad idea to backup your XMail settings and storage
directory!

.. _SetupSSL:

Setup SSL
=========

#. Build XMail with SSL support
#. Login using telnet (or better SSH)
#. Goto the XMail settings directory
#. Create the file *openssl.cnf* with the example contents from
   `​here <http://www.iona.com/support/docs/orbix2000/2.0/tls/html/OpenSslUtils3.html>`__
#. Enter the following commands:

   .. code:: bash

      openssl_genrsa 2048 > server.key
      openssl_req -new -x509 -key server.key -out server.cert -days 365 -config openssl.cnf

#. Answer the questions with anything you like, but use your domain name
   as common name (CN)
#. Forward TCP port 465 to Fritz!Box port 10465 (SSMTP)
#. Forward TCP port 995 to Fritz!Box port 10995 (POP3S)
#. Activate the XMail options SSMTP and POP3S (note that the checkboxes
   don't show up checked again before changeset
   `r4760 </changeset/4760>`__)
#. Test by checking your e-mail with SSL (port 995) enabled

.. _Usefullinks:

Useful links
============

-  `​XMail Home Page <http://www.xmailserver.org/>`__
-  `​PHPXmail source
   forge <http://sourceforge.net/projects/phpxmail/>`__
-  `​PhpXMail
   Configuration <http://wiki.qnap.com/wiki/PhpXMail_Configuration>`__
-  `​IPPF: Mailserver für die
   Fritzbox? <http://www.ip-phone-forum.de/showthread.php?t=103699&highlight=PHPXMail>`__
-  `​IPPF: [PATCH]: XMail
   funktioniert <http://www.ip-phone-forum.de/showthread.php?t=205071&highlight=PHPXMail>`__
   \*
-  `​OpenSSL Self-signed Test
   Certificates <http://sial.org/howto/openssl/self-signed/>`__
-  `​HOWTO: Creating SSL certificates with CAcert.org and
   OpenSSL <http://www.lwithers.me.uk/articles/cacert.html>`__
-  `​Welche Webmail-Oberflächen in PHP gibt
   es? <http://www.php-faq.de/q-scripte-webmailer.html>`__
-  `​AfterLogic WebMail
   Pro <http://www.afterlogic.com/products/webmail-pro>`__

-  Tags
-  `mail </tags/mail>`__
-  `network </tags/network>`__
-  `packages <../packages.html>`__
