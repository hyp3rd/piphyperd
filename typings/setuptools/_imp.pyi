"""
This type stub file was generated by pyright.
"""

"""
Re-implementation of find_module and get_frozen_object
from the deprecated imp module.
"""
PY_SOURCE = 1
PY_COMPILED = 2
C_EXTENSION = 3
C_BUILTIN = 6
PY_FROZEN = 7
def find_spec(module, paths):
    ...

def find_module(module, paths=...):
    """Just like 'imp.find_module()', but with package support"""
    ...

def get_frozen_object(module, paths=...):
    ...

def get_module(module, paths, info):
    ...
