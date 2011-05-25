import traceback
def error(settings,environ,error):
    """Debug view that prints out the error and request environ."""
    formatted_environ = ['%s: %s<br>' % (key, value) for key, value in sorted(environ.items())]

    settings = vars(settings).copy()
    cleaned_settings = dict()
    for key, value in settings.items():
        if not key.startswith('__'):
            cleaned_settings[key] = value

    formatted_settings = ['%s: %s<br>' % (key, value) for key, value in sorted(cleaned_settings.items())]

    error_tb = traceback.extract_tb(error.__traceback__, 20)
    formatted_tb = []
    for line in error_tb:
        formatted_tb.append("".join(
            ["<p>In <em>",line[0],"</em> line <strong>",str(line[1]),"</strong> in <em>",
                line[2],"</em>:<br>",line[3],"</p>"]))
    formatted_tb = "".join(formatted_tb)

    response_body = """
<html>
<head><title>WSGIFire Debug Error</title></head>
<body>
<h1>Error: %(error)s</h1>
<p>Set <em>DEBUG = False</em> in your settings file to receive normal errors.</p>
<h3>Traceback:</h3>
%(traceback)s
<h4>Settings:</h4>
<div>%(str_settings)s</div>
<h4>The request is</h4>
<div>%(request)s</div>
</body>
</html>""" % {'error': repr(error),'traceback':formatted_tb,'str_settings':"\n".join(formatted_settings),
              'request':"\n".join(formatted_environ)}
    return response_body
