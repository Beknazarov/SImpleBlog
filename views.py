# coding: utf-8
from http import HTTPStatus

import settings
from db.database import DataAccessLayer
from system import methodPost, get_cookies
from template_code.template import Template, Templates


def indexPage(request):
    db = DataAccessLayer()
    if get_cookies(request):
        username = get_cookies(request).get('cookie_user')
        status = True
    else:
        username = ""
        status = False

    all_post_html = ""
    for key, value in db.getAllPost().items():
        for k, v in value.items():
            all_post_html += "<div class='post'>"
            all_post_html += "<div class='title'><h2><a class='id' href=/index/post/%s/>%s</a></h2></div>" % (
                k, v[0])
            all_post_html += "<div class='description'>%s</div>" % v[1]
            all_post_html += "<div class='author'>%s</div>" % key
            all_post_html += "<hr />"
            all_post_html += "</div>"
    f = open(settings.TEMPLATES_DIR + '/index.html')
    read = f.read()
    html = Templates(read).render(blog=all_post_html, username=username, status=status)
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def adminPage(request):
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    if get_cookies(request):
        username = get_cookies(request).get('cookie_user')
    else:
        username = "Anonym"
        request.send_header('Location', '/admin/')
    postUserHtml = ""
    postCountOwnUser = db.getCountPostOwnUser(username)
    post = db.getAllPostOwnUser(username)
    if postCountOwnUser <= 0:
        postUserHtml = "<h1>Empty Post </h1>"
    else:
        for key, value in post.items():
            postUserHtml += '<br/>'
            postUserHtml += '<h1>%s </h1>' % key
            postUserHtml += "<h2><div class='title'>%s</div></h2>" % str(value[0])
            postUserHtml += '<a href=/admin/edit/blog/%s/> Update </a><br/>' % key
            postUserHtml += '<a href=/admin/delete/blog/%s/> Delete </a><br/><br/>' % key
            postUserHtml += "<div class='description'>%s</div>" % (value[1])
            postUserHtml += "<hr />"
    f = open(settings.TEMPLATES_DIR + '/admin_post.html')
    read = f.read()
    html = Templates(read).render(username=username, post=postUserHtml)

    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def createPostPage(request):
    context = {}
    request.send_response(HTTPStatus.SEE_OTHER)
    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    html = Template('create_post.html', context).render()
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def createPostMethodPost(request):
    context = {}
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    html = Template('create_post.html', context).render()
    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    postAttribute = methodPost(request)
    title = postAttribute.get('title')
    description = postAttribute.get('description')
    username = get_cookies(request).get('cookie_user')
    begin_blog_length = int(db.countPost())
    db.createPost(username, title, description)
    end_blog_length = int(db.countPost())
    if end_blog_length > begin_blog_length:
        request.send_header('Location', '/admin/blog/')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def updatePost(request):
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    edit_post_html = ""
    username = get_cookies(request).get('cookie_user')
    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    else:
        post_id = int(request.path.split('/')[-2])
        if not db.isPostExist(post_id):
            request.send_header('Location', '/error/')
        if not db.isPostInUser(username, post_id):
            request.send_header('Location', '/error/')
        else:
            post = db.getPostById(post_id)
            edit_post_html += "<form action='/admin/update/' method='post'>"
            edit_post_html += "<input type='hidden' value='%s' name='hiddenid'/><br/>" % post_id
            edit_post_html += "<input type='text' value='%s' name='title'/><br/>" % post[0]
            edit_post_html += "<textarea cols='50' rows='10' id='description' name='description'>%s</textarea> <br/>" % \
                              post[1]
            edit_post_html += "<input type='submit' value='Update' />"
            edit_post_html += "</form>"
    f = open(settings.TEMPLATES_DIR + '/update_post.html')
    read = f.read()
    html = Templates(read).render(post_edit=edit_post_html)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def updateMethodPost(request):
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    post_attribute = methodPost(request)
    id = post_attribute.get('hiddenid')
    title = post_attribute.get('title')
    description = post_attribute.get('description')
    username = get_cookies(request).get('cookie_user')
    db.updatePost(int(id), username, title, description)
    request.send_header('Content-Type', 'text/html')
    request.send_header('Location', '/admin/blog/')
    request.end_headers()
    return request


def postDetail(request):
    db = DataAccessLayer()
    id = request.path.replace(' ', '').split('/')[3]
    request.send_response(HTTPStatus.OK)
    post = db.getPostById(int(id))
    print(id)
    f = open(settings.TEMPLATES_DIR + '/detail_post.html')
    read = f.read()

    post_html = '<br/>'
    post_html += "<div class='title'>%s</div><br/>" % post[0]
    post_html += "<div class='description'>%s</div><br/>" % post[1]
    # post_html += "<div class='author'>%s</div><br/>" % (get_cookies(request).get('cookie_user'))
    post_html += "<hr />"

    html = Templates(read).render(detail_blog_id=post_html)
    request.send_header('Content-Type', 'text/html')

    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def deletePost(request):
    id = request.path.split('/')[-2]
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    if not db.isPostInUser(get_cookies(request).get('cookie_user'), id):
        request.send_header('Location', '/error/')
    else:
        db.deletePostById(int(id))
        request.send_header('Location', '/admin/blog/')
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    return request


def login(request):
    context = {"error": ""}
    html = Template('login.html', context).render()
    request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
    if get_cookies(request):
        request.send_header('Location', '/admin/blog/')
    else:
        request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def loginMethodPost(request):
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)

    userAttribute = methodPost(request)
    username = userAttribute.get('username')
    # password = userAttribute.get('password')

    context = {"error": ""}
    if db.isUserExist(username):
        request.send_header('Set-Cookie', 'cookie_user=%s;path=/;' % username)
        request.send_header('Location', '/admin/blog/')
        print("Login Success")
    else:
        request.send_header('Content-Type', 'text/html')
        context["error"] = "Ошибка авторизации"
        print("Login Error")
    request.end_headers()
    html = Template('login.html', context).render()
    request.wfile.write(str.encode(html))

    return request


def register(request):
    context = {'title': 'Регистрация'}
    html = Template('register.html', context).render()
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def registerMethodPost(request):
    context = {'title': 'Регистрация'}
    db = DataAccessLayer()

    request.send_response(HTTPStatus.OK)
    html = Template('register.html', context).render()
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    userAttribute = methodPost(request)
    username = userAttribute.get('username')
    password = userAttribute.get('password')
    email = userAttribute.get('email')
    if not db.isUserExist(username):
        db.createUser(username, password, email)
        print("Create success new login")
    else:
        print("Login don't register")
    return request


def logout(request):
    request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
    if get_cookies(request).get('cookie_user'):
        request.send_header("Set-Cookie", "cookie_user=0;path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT")
        request.send_header('Location', '/admin/')

    else:
        request.send_header('Content-Type', 'text/html')

    request.end_headers()


def handle_404(request):
    context = {'not-found': 'File Not found'}
    html = Template('404.html', context).render()
    request.send_response(HTTPStatus.NOT_FOUND)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))

    return request


def error(request):
    context = {}
    html = Template('error.html', context).render()
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
