
def func_from_str(mod_string):
    """Return the func/class/etc referenced by <mod_string>, which should
        be a valid module path. This is used in importing modules set in
        strings in settings files, providing a flexible interface allowing
        some internals to be swapped out easily, such as error views.
        """
    mod_name, sep, func = mod_string.rpartition('.')
    mod = __import__(mod_name,fromlist=[func])
    return getattr(mod,func)
