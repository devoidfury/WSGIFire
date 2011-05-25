import re
from wsgifire.helpers import func_from_str
from wsgifire.exceptions import NoMatchingURL, ViewFunctionDoesNotExist

def dispatcher(request, url_seq):
    def parse_url(rel_url):
        for url in url_seq:
            match = re.match(url[0],rel_url)
            if match:
                args = match.groupdict()
                try:
                    return_view = func_from_str(url[1])
                except (AttributeError, ImportError) as error_instance:
                    # If there is an import error or attribute error, the function probably
                    # doesn't exist.
                    view_error = ViewFunctionDoesNotExist(url[0],url[1])
                    view_error.with_traceback(error_instance.__traceback__)
                    raise view_error
                else:
                    if args:
                        return return_view(request,args)
                    return return_view(request)
        raise NoMatchingURL(rel_url)

    rel_url = request['PATH_INFO'][1:]
    try:
        return parse_url(rel_url)
    except NoMatchingURL:
        if rel_url and rel_url[-1] != r'/':
            try:
                return parse_url("".join([rel_url,r'/']))
            except NoMatchingURL:
                pass
        raise NoMatchingURL(rel_url)
