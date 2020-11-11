hiawatha
========

"*Hiawatha is a webserver for Unix and has been build with security in
mind. This resulted in a highly secure webserver, in both code and
features. This webserver runs on Linux, BSD, MacOS X and Windows.
Although it can run any kind of CGI / FastCGI application, it has been
optimized for usage with PHP.*"

.. _Quickcompare:

Quick compare
-------------

+------------+---------------------+---------------------+
|            | **Memory** :sup:`1` | **Binary** :sup:`2` |
+------------+---------------------+---------------------+
| *hiawatha* | ~1320 kB            | ~105 kB             |
+------------+---------------------+---------------------+
| *lighttpd* | ~1768 kB            | ~409 kB             |
+------------+---------------------+---------------------+

#. After one request "*Hello world!* "
#. Minimal menuconfig, including libraries, excluding *pthread*,
   *md5sum*

.. code:: bash

   -rwxr-xr-x    1 root     root        105788 Apr 25 20:29 hiawatha
   -rwxr-xr-x    1 root     root        150324 Apr 25 10:56 lighttpd
   -rwxr-xr-x    1 root     root          5496 Apr 25 10:56 mod_access.so
   -rwxr-xr-x    1 root     root         16772 Apr 25 11:11 mod_dirlisting.so
   -rwxr-xr-x    1 root     root          6320 Apr 25 10:56 mod_indexfile.so
   -rwxr-xr-x    1 root     root         10584 Apr 25 10:56 mod_staticfile.so
   -rwxr-xr-x    1 root     root        219916 Apr 24 08:54 libpcre.so.0.0.1

.. _Security:

Security
--------

You might want to add this or similar to the extra configuration:

.. code:: bash

   BanOnGarbage = 300
   BanOnMaxPerIP = 60
   BanOnMaxReqSize = 300
   KickOnBan = yes
   RebanDuringBan = yes

And you might want to limit the number of simultaneous connections too:

.. code:: bash

   ConnectionsTotal = 5
   ConnectionsPerIP = 3

.. _Links:

Links
-----

-  `​Homepage <http://www.hiawatha-webserver.org/>`__
-  `Ticket with patches </ticket/1139>`__
-  `​Linux magazine about
   hiawatha <http://www.linux-magazine.com/Issues/2009/107/Hiawatha>`__
