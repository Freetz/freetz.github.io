.. _ReleaseManagement:

Release Management
==================

**Warning Work In Progress Warning**

.. _SubversionRepository:

Subversion Repository
---------------------

The subversion repository of Freetz follows the recommended repository
layout by the subversion maintainers. [1]

.. code:: bash

   /
     trunk
     branches
     tags

The main development is done in the trunk. A branch could be created if
a developer wants to work on a topic without the guaranteed stability of
his checkins all the time. Also a branch is forked when a new stable
release is planned. This branch holds the future major version (e.g.
1.2).

Mainly bugfixes should be commited to this branch. But security version
bumps are allowed, too.

Later on the Releases 1.2.1, 1.2.2 and so on should be tagged from this
branch.

Tagged versions should never be modified afterwards even if they seem
nothing else like a branch from the repository view.

.. _Checklists:

Checklists
----------

In the following sections you can find the TODOs before branching and
tagging.

.. _Creatinganewstablebranch:

Creating a new stable branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Before creating a new stable branch:

   -  Update CHANGELOG file
   -  Merge changes from last stable-branch (if not done already)
   -  Rename devel-section to new stable version

-  Copy branch
-  After creating the new branch:

   -  Update version in .version file
   -  Update Config.in (set VERBOSITY_LEVEL=0 and SUBVERSION_STRING=n)
   -  Remove labor firmwares (Config.in and FIRMWARES file)
   -  Add new devel-section to CHANGELOG file in trunk

.. _Tagginganewrelease:

Tagging a new release
~~~~~~~~~~~~~~~~~~~~~

TODO

.. _GIT:

GIT
---

As the popularity of GIT is growing rapidly, we provide a GIT mirror on
`​github <https://github.com/>`__. At the moment only the trunk is
mirrored to github because of the different repository layout it's
difficult to sync all branches and tags. The mirror can be found
`​here <https://github.com/Freetz/freetz>`__. [2]

.. _Downloads:

Downloads
---------

TODO

.. _References:

References
----------

| `[1] </changeset/1>`__ `​Subversion Best
  Practices <http://svn.apache.org/repos/asf/subversion/trunk/doc/user/svn-best-practices.html>`__
| `[2] </changeset/2>`__ `​Freetz Github
  Mirror <https://github.com/Freetz/freetz>`__

-  Tags
-  `development </tags/development>`__
-  `howtos </tags/howtos>`__
