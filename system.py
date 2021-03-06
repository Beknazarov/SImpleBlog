import cgi

import settings


def method_POST(request):
    ctype, pdict = cgi.parse_header(request.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(request.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(request.headers['content-length'])
        postvars = cgi.parse_qs(request.rfile.read(length), keep_blank_values=1)

    else:
        postvars = {}
    model_attr = dict()
    if len(postvars):
        for key, value in postvars.items():
            model_attr[key.decode("utf-8")] = value[0].decode("utf-8")
    return model_attr


def set_cookie(request, key, value):
    request.send_header('Set-Cookie', key + '=%s;path=/;' % value)


def set_clear_cookie(request):
    expires = "cookie_username=0;path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"
    request.send_header("Set-Cookie", expires)


def get_cookies(request):
    res = {}
    cookie = (request.headers.get_all('Cookie', failobj={}))
    if len(cookie) > 0:
        for i in cookie[0].split(';'):
            res[(i.strip().split('='))[0]] = i.strip().split('=')[1]
    return res


def static(request):
    try:
        sendReply = False
        if request.path.endswith(".jpg"):
            mimetype = 'image/jpg'
            sendReply = True
        if request.path.endswith(".gif"):
            mimetype = 'image/gif'
            sendReply = True
        if request.path.endswith(".png"):
            mimetype = 'image/png'
            sendReply = True
        if request.path.endswith(".js"):
            mimetype = 'application/javascript'
            sendReply = True
        if request.path.endswith(".css"):
            mimetype = 'text/css'
            sendReply = True

        if sendReply:
            file_path = (settings.STATIC_DIR[:-7] + request.path)
            request.send_response(200)
            request.send_header('Content-type', mimetype)
            if request.path.endswith('.jpg') or \
                    request.path.endswith('.jpeg') or \
                    request.path.endswith('.gif') or \
                    request.path.endswith('.png'):
                def load_binary(file):
                    with open(file, 'rb') as file:
                        return file.read()

                read = load_binary(file_path)
                request.wfile.write(bytes(read))
            else:
                f = open(file_path)
                read = f.read()
                request.end_headers()
                request.wfile.write(bytes(read, 'utf-8'))
                f.close()
            return
    except IOError:
        request.send_error(404, 'File Not Found: %s' % request.path)
