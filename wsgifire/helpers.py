
def func_from_str(mod_string):
    func = mod_string.split('.')[-1]
    mod_name = ".".join(mod_string.split('.')[:-1])
    mod = __import__(mod_name,fromlist=[func])
    return getattr(mod,func)
