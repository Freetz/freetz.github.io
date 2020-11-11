.. _Dropbear:

Dropbear
--------

| Drobear is a small ssh server, client with keygenerator and scp
  support.
| More information about dropbear can be found at
  `​http://matt.ucc.asn.au/dropbear/dropbear.html <http://matt.ucc.asn.au/dropbear/dropbear.html>`__

.. _CreatingaFeetzImagewithDropbrear:

Creating a Feetz Image with Dropbrear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Follow the directions from the `Wiki <../index.en.html#>`__
| After the following step you can configure the packages you want to
  have included in your image.

.. code:: bash

   make menuconfig

Make sure the following is selected:

.. code:: bash

   Package selection  ---> Standard packages  ---> [*] Dropbear 0.53.1
   Package selection  ---> Standard packages  ---> [ ]   Without scp & ssh client (NEW)
   Package selection  ---> Standard packages  ---> [ ]   With zlib Compression (NEW)
   Package selection  ---> Standard packages  ---> [*]   Disable DNS reverse-lookup of the client (NEW)
   Package selection  ---> Standard packages  ---> [ ]   Build static binary (NEW)

.. _SetupinFreetzweb-interface:

Setup in Freetz web-interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Using the Dropbear setup page you can enable Dropbear to start
  automatically at bootup.

.. figure:: /screenshots/249.jpg
   :alt: Dropbear setup

   Dropbear setup

| From the setup page you can also select to edit authorized_keys file
  which allows you to access the router with pre-shared keys i.s.o. just
  a password.
| Selecting to edit the authorized_keys file will redirect you to SSH >
  authorized_keys
| Look at the `authorized_key <authorized-keys.html>`__ page for more
  info.
