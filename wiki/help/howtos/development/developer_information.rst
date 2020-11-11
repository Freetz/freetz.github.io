.. _DeveloperInformation:

Developer Information
=====================

Most of the information for developers is still only available in the
`​IPPF wiki <http://wiki.ip-phone-forum.de/software:ds-mod:start>`__,
but it is partly outdated and quite disarranged. This shall be a
starting point for writing current developer information regarding
freetz.

Table of Contents
^^^^^^^^^^^^^^^^^

#. `Package
   Development <developer_information/package_development.html#PackageDevelopment>`__

   #. `Persistent Package
      Settings <developer_information/package_development.html#PersistentPackageSettings>`__

#. `Package Developing - Advanced
   Topics <developer_information/package_development_advanced.html#PackageDeveloping-AdvancedTopics>`__

   #. `Adding conditional
      patches <developer_information/package_development_advanced.html#Addingconditionalpatches>`__
   #. `Adding multi-binary
      packages <developer_information/package_development_advanced.html#Addingmulti-binarypackages>`__

#. `Paketverwaltung für
   Freetz <developer_information/package_development_dynamic.html#PaketverwaltungfürFreetz>`__

   #. `Erweiterung des
      Dateisystems <developer_information/package_development_dynamic.html#ErweiterungdesDateisystems>`__
   #. `Paketverwaltung <developer_information/package_development_dynamic.html#Paketverwaltung>`__
   #. `Links <developer_information/package_development_dynamic.html#Links>`__
   #. `Kommentare <developer_information/package_development_dynamic.html#Kommentare>`__

#. `First steps - How to start your first freetz
   package <developer_information/package_development_start.html#Firststeps-Howtostartyourfirstfreetzpackage>`__

   #. `Info <developer_information/package_development_start.html#Info>`__
   #. `Build
      Environment <developer_information/package_development_start.html#BuildEnvironment>`__
   #. `File
      Structure <developer_information/package_development_start.html#FileStructure>`__
   #. `Examples Binary
      Package <developer_information/package_development_start.html#ExamplesBinaryPackage>`__
   #. `Configuration
      Handling <developer_information/package_development_start.html#ConfigurationHandling>`__
   #. `Examples
      Web-Interface <developer_information/package_development_start.html#ExamplesWeb-Interface>`__
   #. `Trouble
      shooting <developer_information/package_development_start.html#Troubleshooting>`__

#. `Example 1:
   Httptunnel <developer_information/package_development_start/example_1.html#Example1:Httptunnel>`__

   #. `Build
      manually <developer_information/package_development_start/example_1.html#Buildmanually>`__
   #. `Add package to
      Freetz <developer_information/package_development_start/example_1.html#AddpackagetoFreetz>`__
   #. `Call Procedures "make menuconfig" and
      "make" <developer_information/package_development_start/example_1.html#CallProceduresmakemenuconfigandmake>`__
   #. `Testing <developer_information/package_development_start/example_1.html#Testing>`__
   #. `Preparing New Package for Public Integration to Freetz
      Trunk <developer_information/package_development_start/example_1.html#PreparingNewPackageforPublicIntegrationtoFreetzTrunk>`__

#. `Example 2:
   par2cmdline <developer_information/package_development_start/example_2.html#Example2:par2cmdline>`__

   #. `Build
      manually <developer_information/package_development_start/example_2.html#Buildmanually>`__
   #. `Add package to
      Freetz <developer_information/package_development_start/example_2.html#AddpackagetoFreetz>`__
   #. `Create new image with added
      package <developer_information/package_development_start/example_2.html#Createnewimagewithaddedpackage>`__
   #. `Testing <developer_information/package_development_start/example_2.html#Testing>`__
   #. `Preparing New Package for Public Integration to Freetz
      Trunk <developer_information/package_development_start/example_2.html#PreparingNewPackageforPublicIntegrationtoFreetzTrunk>`__

#. `Example 3:
   NZBGet <developer_information/package_development_start/example_3.html#Example3:NZBGet>`__

   #. `Build
      manually <developer_information/package_development_start/example_3.html#Buildmanually>`__
   #. `Add package to
      Freetz <developer_information/package_development_start/example_3.html#AddpackagetoFreetz>`__
   #. `Create new image with added
      package <developer_information/package_development_start/example_3.html#Createnewimagewithaddedpackage>`__
   #. `Testing <developer_information/package_development_start/example_3.html#Testing>`__
   #. `Preparing New Package for Public Integration to Freetz
      Trunk <developer_information/package_development_start/example_3.html#PreparingNewPackageforPublicIntegrationtoFreetzTrunk>`__

#. 

   #. `Web-interface
      HTTPTunnel <developer_information/package_development_start/webinterface_example_1.html#Web-interfaceHTTPTunnel>`__

#. `Trac
   Hooks <developer_information/post_commit_hook.html#TracHooks>`__

   #. `trac-post-commit-hook <developer_information/post_commit_hook.html#trac-post-commit-hook>`__
   #. `trac-post-revprop-change-hook <developer_information/post_commit_hook.html#trac-post-revprop-change-hook>`__

#. `Shell Coding
   Conventions <developer_information/shell_coding_conventions.html#ShellCodingConventions>`__

   #. `Shell
      Language <developer_information/shell_coding_conventions.html#ShellLanguage>`__
   #. `Basic
      Format <developer_information/shell_coding_conventions.html#BasicFormat>`__
   #. `If, For, and
      While <developer_information/shell_coding_conventions.html#IfForandWhile>`__
   #. `Test
      Built-in <developer_information/shell_coding_conventions.html#TestBuilt-in>`__
   #. `Single-line conditional
      statements <developer_information/shell_coding_conventions.html#Single-lineconditionalstatements>`__
   #. `Infinite
      Loops <developer_information/shell_coding_conventions.html#InfiniteLoops>`__
   #. `Exit Status and If/While
      Statements <developer_information/shell_coding_conventions.html#ExitStatusandIfWhileStatements>`__
   #. `Variable
      References <developer_information/shell_coding_conventions.html#VariableReferences>`__
   #. `Variable
      Naming <developer_information/shell_coding_conventions.html#VariableNaming>`__
   #. `Quoting <developer_information/shell_coding_conventions.html#Quoting>`__
   #. `Variable
      Assignments <developer_information/shell_coding_conventions.html#VariableAssignments>`__
   #. `Testing for (Non-)Empty
      Strings <developer_information/shell_coding_conventions.html#TestingforNon-EmptyStrings>`__
   #. `Commenting <developer_information/shell_coding_conventions.html#Commenting>`__
   #. `Pathnames <developer_information/shell_coding_conventions.html#Pathnames>`__
   #. `Interpreter
      Magic <developer_information/shell_coding_conventions.html#InterpreterMagic>`__

#. `libmodcgi.sh <developer_information/webif/libmodcgi.html#libmodcgi.sh>`__

   #. `cgi <developer_information/webif/libmodcgi.html#cgi>`__
   #. `cgi_begin <developer_information/webif/libmodcgi.html#cgi_begin>`__
   #. `cgi_end <developer_information/webif/libmodcgi.html#cgi_end>`__
   #. `sec_begin <developer_information/webif/libmodcgi.html#sec_begin>`__
   #. `sec_end <developer_information/webif/libmodcgi.html#sec_end>`__
   #. `html <developer_information/webif/libmodcgi.html#html>`__
   #. `check,
      select <developer_information/webif/libmodcgi.html#checkselect>`__
   #. `href <developer_information/webif/libmodcgi.html#href>`__
   #. `back_button <developer_information/webif/libmodcgi.html#back_button>`__
   #. `sec_level <developer_information/webif/libmodcgi.html#sec_level>`__
   #. `stat_bar <developer_information/webif/libmodcgi.html#stat_bar>`__
   #. `cgi_param <developer_information/webif/libmodcgi.html#cgi_param>`__
   #. `cgi_error,
      print_error <developer_information/webif/libmodcgi.html#cgi_errorprint_error>`__
   #. `path_info <developer_information/webif/libmodcgi.html#path_info>`__
   #. `valid <developer_information/webif/libmodcgi.html#valid>`__

-  `Writing Wiki Articles <../../wikiedit.html>`__

-  Interner Entwicklerbereich: Nur für Entwickler: Interner Bereich zur
   Abstimmung.
