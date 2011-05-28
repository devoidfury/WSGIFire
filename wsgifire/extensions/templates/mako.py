from io import StringIO
from wsgifire.settings import settings

from mako.template import Template
from mako.lookup import TemplateLookup
from mako.runtime import Context

if settings.TEMP_DIRECTORY:
    mako_lookup = TemplateLookup(directories=settings.TEMPLATE_DIRS,
                                 module_directory=settings.TEMP_DIRECTORY)
else:
    mako_lookup = TemplateLookup(directories=settings.TEMPLATE_DIRS)

def render_template(template_path, data):
    template = mako_lookup.get_template(template_path)
    return template.render_unicode(**data)