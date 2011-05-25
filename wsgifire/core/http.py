from collections import UserDict
from cgi import parse_qs, escape

# Status code dict from Django
# See http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
STATUS_CODE_TEXT = {
    100: 'CONTINUE',
    101: 'SWITCHING PROTOCOLS',
    200: 'OK',
    201: 'CREATED',
    202: 'ACCEPTED',
    203: 'NON-AUTHORITATIVE INFORMATION',
    204: 'NO CONTENT',
    205: 'RESET CONTENT',
    206: 'PARTIAL CONTENT',
    300: 'MULTIPLE CHOICES',
    301: 'MOVED PERMANENTLY',
    302: 'FOUND',
    303: 'SEE OTHER',
    304: 'NOT MODIFIED',
    305: 'USE PROXY',
    306: 'RESERVED',
    307: 'TEMPORARY REDIRECT',
    400: 'BAD REQUEST',
    401: 'UNAUTHORIZED',
    402: 'PAYMENT REQUIRED',
    403: 'FORBIDDEN',
    404: 'NOT FOUND',
    405: 'METHOD NOT ALLOWED',
    406: 'NOT ACCEPTABLE',
    407: 'PROXY AUTHENTICATION REQUIRED',
    408: 'REQUEST TIMEOUT',
    409: 'CONFLICT',
    410: 'GONE',
    411: 'LENGTH REQUIRED',
    412: 'PRECONDITION FAILED',
    413: 'REQUEST ENTITY TOO LARGE',
    414: 'REQUEST-URI TOO LONG',
    415: 'UNSUPPORTED MEDIA TYPE',
    416: 'REQUESTED RANGE NOT SATISFIABLE',
    417: 'EXPECTATION FAILED',
    500: 'INTERNAL SERVER ERROR',
    501: 'NOT IMPLEMENTED',
    502: 'BAD GATEWAY',
    503: 'SERVICE UNAVAILABLE',
    504: 'GATEWAY TIMEOUT',
    505: 'HTTP VERSION NOT SUPPORTED',
}


class Request(UserDict):
    """Wrapper class for the wsgi environ dict"""
    def __init__(self,environ):
        super().__init__(environ)

        # Cleans and sets GET and POST dicts from request.QUERY_STRING. Also escapes user input to avoid script
        # injection, see http://webpython.codepoint.net/wsgi_request_parsing_get
        dirty_qs = parse_qs(self.get('QUERY_STRING'))
        self.GET = self._clean_get(dirty_qs)

        # the environment variable CONTENT_LENGTH may be empty or missing
        try:
            request_body_size = int(self.get('CONTENT_LENGTH', 0))
        except ValueError:
            request_body_size = 0
        request_body = self['wsgi.input'].read(request_body_size)
        dirty_qs = parse_qs(request_body)
        self.POST = self._clean_post(dirty_qs)

    @staticmethod
    def _clean_get(dirty_qs):
        clean_qs = {}
        for key, values in dirty_qs.items():
            clean_qs[key] = [escape(v) for v in values]
        return dict((k,clean_qs[k]) for k in clean_qs)

    @staticmethod
    def _clean_post(dirty_qs):
        clean_qs = {}
        for key, values in dirty_qs.items():
            clean_qs[str(key,'utf-8')] = [escape(str(v,'utf-8')) for v in values]
        return dict((k,clean_qs[k]) for k in clean_qs)


class Response(object):
    # HTTP response code and message
    status_code = 200
    _status = " ".join([str(status_code),STATUS_CODE_TEXT[200]])
    headers = {'Content-Type': 'text/html'}
    callback = None

    def __init__(self,body,request):
        self.body = body
        self.request = request

    # These are HTTP headers expected by the client.
    # They must be wrapped as a list of tupled pairs:
    # [(Header name, Header value)]
    @property
    def get_final_headers(self):
        self.headers['Content-Length'] = str(len(self.body))
        return [(key,self.headers[key]) for key in self.headers]


    def send_response(self):
        self.callback(self._status, self.get_final_headers)
        return [self.body.encode('latin-1')]
