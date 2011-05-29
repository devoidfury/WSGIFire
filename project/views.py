from wsgifire.core.decorators import simple_response

@simple_response
def landing(request):
    return """
<html>
<head><title>WSGIFire Example</title></head>
<body>
<h1>It worked!</h1>
<p>This is an example WSGIFire project.</p>
<h3>Check out other parts of the example:</h3>
<ul>
    <li><a href="/jinja2/">WSGIFire using Jinja2 templates</a></li>
    <li><a href="/mako/">WSGIFire using Mako templates</a></li>
    <li>
        <a href="/fake/">Example of a bad URL request.</a>
        <br>Try this with settings.DEBUG=True to get a traceback, or settings.DEBUG=False to get a 404 page.
    </li>
    <li>
        <a href="/error-test/">Example of a good URL request with a bad view function reference.</a>
        <br>Try this with settings.DEBUG=True to get a traceback, or settings.DEBUG=False to get a 500 page.
    </li>
</ul>

</body></html>"""
