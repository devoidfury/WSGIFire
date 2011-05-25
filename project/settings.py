
URLS = (
    (r'^test/$', 'wsgifire.internal_views.list_request'),
    (r'^error-test/$', 'fake.fake.fake'),
    (r'^$', 'project.views.add_numbers')
)

DEBUG = True
