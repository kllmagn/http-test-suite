from urllib.parse import unquote
from . import resp


def handle(conn, document_root):
    rawFile = conn.makefile('r')
    info = rawFile.readline()
    r = resp.RequestParser(info)
    request = r.to_request()
    if request.error == 1:
        resp.response(conn, resp.HttpResponse(400, 'Bad request', resp.badResponseHeaders))
        return
    if request.method not in ['GET', 'HEAD']:
        resp.response(conn, resp.HttpResponse(405, 'Method Not Allowed', resp.badResponseHeaders))
        return
    if request.path.find('../') != -1:
        resp.response(conn, resp.HttpResponse(403, 'Forbidden', resp.badResponseHeaders))
        return
    indexFile = False
    unquotedPath = unquote(request.path)
    if request.path[-1] == '/' and request.path.find('.') == -1:
        filePath = document_root + unquotedPath + 'index.html'
        indexFile = True
    else:
        filePath = document_root + unquotedPath
    try:
        file = open(filePath, 'rb')
    except:
        if indexFile:
            r = resp.HttpResponse(403, 'Forbidden', headers=resp.badResponseHeaders)
        else:
            r = resp.HttpResponse(404, 'Not Found', headers=resp.badResponseHeaders)
        resp.response(conn, r)
        return
    resp.ok(conn, filePath)
    if request.method == 'GET':
        try:
            conn.sendfile(file)
        except BrokenPipeError:
            conn.sendfile(file)
    file.close()
