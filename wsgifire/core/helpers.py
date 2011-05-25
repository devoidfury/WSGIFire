from wsgifire.core.http import Response

def redirect(location):
    response = Response()
    response.status_code = 302
    response.headers['Location'] = location
    return response

def permanent_redirect(location):
    response = Response()
    response.status_code = 301
    response.headers['Location'] = location
    return response
