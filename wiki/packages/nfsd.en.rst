.. _NFSD_CGI:

NFSD_CGI
--------

| NFSD_CGI is the web-interface for the NFSD (Server) on Freetz.

| Some observations:
| Currently using NFS with a 7390 using Freetz-trunk revision 11466.
| Using this revision I didn't observe permission issues like with
  Freetz-1.2 for my 7270v3.
| As mount I'm using a `NDAS-NetDisk <ndas.html>`__ which is Ext3
  formatted.

.. _etcexportsexportsinGUI:

/etc/exports (exports in GUI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| My currect config allows 192.168.178.0/24 and localhost (for the local
  NFS Client).

.. code:: bash

   /var/media/ndas/ext3 192.168.178.0/255.255.250.0(rw,no_subtree_check) localhost(rw)

/etc/hosts.allow
~~~~~~~~~~~~~~~~

| Looks only the first two lines are needed, but the others should not
  harm.

.. code:: bash

   mountd,nfsd,portmap: 192.168.178.0/255.255.255.0 , localhost
   lockd: 192.168.178.0/255.255.255.0 , localhost
   rquotad: 192.168.178.0/255.255.255.0 , localhost
   statd: 192.168.178.0/255.255.255.0 , localhost

/etc/hosts.deny
~~~~~~~~~~~~~~~

| Only deny the NFS related services

.. code:: bash

   mountd,nfsd,portmap:ALL
   lockd:ALL
   rquotad:ALL
   statd:ALL

.. _VerificationonServer::

Verification on Server:
~~~~~~~~~~~~~~~~~~~~~~~

| Below some helpfull commands for trouble-shooting on the server.
| Unfortunately ``rpcinfo`` and ``nfsstat`` where not available on my
  FB. Maybe ``rpcinfo`` is available if 'replace kernel' is used.

List of kernel supported filesystems by the FB:

.. code:: bash

   cat /proc/filesystems

| Just look if the filesystems you are planning to use are listed.

.. code:: bash

   /etc/init.d/rc.nfsd status

| Status should be ``running``. Use the following ``ps`` command first
  to see which processes are actually running before restarting the nfs
  server.

.. code:: bash

   ps -wl | grep 'nfs\|portmap\|lockd\|statd\|mountd\|quota'

| portmap, lockd, mountd, and nfsd should be all listed as a process.
| You can use ``/etc/init.d/rc.nfsd stop`` and
  ``/etc/init.d/rc.nfsd start`` to stop and start the nfs server.

.. code:: bash

   exportfs

| Should show the hosts or subnets (incl. localhost if configured)
  configured in /etc/exports

.. code:: bash

   mount

| Look that the mounted disk allows rw (if intended)

If you also have the `NFS Client </wiki/packages/nfs.en>`__ installed on
the FB, the following verification is available:

.. code:: bash

   mount -t nfs localhost:/<share-path> /<mount-point>

To show from the server which nfs exports are in use:

.. code:: bash

   showmount --all
   showmount --exports

To verify layer-4 network information (e.g. used ports):

.. code:: bash

   netstat -anp

| 

.. code:: bash

   logread

.. _rsizeandwsizebuffers:

rsize and wsize buffers
~~~~~~~~~~~~~~~~~~~~~~~

| The read and write buffers are assigned during the ``mount`` on the
  client.
| The server supports a buffer size that range from 4kbytes to
  1024kbytes (RPCSVC_MAXPAYLOAD (1*1024*1024u)) in steps of 1kbyte.
| Finding the optimal buffer size is normally the best option to get a
  better performance.
| I only have a ndas Net-Disk mounted, and found that all rsize values
  had a similar variation in the results.
| The FB CPU is the bottleneck.
| It might be interesting to retest this with a USB-stick to see if than
  varying the buffersizes would show a difference.

| I tested the performance with
  `​Bonnie++ <http://www.coker.com.au/bonnie++>`__ using one of the
  `​experimental
  versions <http://www.coker.com.au/bonnie++/experimental/>`__

.. _Bonnie:

Bonnie++
^^^^^^^^

| For this I used two scripts to: run the test, unmount/mount both
  client and server mounts, restart nfsd, and mounted the client with a
  different rsize parameter.
| During the tests I only varied the rsize parameter, because I'm only
  interested in the read optimalisation now, but changing both wsize and
  rsize is also possible.
| Each test takes about 35 minutes (with 1gigbyte transfers), so you can
  do about 16 overnight.
| Here the scripts I used:

main script:

.. code:: bash

   #!/bin/sh

   # the initial test with a rsize of 32768 (=32k) and increased with steps of 32k to 1024k
   # rsize=32768
   # for the second test again 32 test using 1gigabyte using the best result -16*1k to +16*1k
   # rsize to test is rsize=294912. Start rsize is
   rsize=(294912-16384)
   i=1
   date > results.txt
   date +%s >> results.txt
   while [ $i -le 32 ]; do
           echo ======================================================= >> results.txt
           echo =======================================================
           echo setup bonny++ test with rsize of $(($rsize+1024*$i))
           echo setup bonny++ test with rsize of $(($rsize+1024*$i)) >> results.txt
           mount -o hard,intr,rsize=$(($rsize+1024*$i)) 192.168.178.1:<full_share_path> <local_mount_point>
           bonnie++ -d <local_mount_point> -s 1g -n 0 -m nfs_client_$rsize -f -b -u root >> results.txt 2>> results.txt
           echo ======================================================= >> results.txt
           umount <local_mount_point>
           expect autologin.sh
           i=$(($i + 1))
   done
   date >> results.txt
   date +%s >> results.txt

expect script:

.. code:: bash

   #!/usr/bin/expect

   spawn ssh root@192.168.178.1
   # expect "connecting (yes/no)?"
   # send "yes\r"
   expect "assword:"
   send "<your_passwd>\r"
   expect "#"
   send "/etc/init.d/rc.nfsd stop\r"
   expect "done."
   send "umount /dev/nda2\r"
   expect "#"
   send "mount /dev/nda2 <mount-point>\r"
   expect "#"
   send "/etc/init.d/rc.nfsd start\r"
   expect "done."

You can obtain a nice html page of your results with:

.. code:: bash

   cat results.txt | grep ,,, | bon_csv2html > /tmp/nfs_client_test.html

But you can also use the csv format output in an Excel sheet. I attached
3 html files showing my results.

.. _MRTGCPUUtil:

MRTG CPU Util
^^^^^^^^^^^^^

.. figure:: /screenshots/276.png
   :alt: CPU Util 7390 bonnie++ test script

   CPU Util 7390 bonnie++ test script

| In the `MRTG <netsnmp.en.html>`__ graph of the CPU Utilization you can
  clearly see that the CPU Utilization is the bottleneck in my setup
  using a `NDAS NetDisk <ndas.html>`__.
| The picture shows I started the test at about 7:20am which took until
  1:10am the next day.
| Than I did two manual bonny++ tests at 1:15am and 2am. Than started a
  new batch test using the scripts at about 2:45am.

.. _References:

References
~~~~~~~~~~

| `​NFS howto <http://nfs.sourceforge.net/nfs-howto/index.html>`__
| `​bonnie++ <http://www.coker.com.au/bonnie++/>`__ and the
  `​experimental <http://www.coker.com.au/bonnie++/experimental/>`__
  page
| `​bonnie++ examples <http://www.googlux.com/bonnie.html>`__

Anhänge (3)
~~~~~~~~~~~

-  `ndas_nfs_client_32k_1024k.html </attachment/wiki/packages/nfsd.en/ndas_nfs_client_32k_1024k.html>`__\ `​ </raw-attachment/wiki/packages/nfsd.en/ndas_nfs_client_32k_1024k.html>`__
   (33.3 KB) - hinzugefügt von *RomMon* `vor 4
   Jahren </timeline?from=2014-01-04T16%3A27%3A55Z&precision=second>`__.
   “Bonnie++ test results 7390 rsize from 32kbytes to 1024kbytes with
   32kbytes steps”
-  `ndas_nfs_client_288k_test.html </attachment/wiki/packages/nfsd.en/ndas_nfs_client_288k_test.html>`__\ `​ </raw-attachment/wiki/packages/nfsd.en/ndas_nfs_client_288k_test.html>`__
   (33.3 KB) - hinzugefügt von *RomMon* `vor 4
   Jahren </timeline?from=2014-01-04T16%3A30%3A22Z&precision=second>`__.
   “„Bonnie++ test results 7390 rsize 288k plus/minus 16k in steps of
   1k”
-  `ndas_nfs_client_287k_test.html </attachment/wiki/packages/nfsd.en/ndas_nfs_client_287k_test.html>`__\ `​ </raw-attachment/wiki/packages/nfsd.en/ndas_nfs_client_287k_test.html>`__
   (10.3 KB) - hinzugefügt von *RomMon* `vor 4
   Jahren </timeline?from=2014-01-04T16%3A31%3A17Z&precision=second>`__.
   “Bonnie++ test results 7390 rsize is 287k 8 repeates”

Alle Anhänge herunterladen als:
`.zip </zip-attachment/wiki/packages/nfsd.en/>`__
