
class BaseWSGIFireException(Exception):
    """Base exception class for WSGIFire."""
    pass


class NoMatchingURL(BaseWSGIFireException):
    """Dispatcher error, the requested path did not match any of the URLS defined in settings."""
    pass


class ViewFunctionDoesNotExist(BaseWSGIFireException):
    """String for view defined in matching request in URLS does not exist."""
    pass
