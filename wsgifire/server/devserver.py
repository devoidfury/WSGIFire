from wsgiref.simple_server import make_server
from wsgifire.middleware.debug_error import DebugMiddleware
from wsgifire.execution_handlers.base import wsgi_application_handler

def runserver(wsgi_application_handler=wsgi_application_handler,middleware=None):
    wrapped_app = DebugMiddleware(wsgi_application_handler)
    if middleware:
        for item in middleware:
            wrapped_app = item(wrapped_app)

    httpd = make_server('', 8000, wrapped_app)
    print("Serving on port 8000...")

    # Serve until process is killed
    httpd.serve_forever()
