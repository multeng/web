def app(environ, start_response):
	start_response('200 ok',['Content-type', 'text/plain'])
	body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
	return body