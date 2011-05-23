from wsgifire.internal_views import list_request

URLS = (
    (r'^test/$', list_request),
    (r'^testing2/$', list_request)
)

DEBUG = True
