s3fslite
========

"*s3fslite is a fork of s3fs, originally written by Randy Rizun. It is a
file system that stores all data in an Amazon S3 bucket. It allows
access to a bucket as though it were a local file system. It is useful
for publishing static web data that can be read easily by a browser, or
for backing up private or shared data.*"

.. _Usage:

Usage
-----

See the home page for detailed usage instructions. Be sure to specify
the following options:

.. code:: bash

   -o attr_cache=
   -o writeback_cache=

to a non-memory location to prevent running out of memory when storing
larger files (your box could crash and reboot).

For example:

.. code:: bash

   s3fs <bucket> <mount point> \
   -o attr_cache=/var/media/ftp/uStor01/... \
   -o writeback_cache=/var/media/ftp/uStor01/...

| You can store your credentials in */tmp/flash/passwd-s3fs*, if you
  don't want to specify them on the command line.

It is possible to use a *mime.types* file, if you want to access your
objects from internet: (for example for a static web site) 

-  Copy */etc/mime.types* to your box, for example to
   */var/media/ftp/uStor01/mime.types*
-  Create a symbolic link like this: *ln -s
   /var/media/ftp/uStor01/mime.types /tmp/flash/mime.types*

Using *rsync* to make backups:

.. code:: bash

   rsync -avW --delete /source-folder/ /mount-point/

Advice: read the man page of rsync, before using it.

.. _Links:

Links
-----

-  `​Home page <http://github.com/russross/s3fslite>`__
-  `​Ticket <http://trac.freetz.org/ticket/796>`__ (with patch)
-  `​Amazon S3 <http://aws.amazon.com/s3/>`__
-  `​Man page
   rsync <http://optics.ph.unimelb.edu.au/help/rsync/rsync.html>`__
