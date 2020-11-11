.. _Ereignisse:

Ereignisse
==========

Ein erfolgreicher eingehender Anruf erzeugt nacheinander folgende
Ereignisse (analog für ausgehende Anrufe mit ``out:*``):

#. in:request
#. in:connect
#. in:disconnect

Ein Anruf, der abgebrochen wird, bevor die Gegenseite ihn annimmt,
erzeugt folgende Ereignisse:

#. in:request
#. in:cancel

Die Ereignisse sind nicht direkt die Rohereignisse, wie sie an der
JFritz-Schnittstelle (Port 1012) sichtbar sind, sondern entstehen aus
diesen (bei gleicher ID) mit Hilfe eines endlichen Automaten (an den
Kanten sind oben die Eingangsereignisse angegeben, unten die
Ausgangsereignisse; das Ereignis ``in:accept`` wird nur intern benutzt):

.. figure:: /screenshots/36.png
   :alt: CallMonitor: Ereignisse

   CallMonitor: Ereignisse

-  Tags
-  `callmonitor </tags/callmonitor>`__
