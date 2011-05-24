import traceback
def error(request,error):
    items = ['%s: %s<br>' % (key, value) for key, value in sorted(request.items())]

    error_tb = traceback.extract_tb(error.__traceback__, 20)
    formatted_tb = []
    for line in error_tb:
        formatted_tb.append("".join(
            ["<p>In <em>",line[0],"</em> line <strong>",str(line[1]),"</strong> in <em>",
                line[2],"</em>:<br>",line[3],"</p>"]))
    formatted_tb = "".join(formatted_tb)
    get = ""
    for key, values in request.GET.items():
        value = ", ".join([v for v in values])
        row = "".join(["<p>",": ".join([key,value]),"</p>"])
        get = "".join([get,row])

    post = ""
    for key, values in request.POST.items():
        value = ", ".join([v for v in values])
        row = "".join(["<p>",": ".join([key,value]),"</p>"])
        post = "".join([post,row])

    response_body = """
<html>
<head><title>WSGIFire Debug Error</title></head>
<body>
<h1>Error: %(error)s</h1>
<p>Set <em>DEBUG = False</em> in your settings file to receive normal errors.</p>
<h3>Traceback:</h3>
%(traceback)s
<h3>The request is</h3>
<div>%(request)s</div>
GET:<br>%(get)s<br>POST:<br>%(post)s
</body>
</html>""" % {'error': repr(error),'traceback':formatted_tb,'request':
        "\n".join(items), 'get': get, 'post': post}
    return response_body