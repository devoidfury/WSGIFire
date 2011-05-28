from wsgifire.exceptions import ModuleDoesNotExist
from importlib import import_module
from importlib.machinery import PathFinder

def func_from_str(mod_string):
    """
    Return the object referenced by `mod_string`.

    This is used in importing modules set in strings in settings files,
    providing a flexible interface allowing some internals to be swapped out
    easily, such as error views.

    - `mod_string`: string that should resolve to a valid module.object path.
    """
    mod_name, sep, func = mod_string.rpartition('.')

    loader = PathFinder.find_module(mod_name)

    if loader:
        mod = import_module(mod_name)
        return getattr(mod,func)
    else:
        module_error = ModuleDoesNotExist(mod_string)
        raise module_error     

