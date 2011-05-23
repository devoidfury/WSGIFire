
def func_from_str(string):
    func = string('.')[-1]
    mod_name = ".".join(string('.')[:-1])
    mod = __import__(mod_name,fromlist=[func])
    return getattr(mod,func)
