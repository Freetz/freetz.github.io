.. _JamVM:

JamVM
=====

`​JamVM <http://jamvm.sourceforge.net/>`__ ist eine neue `​Java Virtual
Machine <http://en.wikipedia.org/wiki/Java_Virtual_Machine>`__, die der
JVM Spezifikation Version 2 (blue book) entspricht. Im `​Vergleich mit
den meisten anderen
VM's <http://bugblogger.com/java-vms-compared-160/>`__ (frei und
kommerziell) ist *JamVM* extrem klein ("stripped executables" für
PowerPC nur ~160K, und für Intel 140K). Dennoch unterstützt es, anders
als andere "kleine" VMs (z.B. KVM) die vollständige Spezifikation, und
enthält Support für "object finalisation", Soft/Weak/Phantom Referenzen,
class-unloading, das `​Java Native
Interface <http://de.wikipedia.org/wiki/Java_Native_Interface>`__ (JNI)
und die Reflection API.

JamVM nutzt die `​GNU
Classpath <http://de.wikipedia.org/wiki/GNU_Classpath>`__ Java Class
Library. Eine Reihe von Klassen sind Referenz-Klassen, die für eine
spezielle VM angepasst werden müssen. Diese werden zusammen mit *JamVM*
gebündelt.

|Warning| **Anmerkung:** *JamVM* wird nicht mit der Class Library von Suns
oder IBMs JVMs funktionieren.

Da die normale Klassenbiliothek (glibj.zip) über 9 MB groß ist wird
standardmäßig nur eine reduzierte Version (mini.jar) installiert.
Deshalb muss jamvm folgendermaßen aufgerufen werden um z.B. die Datei
Hello.class im aktuellen Verzeichnis aufzurufen:

.. code:: bash

   jamvm -Xbootclasspath/a:/usr/share/classpath/mini.jar Hello

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

-  `​JavaVM Homepage <http://jamvm.sourceforge.net/>`__
-  `​Vergleich verschiedener
   JVMs <http://bugblogger.com/java-vms-compared-160/>`__
-  `​List of
   JVMs <http://en.wikipedia.org/wiki/List_of_Java_virtual_machines>`__
-  `​freie Java
   Implementierungen <http://en.wikipedia.org/wiki/Free_Java_implementations>`__

-  Tags
-  `packages <../packages.html>`__

.. |Warning| image:: ../../chrome/wikiextras-icons-16/exclamation.png

