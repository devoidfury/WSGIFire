from wsgifire.core.decorators import simple_response

@simple_response
def list_request(request):
    """Temporary testing view."""
    items = ['{0}: {1}<br>'.format(key, value) for key, value in sorted(request.items())]

    get = ""
    for key, values in request.GET.items():
        value = ", ".join([v for v in values])
        row = ": ".join([key,value])
        get = "\n".join([get,row])

    post = ""
    for key, values in request.POST.items():
        value = ", ".join([v for v in values])
        row = ": ".join([key,value])
        post = "\n".join([post,row])

    response_body = "The request is \n\n{0}\n\nGET:\n{1}\n\nPOST:\n{2}".format("\n".join(items), get, post)
    return response_body

@simple_response
def error404(request):
    """Basic 404 message."""
    return """<html><head><title>404: Page Not Found</title></head>
    <body><h1>404 Error:</h1><p>The page you requested does not exist.</p>
    </body</html>"""

@simple_response
def error500(request):
    """Basic 500 message."""
    return """<html><head><title>500: Internal Server Error</title></head>
    <body><h1>500 Error:</h1><p>The sever encountered a problem.</p>
    </body</html>"""

@simple_response
def it_worked(request):
    """Basic view to show server is working."""
    return "<html><body><h1>It worked!</h1></body></html>"
