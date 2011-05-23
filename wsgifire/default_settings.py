def it_worked(request):
    return "It worked!"

URLS = (
    (r'^$', it_worked),
)

DEBUG = False
VIEW_404 = 'wsgifire.internal_views.Error404'