dtach
=====

*"dtach is a free (GPL'ed) program for POSIX-compliant OSs intended to
provide similar functionality to that of the GNU Project's Screen, but
stripping out what the developer (Ned T. Crigler) considers to be
unneeded features to provide a much slimmer product; in addition, it is
intended to interfere less with key bindings than Screen does."*
(source: Wikipedia - see below)

*Dtach* is a tiny program that emulates the detach feature of
`screen <screen.html>`__, allowing you to run a program in an
environment that is protected from the controlling terminal and attach
to it later. It was introduced in Freetz trunk
`2636 </changeset/2636>`__ by whoopie. It is smaller than the
aforementioned *screen*.

.. _Bedienung:

Bedienung
---------

Erstellen einer neuen dtach-Session am Beispiel von
`mcabber <mcabber.html>`__:

.. code:: bash

   dtach -c /tmp/mcabber.dtach mcabber

Erstellen einer neuen dtach-Session, aber direkt wieder die Session
verlassen bzw. im Hintergrund starten:

.. code:: bash

   dtach -n /tmp/mcabber.dtach mcabber

Mit "*Strg + \\*" kann man die Session verlassen.

Wieder in die Session "einklinken":

.. code:: bash

   dtach -a /tmp/mcabber.dtach

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

-  `​Sourceforge-Projektseite
   (Englisch) <http://dtach.sourceforge.net>`__
-  `​Wikipedia (Englisch) <http://en.wikipedia.org/wiki/Dtach>`__
-  `​Thread for discussion in
   IP-Phone-Forum.de <http://www.ip-phone-forum.de/showthread.php?t=176923>`__

-  Tags
-  `console </tags/console>`__
-  `packages <../packages.html>`__
-  `tools </tags/tools>`__
