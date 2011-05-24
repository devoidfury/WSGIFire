from wsgiref.simple_server import make_server
from wsgifire.core.http import wsgi_application_handler

def runserver(wsgi_application_handler=wsgi_application_handler):
    httpd = make_server('', 8000, wsgi_application_handler)
    print("Serving on port 8000...")

    # Serve until process is killed
    httpd.serve_forever()
