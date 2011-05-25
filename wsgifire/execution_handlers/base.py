from wsgifire.core.http import Request
from wsgifire.dispatcher import dispatcher
from wsgifire.settings import settings

def wsgi_application_handler(environ, start_response):
    request = Request(environ)
    view_function, view_args = dispatcher(request,settings.URLS)

    if view_args:
        response = view_function(request,view_args)
    else:
        response = view_function(request)
    response.callback = start_response

    return response.send_response()
