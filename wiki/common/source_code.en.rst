.. _Sourcecode:

Source code
===========

The Freetz source code is managed in a
`​Subversion <http://subversion.apache.org>`__ repository. Subversion is
generally abbreviated by SVN.

.. _Developerversiontrunk:

Developer version (trunk)
-------------------------

|Warning| This version is only for experienced users and developers who
know how to help themselves! The trunk changes continuously and might
temporarily contain bugs or not work at all.

Check out from SVN:

.. code:: bash

   $ svn co http://svn.freetz.org/trunk                     <--- check out current trunk revision
   $ svn co http://svn.freetz.org/trunk trunk_7843 -r 7843  <--- check out specific trunk revision (here: 7843) into subdirectory
                                                                 "trunk_7843", so as not to overwrite the current trunk directory

Check out from Git (|Warning| Git is not the leading system and is
officially unsupported presently. We provide it "as is" for test
purposes.):

.. code:: bash

   $ git clone https://github.com/Freetz/freetz.git freetz-devel  <--- freetz-devel: local copy of Git repository

.. _Updates:

Updates
-------

How to update an existing local SVN repository (here: developer
version):

.. code:: bash

   $ cd trunk
   $ svn up         <--- update to current revision
   $ svn up -r 7843 <--- update to specific revision (here: 7843)

How to update an existing local Git repository (here: developer
version):

.. code:: bash

   $ cd freetz-devel
   $ git pull

.. _Stableversion:

Stable version
--------------

|Warning| **The "stable" version is not maintained anymore. Newer boxes as
well as firmwares are not available there. Please use whenever possible
the trunk as mentioned above.** |Warning|

For some box types no firmware is available on AVM servers. Help
yourself using this
`info <../FAQ.html#Couldnotdownloadfirmwareimage>`__.

Depending on your hardware type you need one of the following Freetz
versions:

**freetz-2.0**: current stable version (list of supported boxes and
firmware versions)

.. code:: bash

   $ svn co http://svn.freetz.org/branches/freetz-stable-2.0

**ds-0.2.9-p8** (kernel 2.4): for very old boxes which do not get AVM
firmware updates anymore (more
`​info <http://www.ip-phone-forum.de/showthread.php?t=135253>`__)

.. code:: bash

   $ svn co http://svn.freetz.org/tags/ds-0.2.9-p8

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

