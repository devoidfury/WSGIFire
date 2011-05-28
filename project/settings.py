
URLS = (
    (r'^$', 'project.views.landing'),
    (r'^test/$', 'wsgifire.internal_views.list_request'),
    (r'^error-test/$', 'fake.fake.fake'),

    (r'^mako/$', 'project.mako_views.mako_home'),
    (r'^mako/add_get/$', 'project.mako_views.add_numbers_get'),
    (r'^mako/add_post/$', 'project.mako_views.add_numbers_post')
)

DEBUG = True

TEMPLATE_DIRS = ['./templates']
