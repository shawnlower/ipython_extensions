Overview
========

A collection of (currently 1) extensions for [https://ipython.org/](iPython).

Mostly created to play around with ipython and %magic, but possibly useful.

Installation
============

- Copy the extension into ~/.ipython/extensions
- Ensure your config contains the following:
```
$ grep 'module_list' ~/.ipython/profile_default/ipython_config.py 
c.InteractiveShellApp.extensions = [ 'module_list' ]
```
  *note:* you can generate a new config with *ipython profile create*


Contents
========

- module_list


module_list
-----------

```bash
In [1]: import types

In [2]: from rdflib import plugins
INFO:rdflib:RDFLib Version: 4.2.2

In [3]: from rdflib.plugins.parsers import pyRdfa

In [4]: %modules
Out[4]: 
builtins   <built-in>
rdflib.plugins   /home/shawn/projects/rest-app/rest-app.git/venv/lib/python3.6/site-packages/rdflib-4.2.2-py3.6.egg/rdflib/plugins
rdflib.plugins.parsers.pyRdfa   /home/shawn/projects/rest-app/rest-app.git/venv/lib/python3.6/site-packages/rdflib-4.2.2-py3.6.egg/rdflib/plugins/parsers/pyRdfa
types                           <built-in>

```

