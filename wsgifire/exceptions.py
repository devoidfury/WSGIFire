
class BaseWSGIFireException(Exception):
    """Base exception class for WSGIFire"""
    pass


class NoMatchingURL(BaseWSGIFireException):
    """Dispatcher error, the requested path did not match any of the URLS defined."""
    pass


class ViewFunctionDoesNotExist(BaseWSGIFireException):
    """String to view defined for matching request in URLS does not exist."""
    pass
