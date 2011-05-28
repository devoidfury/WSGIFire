from importlib import import_module

def func_from_str(mod_string):
    """
    Return the object referenced by `mod_string`.

    This is used in importing modules set in strings in settings files,
    providing a flexible interface allowing some internals to be swapped out
    easily, such as error views.

    - `mod_string`: string that should resolve to a valid module.object path.
    """
    mod_name, sep, func = mod_string.rpartition('.')
    mod = import_module(mod_name)
    return getattr(mod,func)
