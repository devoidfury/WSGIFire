import re
from wsgifire.helpers import func_from_str
from wsgifire.exceptions import NoMatchingURL, ViewFunctionDoesNotExist

def dispatcher(request, url_seq):
    """Match the requested url against patterns defined in settings.URLS, and return the view function.
    Using this we can easily abstract URLs from project/filesystem layout.
    """
    def parse_url(rel_url):
        for url in url_seq:
            match = re.match(url[0],rel_url)
            if match:
                # using 'args' to pull named groups from the url and passing them to the view, if any.
                args = match.groupdict()
                try:
                    return_view = func_from_str(url[1])
                except (AttributeError, ImportError) as error_instance:
                    # If there is an import error or attribute error, the function probably
                    # doesn't exist, throw our own appropriate error
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
        # If the path didn't match and the path doesn't end in a slash (excluding GET params),
        # try to match it again appending a slash.
        if rel_url and rel_url[-1] != r'/':
            try:
                return parse_url("".join([rel_url,r'/']))
            except NoMatchingURL:
                pass
        raise NoMatchingURL(rel_url)
