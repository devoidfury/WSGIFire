from wsgifire.core.http import Request, Response
from wsgifire.dispatcher import dispatcher
from wsgifire.settings import settings

def wsgi_application_handler(environ, start_response):
    request = Request(environ)
    object, view_args = dispatcher(request,settings.URLS)

    if isinstance(object, Response):
        response = object
    else:
        if view_args:
            response = object(request,view_args)
        else:
            response = object(request)
    response.callback = start_response

    return response.send_response()
