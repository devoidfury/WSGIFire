
URLS = (
    (r'^$', 'project.views.landing'),
    (r'^test/$', 'wsgifire.internal_views.list_request'),
    (r'^error-test/$', 'fake.fake.fake'),

    (r'^jinja2/$', 'project.template_engines.jinja2_views.home'),
    (r'^jinja2/add_get/$', 'project.template_engines.jinja2_views.add_numbers_get'),
    (r'^jinja2/add_post/$', 'project.template_engines.jinja2_views.add_numbers_post'),

    (r'^mako/$', 'project.template_engines.mako_views.home'),
    (r'^mako/add_get/$', 'project.template_engines.mako_views.add_numbers_get'),
    (r'^mako/add_post/$', 'project.template_engines.mako_views.add_numbers_post'),
)

DEBUG = True

URLS += (
    (r'^.*\.[ico|jpg|png|js|css|gif|svg|jpeg]', 'wsgifire.internal_views.static'),
)

TEMPLATE_DIRS = ['./templates']

MEDIA_DIRECTORY = './media'
