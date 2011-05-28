
URLS = (
    (r'^test/$', 'wsgifire.internal_views.list_request'),
    (r'^error-test/$', 'fake.fake.fake'),
    (r'^add_numbers_get/$', 'project.views.add_numbers_get'),
    (r'^add_numbers_post/$', 'project.views.add_numbers_post')
)

DEBUG = True

TEMPLATE_DIRS = ['./templates']