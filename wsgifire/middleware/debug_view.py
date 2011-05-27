import traceback
def error(settings,environ,error):
    """Debug view that prints out the error and request environ."""
    formatted_environ = ['{0}: {1}<br>'.format(key, value) for key, value in sorted(environ.items())]

    settings = vars(settings).copy()
    cleaned_settings = dict()
    for key, value in settings.items():
        if not key.startswith('__'):
            cleaned_settings[key] = value

    formatted_settings = ['{0}: {1}<br>'.format(key, value) for key, value in sorted(cleaned_settings.items())]

    error_tb = traceback.extract_tb(error.__traceback__, 20)
    formatted_tb = []
    for line in error_tb:
        formatted_tb.append("""
            <p>In <em>{file}</em> line <strong>{line}</strong> in <em>{object}</em>:
            <br>{trace_line}</p>""".format(
                 file=line[0],
                 line=line[1],
                 object=line[2],
                 trace_line=line[3])
            )
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
