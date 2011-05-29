from wsgifire.core.decorators import simple_response
from wsgifire.extensions.templates.mako import render_template

@simple_response
def home(request):
    """Small demo using mako templating."""
    return render_template("mako/home.html",None)

@simple_response
def add_numbers_get(request):
    """Basic view that adds two numbers inputed by user."""
    if request.GET:
        first = int(request.GET['number1'][0])
        second = int(request.GET['number2'][0])
        if first and second:
            value = first + second
            response_body = '<html>\n<head>\n\t<title>Numbers summed</title>\n</head>\n'
            response_body += '<body>\n\t<h1>' + str(value) + '</h1>\n</body>\n</html>'
        else:
            response_body = '<html>\n<head>\n\t<title>Invalid Input</title>\n</head>\n'
            response_body += '<body>\n\t<h1>Invalid Input</h1>\n</body>\n</html>'
    else:
        response_body = '<html>\n<head>\n\t<title>Add numbers</title>\n</head>\n'
        response_body += '<body>\n\t<form method="get" action="">\n'
        response_body += '\t\t<input name="number1" type="text" /><input name="number2" type="text" />\n'
        response_body += '\t\t<input type="submit" />\n'
        response_body += '\t</form>\n</body>\n</html>'
    return response_body

@simple_response
def add_numbers_post(request):
    """
    Basic view that adds two numbers input by user.
    Small demo of using forms to POST data and mako templating.
    """
    value = 0
    message = ''
    if request.POST:
        first = int(request.POST.get('number1',[''])[0])
        second = int(request.POST.get('number2',[''])[0])
        value = first + second
        
    data = dict(value=value,message=message)
    return render_template("mako/add_numbers_post.html",data)
