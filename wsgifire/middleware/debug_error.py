from wsgifire.exceptions import NoMatchingURL
from wsgifire.settings import settings
from wsgifire.helpers import func_from_str

class DebugMiddleware(object):
    """Debug middleware that catches errors from wsgifire."""
    # TODO: Needs some lovin'.
    def __call__(self,environ, start_response):
        try:
            return self._wrapped(environ,start_response)
        except Exception as error_instance:
            if isinstance(error_instance,NoMatchingURL):
                status = '404 NOT FOUND'
                standard_error = settings.VIEW_404
            else:
                status = '500 INTERNAL SERVER ERROR'
                standard_error = settings.VIEW_500

            response_headers = [('Content-type','text/html')]
            start_response(status, response_headers)

            if settings.DEBUG:
                return [func_from_str(settings.DEBUG_ERROR_VIEW)(settings, environ, error_instance).encode('latin-1')]
            return [func_from_str(standard_error)(None).encode('latin-1')]

    def __init__(self,application):
        self._wrapped = application
