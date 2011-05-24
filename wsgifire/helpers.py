
def func_from_str(mod_string):
    """Return the func/class/etc referenced by <mod_string>, which should
        be a valid module path."""
    func = mod_string.split('.')[-1]
    mod_name = ".".join(mod_string.split('.')[:-1])
    mod = __import__(mod_name,fromlist=[func])
    return getattr(mod,func)
