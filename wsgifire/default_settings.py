# WSGIFire default settings, always imported first in projects and then
# (most optionally) overridden by project settings.

# Basic view to show server is working.
def it_worked(request):
    return "<html><body><h1>It worked!</h1></body></html>"

# Main setting. Overwrite URLS to determine project's behavior.
# It's expecting a tuple of two-tuples. ((url_regex, view_function),...)
URLS = (
    (r'^$', it_worked),
)

# If True, show debugging view when something breaks, else show
# standard error pages.
DEBUG = False

# Default error view. Set this in your project's settings
# to use a different debugging error view.
DEBUG_ERROR_VIEW = 'wsgifire.middleware.debug_view.error'

# Default 404 error view. Set this in your project's settings
# to use a different 404 view.
VIEW_404 = 'wsgifire.internal_views.error404'
