import importlib, re
from wsgifire.settings import settings
from wsgifire.exceptions import NoMatchingURLException
from wsgifire.internal_views import error_view

def dispatcher(request, url_seq):
    def parse_url(rel_url):
        for url in url_seq:
            match = re.match(url[0],rel_url)
            if match:
                args = match.groupdict()
                if args:
                    return url[1](request,args)
                return url[1](request)
        raise NoMatchingURLException(rel_url)

    rel_url = request['PATH_INFO'][1:]
    try:
        return parse_url(rel_url)
    except NoMatchingURLException as error:
        dispatch_error = error
        if rel_url and rel_url[-1] != r'/':
            try:
                return parse_url("".join([rel_url,r'/']))
            except NoMatchingURLException as error:
                dispatch_error = error
    if settings.DEBUG:
        return error_view(request,dispatch_error)
    
    func = settings.VIEW_404.split('.')[-1]
    mod_name = ".".join(settings.VIEW_404.split('.')[:-1])
    mod = __import__(mod_name,fromlist=[func])
    return getattr(mod,func)(request)