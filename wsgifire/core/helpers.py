from wsgifire.core.http import Response

def redirect(location):
    """
    Return a `Response` with temporary redirect code (302) and forward to `location`.
    """
    response = Response()
    response.status_code = 302
    response.headers['Location'] = location
    return response

def permanent_redirect(location):
    """
    Return a `Response` with permanent redirect code (301) and forward to `location`.
    """
    response = Response()
    response.status_code = 301
    response.headers['Location'] = location
    return response
