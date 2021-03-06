from functools import wraps
from wsgifire.core.http import Response

def simple_response(view_func):
    """
    Decorator to wrap view functions if a standard `Response` instance is adequate.
    The view wrapped with this will only need to return a string instead of an entire `Response` instance.
    """
    def _response(request,*args,**kwargs):
        response_body = view_func(request,*args,**kwargs)
        return Response(response_body)
    return wraps(view_func)(_response)
