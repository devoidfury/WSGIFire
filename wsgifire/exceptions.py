
class BaseWSGIFireException(Exception):
    """Base exception class for WSGIFire"""
    pass


class NoMatchingURLException(BaseWSGIFireException):
    """Dispatcher error, the requested path did not match any of the URLS defined."""
    pass
