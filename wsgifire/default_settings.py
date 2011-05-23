def it_worked(request):
    return "It worked!"

URLS = (
    (r'^$', it_worked),
)
