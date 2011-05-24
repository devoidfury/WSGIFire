from wsgifire.core.http import Request, Response
from wsgifire.dispatcher import dispatcher
from wsgifire.settings import settings

def wsgi_application_handler(environ, start_response):
    request = Request(environ)
    response_body = dispatcher(request,settings.URLS)
    response = Response(response_body,request,start_response)
    return response.send_response()
