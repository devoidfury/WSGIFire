import traceback
def error_view(request,error):
    items = ['%s: %s' % (key, value) for key, value in sorted(request.items())]

    error_tb = traceback.extract_tb(error.__traceback__, 20)
    formatted_tb = []
    for line in error_tb:
        formatted_tb.append("".join(["In ",line[0].rjust(10)," line ",str(line[1])," in ",line[2],":\n",line[3]]))
    formatted_tb = "\n\n".join(formatted_tb)
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

    response_body = """Error: %s\nTraceback:\n%s\n
The request is \n\n%s\n\nGET:\n%s\n\nPOST:\n%s""" % (error,formatted_tb,"\n".join(items), get, post)
    return response_body

def list_request(request):
    """Test view that prints out the environ"""
    items = ['%s: %s' % (key, value) for key, value in sorted(request.items())]

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

    response_body = 'The request is \n\n%s\n\nGET:\n%s\n\nPOST:\n%s' % ("\n".join(items), get, post)
    return response_body

def error404(request):
    return "404 Error: the page you requested does not exist."
