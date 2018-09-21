ProTemp
=======

A template system for quickly setting up project folders for programming projects.

Put the folder in ``$PATH`` and run ``protemp`` from wherever you may which to create a new project. Eventually the plan is that you're to choose a template (e.g. ``py`` for python projects, and that you should be able to make your own templates. For now there's only one fixed Python setup in the ``py`` folder. When you create a new project it will duplicate the template you choose (currently only Python) and replace tags with correct values. Tags in file contents and file names are indicated as ``{tag}``.
