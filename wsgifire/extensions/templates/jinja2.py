
from jinja2 import Environment, FileSystemLoader, BytecodeCache
from wsgifire.settings import settings

env = Environment(loader=FileSystemLoader(settings.TEMPLATE_DIRS))

def render_template(template_path, data):
    template = env.get_template(template_path)
    if data:
        return template.render(**data)
    return template.render()
