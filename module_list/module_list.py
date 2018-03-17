from collections import namedtuple
import sys
import types

from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)

class ModuleList(object):
    def __init__(self, globals_dict = globals()):
        self.globals_dict = globals_dict
        self.modules = self.get_modules()

    def __repr__(self):
        repr = ''
        width = 0
        for m in sorted(set(self.modules)):
            if len(m.name) > width:
                width = len(m.name)
            repr += "{:{width}} {}\n".format(m.name, m.path, width=width+2)
        return repr

    def get_modules(self):
        mod = namedtuple('modulelist', ['name', 'path'])
        mod_list = []
        for attr, val in self.globals_dict.items():
            if type(val) == types.ModuleType:
                name = val.__name__

                path = getattr(val, '__path__', '<built-in>')

                if type(path) == type(list()):
                    a = [name, path[0]]
                    mod_list.append(mod(*a))
                else:
                    a = [name, path]
                    mod_list.append(mod(*a))
        return mod_list


@magics_class
class ModuleListMagic(Magics):

    @line_magic
    def modules(self, line):
        # Yikes
        globals_dict = self.parent._instance.user_global_ns
        return ModuleList(globals_dict = globals_dict)

def load_ipython_extension(ipython):
    print("Loaded %modules extension")
    ipython.register_magics(ModuleListMagic)

