| Here some examples using the tools for configuration handling to
  explain the behavior of the available commands.

Example to disable the freetz http web-interface (web-server):

+-----------------------------------+-----------------------------------+
| #. vi /mod/etc/conf/mod.cfg       |    | Change MOD_HTTPD=’yes’ to    |
| #. modconf save mod               |      MOD_HTTPD=’no’               |
| #. modsave flash                  |    | will update/ (create if not  |
|                                   |      existing)                    |
|                                   |      /tmp/flash/mod.diff          |
|                                   |    | saves content of /tmp/flash/ |
|                                   |      to tffs, including the new   |
|                                   |      mod.diff file                |
+-----------------------------------+-----------------------------------+

or use a shortcut for step 2 and 3:

+-----------------------------------+-----------------------------------+
| 2. modsave                        |    This will update all           |
|                                   |    /tmp/flash/<package>.diff      |
|                                   |    files, and save resulting      |
|                                   |    content of /tmp/flash/ to tffs |
+-----------------------------------+-----------------------------------+

| The above steps is to give examples of the available commands.
| To more comfortably obtain the same results:

#. modconf set mod MOD_HTTPD=no
#. modconf save mod
#. modsave flash

or use a shortcut for step 2 and 3:

2. modsave
