# coding: utf-8
from http import HTTPStatus

import settings
from db.database import DataAccessLayer, Blog
from template_code.template import Template, post, Templates


def index_blog(request):
    db = DataAccessLayer()
    blog_count = len(Blog.id)
    if get_cookies(request):
        username = get_cookies(request).get('cookie_user')
        status = True
    else:
        username = ""
        status = False

    all_post_html = ""
    for i in range(0, blog_count):
        all_post_html += "<div class='post'>"
        all_post_html += "<div class='title'><h2><a class='id' href=/index/post/%s/>%s</a></h2></div>" % (
            str(db.getAllPost().id[i]), db.getAllPost().title[i])
        all_post_html += "<div class='description'>%s</div>" % (db.getAllPost().description[i])
        all_post_html += "<div class='like'>%s</div>" % (str(db.getAllPost().like[i]))
        all_post_html += "<div class='author'>%s</div>" % (str(db.getAllPost().author[i]))
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


def admin_blog_view(request):
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    if get_cookies(request):
        username = get_cookies(request).get('cookie_user')
    else:
        username = "Anonym"
        request.send_header('Location', '/admin/')
    all_post_html = ""
    blog_count = db.getCountFilterAuthor(username)
    id, title, description, like = db.GetPostFilterByUsername(username)
    if blog_count <= 0:
        all_post_html = "<h1>Empty Post </h1>"
    else:
        for i in range(0, int(blog_count)):
            all_post_html += '<br/>'
            all_post_html += "<h2><div class='title'>%s</div></h2>" % str(title[i])
            all_post_html += '<a href=/admin/edit/blog/%s/> Update </a><br/>' % str(id[i])
            all_post_html += '<a href=/admin/delete/blog/%s/> Delete </a><br/><br/>' % str(id[i])
            all_post_html += "<div class='description'>%s</div>" % (description[i])
            all_post_html += "<div class='like'>%s</div>" % (str(like[i]))
            all_post_html += "<hr />"
    f = open(settings.TEMPLATES_DIR + '/admin_post.html')
    read = f.read()
    html = Templates(read).render(user_list=db.getUserName(), username=username, blog=all_post_html)

    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def admin_edit_post(request):
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    edit_post_html = ""
    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    else:
        id = request.path.split('/')[-2]
        if not db.CheckUserPost(get_cookies(request).get('cookie_user'), id):
            request.send_header('Location', '/error/')
        else:
            title, description, like = db.EditPostById(int(id))
            edit_post_html += "<form action='/admin/update/' method='post'>"
            edit_post_html += "<input type='hidden' value='%s' name='hiddenid'/><br/>" % id
            edit_post_html += "<input type='text' value='%s' name='title'/><br/>" % title
            edit_post_html += "<textarea cols='50' rows='10' id='description' name='description'>%s</textarea> <br/>" % description
            edit_post_html += "<input type='number' name='like' value='%s' /> <br/>" % like
            edit_post_html += "<input type='submit' value='Update' />"
            edit_post_html += "</form>"
    f = open(settings.TEMPLATES_DIR + '/update_post.html')
    read = f.read()
    html = Templates(read).render(post_edit=edit_post_html)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def admin_update_post_method(request):
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    post_attribute = post(request)
    id = post_attribute.get('hiddenid')
    title = post_attribute.get('title')
    description = post_attribute.get('description')
    like = post_attribute.get('like')

    db.updatePostById(id, title, description, like)
    all_post_html = ""
    username = get_cookies(request).get('cookie_user')
    blog_count = db.getCountFilterAuthor(username)
    id, title, description, like = db.GetPostFilterByUsername(username)
    if blog_count <= 0:
        all_post_html = "<h1>Empty Post </h1>"
    else:
        for i in range(0, int(blog_count)):
            all_post_html += '<br/>'
            all_post_html += "<h2><a class='id' href=%s/>%s</a></h2>" % (
                str(id[i]), title[i])
            all_post_html += '<a href=/admin/edit/blog/%s/> Update </a><br/>' % str(id[i])
            all_post_html += '<a href=/admin/delete/blog/%s/> Delete </a><br/><br/>' % str(id[i])
            all_post_html += "<div class='description'>%s</div>" % (description[i])
            all_post_html += "<div class='like'>%s</div>" % (str(like[i]))
            all_post_html += "<hr />"
    f = open(settings.TEMPLATES_DIR + '/admin_post.html')
    read = f.read()
    html = Templates(read).render(username=get_cookies(request).get('cookie_user'), blog=all_post_html)
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.send_header('Location', '/admin/blog/')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def index_blog_detail(request):
    db = DataAccessLayer()

    id = request.path.replace(' ', '').split('/')[3]
    request.send_response(HTTPStatus.OK)
    blog_by_id = db.GetPostIndexById(int(id))
    post_in_blog = blog_by_id.split("/")
    f = open(settings.TEMPLATES_DIR + '/detail_post.html')
    read = f.read()

    post_html = '<br/>'
    post_html += "<div class='title'>%s</div><br/>" % (post_in_blog[0])
    post_html += "<div class='description'>%s</div><br/>" % (post_in_blog[1])
    post_html += "<div class='like'>%s</div><br/>" % (post_in_blog[2])
    post_html += "<div class='author'>%s</div><br/>" % (post_in_blog[3])
    post_html += "<hr />"

    html = Templates(read).render(detail_blog_id=post_html)
    request.send_header('Content-Type', 'text/html')

    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def admin_detail_post(request):
    db = DataAccessLayer()

    id = request.path.replace(' ', '').split('/')[2]
    blog_by_id = db.GetPostById(int(id))
    f = open(settings.TEMPLATES_DIR + '/detail_post.html')
    read = f.read()
    html = Templates(read).render(detail_blog_id=blog_by_id)
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def admin_create_post(request):
    context = {}
    request.send_response(HTTPStatus.SEE_OTHER)
    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    html = Template('create_post.html', context).render()
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def admin_delete_post(request):
    id = request.path.split('/')[-2]
    db = DataAccessLayer()
    request.send_response(HTTPStatus.SEE_OTHER)
    if not db.CheckUserPost(get_cookies(request).get('cookie_user'), id):
        request.send_header('Location', '/error/')
    else:
        db.deletePostById(int(id))
        request.send_header('Location', '/admin/blog/')
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    return request


def admin_create_blog_method_post(request):
    context = {}
    id = 0
    db = DataAccessLayer()
    html = Template('create_post.html', context).render()
    request.send_response(HTTPStatus.SEE_OTHER)
    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    blog_attribute = post(request)
    # id = blog_attribute.get('id')
    title = blog_attribute.get('title')
    description = blog_attribute.get('description')
    like = blog_attribute.get('like')
    begin_blog_length = len(db.getTitlePost())
    db.CreatePost(db.auto_increment(id), title, description, like, get_cookies(request).get('cookie_user'))
    end_blog_length = len(db.getTitlePost())

    if end_blog_length > begin_blog_length:
        request.send_header('Location', '/admin/blog/')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def login_page(request):
    context = {"error": ""}
    html = Template('login.html', context).render()

    request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
    if get_cookies(request):
        request.send_header('Location', '/admin/blog/')
    else:
        request.send_header('Content-Type', 'text/html')

        context["error"] = "Такой логин не существует"
    request.end_headers()
    # request.path = '/s/'
    request.wfile.write(str.encode(html))
    return request


def login_page_post(request):
    db = DataAccessLayer()
    context = {"error": ""}
    user_attribute = post(request)
    username = user_attribute.get('username')
    password = user_attribute.get('password')

    request.send_response(HTTPStatus.SEE_OTHER)
    if db.CheckUserIsExist(username, password):
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


def register_page(request):
    context = {'name': 'askar'}
    html = Template('register.html', context).render()
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def register_page_method_post(request):
    context = {'name': 'askar'}
    db = DataAccessLayer()
    html = Template('register.html', context).render()
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    user_attribute = post(request)
    username = user_attribute.get('username')
    password = user_attribute.get('password')
    phone = user_attribute.get('phone')
    email = user_attribute.get('email')
    address = user_attribute.get('address')
    if not db.CheckUserIsExist(username, password):
        db.CreateUser(username, password, phone, address, email)
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
                def load_benary(file):
                    with open(file, 'rb') as file:
                        return file.read()

                read = load_benary(file_path)
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


def get_cookies(request):
    res = {}
    cookie = (request.headers.get_all('Cookie', failobj={}))
    if len(cookie) > 0:
        for i in cookie[0].split(';'):
            res[(i.strip().split('='))[0]] = i.strip().split('=')[1]
    return res


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
