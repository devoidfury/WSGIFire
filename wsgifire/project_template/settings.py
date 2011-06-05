

# Add patterns to this setting in order to
# define the behavior of the application.
# each entry needs to be a tuple, in the
# format of (<regex pattern>, <dotted path to view>)
URLS = (
    (r'^$', 'myproject.views.example'),
)

# If True, show debugging view when something breaks, else show
# standard error pages.
# This should be turned off in production.
DEBUG = True

# If you're using a template engine such as Jinja or Mako,
# this setting should be a list of paths to your
# template directories.
#
#TEMPLATE_DIRS = ['./templates']
