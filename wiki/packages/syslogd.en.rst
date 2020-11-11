.. _Syslog:

Syslog
------

| The syslog package enables to log messages local to memory, to a local
  disk (e.g. USB), or remote to another server.
| For the local memory a FIFO buffer is used, with a default size of
  200KB.

.. _SetupinFreetzweb-interface:

Setup in Freetz web-interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /screenshots/239.jpg
   :alt: Howto Syslog Setup

   Howto Syslog Setup

.. _Usageofsyslog:

Usage of syslog
~~~~~~~~~~~~~~~

The syslog messages can be displayed via the web-interface via:

.. code:: bash

   Status > Syslog

You can filter on some items depending on your configuration and used
packages (e.g. hostapd, login, INADYN).

Another option is to view the messages via a telnet or ssh connection
using the following commands:

.. code:: bash

   logread

You can monitor the syslog messages where all new messages are displayed
using the command:

.. code:: bash

   logread -f

(With CTRL-C you can stop the monitoring.)
