"""
WSGIFire default settings, always imported first in projects and then
(most optionally) overridden by project settings.
"""

# Main setting. Overwrite URLS to determine project's behavior.
# It's expecting a tuple of two-tuples. ((url_regex, full dotted path to view_function),...)
URLS = (
    (r'^$', 'wsgifire.internal_views.it_worked'),
)

# If True, show debugging view when something breaks, else show
# standard error pages.
DEBUG = False

# Default error view. Set this in your project's settings
# to use a different debugging error view.
DEBUG_ERROR_VIEW = 'wsgifire.middleware.debug_view.error'

# Default error views.
VIEW_404 = 'wsgifire.internal_views.error404'
VIEW_500 = 'wsgifire.internal_views.error500'
