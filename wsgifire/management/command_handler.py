import argparse
from wsgifire.execution_handlers.helpers import setup_environ

def command_handler(settings):
    """
    Handles commands from manage.py.
    Currently only runserver command supported, which runs a
    local simple http server serving the project for development.
    """
    parser = argparse.ArgumentParser(description='WSGIFire management tool.')
    parser.add_argument('runserver', help='Run the integrated development server.')

    args = parser.parse_args()
    if 'runserver' in args:
        setup_environ(settings)
        from wsgifire.server.devserver import runserver
        runserver()
    else:
        parser.print_help()
