
def error_view(request,error):
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

    response_body = """Error: %s\nThe request is \n\n%s\n\nGET:\n%s\n\nPOST:\n%s""" % (error,"\n".join(items), get, post)
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
