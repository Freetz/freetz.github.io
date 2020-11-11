.. _WakeonLAN:

Wake on LAN
===========

Zum Aufwecken eines Rechners im LAN — sofern der Rechner dies generell
unterstützt — dient das in `Freetz <../../../index.html>`__ vorhandene
Programm ``ether-wake``. Zur Benutzung sei auf dessen Online-Hilfe
verwiesen:

.. code:: bash

   Usage: ether-wake [-b] [-i iface] [-p aa:bb:cc:dd[:ee:ff]] MAC

   Send a magic packet to wake up sleeping machines.
   MAC must be a station address (00:11:22:33:44:55) or
       a hostname with a known 'ethers' entry.

   Options:
           -b              Send wake-up packet to the broadcast address
           -i iface        Use interface ifname instead of the default "eth0"
           -p pass Append the four or six byte password PW to the packet
