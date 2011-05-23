def it_worked(request):
    return "It worked!"

URLS = (
    (r'^$', it_worked),
)

DEBUG = False
DEBUG_ERROR_VIEW = 'wsgifire.internal_views.error_view'
VIEW_404 = 'wsgifire.internal_views.error404'
