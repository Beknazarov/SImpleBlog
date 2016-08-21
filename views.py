# coding: utf-8
from http import HTTPStatus

import settings
from db.database import DataAccessLayer
from method import HTTP_CODE
from system import method_POST, get_cookies, get_post_id_after_split, clear_cookie, check_type_post_id
from template_code.template import Template, Templates


def admin_page(request):
    request.send_response(HTTPStatus.SEE_OTHER)

    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    else:
        request.send_header('Content-Type', 'text/html')

    db = DataAccessLayer()
    posts_html = ""
    post_not_exist = 0
    username = get_cookies(request).get('cookie_username')
    count_posts = db.get_count_of_their_posts(username)
    posts = db.get_to_only_their_posts(username)

    if count_posts == post_not_exist:
        posts_html = "<h1>Empty Post </h1>"
    else:
        for post_id, posts_attr in posts.items():
            title, description = posts_attr[0], posts_attr[1]
            posts_html += "<div class='post_page'>"
            posts_html += '<br/>'
            posts_html += "<div class='update'> <a href=/admin/edit/blog/%s/> Update </a></div>" % post_id
            posts_html += "<div class='delete'> <a href=/admin/delete/blog/%s/> Delete </a></div>" % post_id
            posts_html += "<h2> <div class='title'>Title: %s</div></h2>" % title
            posts_html += "<div class='description'>Description: %s</div>" % description
            posts_html += "<hr />"
            posts_html += "</div>"

    f = open(settings.TEMPLATES_DIR + '/admin_post.html')
    read = f.read()
    html = Templates(read).render(username=username, posts=posts_html)
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def index_page(request):
    status = True
    if not get_cookies(request):
        status = False
    db = DataAccessLayer()
    username = get_cookies(request).get('cookie_username')
    all_post_html = ""

    for author, posts in db.get_all_post().items():
        for post_id, post_attr in posts.items():
            title, description = post_attr[0], post_attr[1]
            all_post_html += "<div class='post'>"
            all_post_html += "<div class='title'>" \
                             "<h2>Title: " \
                             "<a class='id' href=/index/post/%s/>%s</a>" \
                             "</h2>" \
                             "</div>" % (post_id, title)
            all_post_html += "<div class='description'>Description: %s</div>" % description
            all_post_html += "<div class='author'>Author: %s</div>" % author
            all_post_html += "<hr />"
            all_post_html += "</div>"

    f = open(settings.TEMPLATES_DIR + '/index.html')
    read = f.read()
    html = Templates(read).render(posts=all_post_html, username=username, status=status)
    request.send_response(HTTP_CODE.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def create_post(request):
    context = {}
    request.send_response(HTTP_CODE.SEE_OTHER)
    db = DataAccessLayer()

    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    if request.HTTP_METHODS == "POST":
        context = {}
        post_attr = method_POST(request)
        title = post_attr.get('title')
        description = post_attr.get('description')
        username = get_cookies(request).get('cookie_username')

        count_before_adding_posts = int(db.count_post())
        db.create_post(username, title, description)
        count_after_adding_posts = int(db.count_post())
        if count_after_adding_posts > count_before_adding_posts:
            request.send_header('Location', '/admin/blog/')
    html = Template('create_post.html', context).render()
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def update_post(request):
    request.send_response(HTTP_CODE.SEE_OTHER)

    if not get_cookies(request):
        request.send_header('Location', '/admin/')
    username = get_cookies(request).get('cookie_username')
    db = DataAccessLayer()
    edit_post_html = ""
    if request.HTTP_METHODS == "GET":
        post_id = get_post_id_after_split(request)
        if not db.is_post_exist(post_id) or \
                not db.check_the_author_of_the_posts(username, post_id):
            request.send_header('Location', '/error/')
        else:
            post = db.get_post_by_id(post_id)
            title, description = post[0], post[1]
            edit_post_html += "<form action='/admin/update/' method='post'>"
            edit_post_html += "<input type='hidden' value='%s' name='hiddenid'/><br/>" % post_id
            edit_post_html += "<input type='text' value='%s' name='title'/><br/>" % title
            edit_post_html += "<textarea cols='50' rows='10' id='description' name='description'>%s</textarea>" \
                              " <br/>" % description
            edit_post_html += "<input type='submit' value='Update' />"
            edit_post_html += "</form>"

    elif request.HTTP_METHODS == "POST":
        post_attribute = method_POST(request)

        post_id = post_attribute.get('hiddenid')
        title = post_attribute.get('title')
        description = post_attribute.get('description')
        username = get_cookies(request).get('cookie_username')

        db.update_post(int(post_id), username, title, description)
        request.send_header('Location', '/admin/blog/')

    f = open(settings.TEMPLATES_DIR + '/update_post.html')
    read = f.read()
    html = Templates(read).render(post_edit=edit_post_html)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def detail_post(request):
    request.send_response(HTTP_CODE.OK)

    db = DataAccessLayer()
    post_id = get_post_id_after_split(request)
    post = db.get_post_by_id(int(post_id))

    detail_post_html = '<br/>'
    detail_post_html += "<div class='title'>Title: %s</div><br/>" % post[0]
    detail_post_html += "<div class='description'>Description: %s</div><br/>" % post[1]
    detail_post_html += "<hr />"

    f = open(settings.TEMPLATES_DIR + '/detail_post.html')
    read = f.read()
    html = Templates(read).render(detail_post=detail_post_html)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def delete_post(request):
    request.send_response(HTTP_CODE.SEE_OTHER)

    post_id = get_post_id_after_split(request)
    username = get_cookies(request).get('cookie_username')
    db = DataAccessLayer()

    if not db.check_the_author_of_the_posts(username, post_id):
        request.send_header('Location', '/error/')
    else:
        db.delete_post_by_id(int(post_id))
        request.send_header('Location', '/admin/blog/')

    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    return request


def login(request):
    context = {"error": ""}
    if request.HTTP_METHODS == "GET":
        request.send_response(HTTP_CODE.TEMPORARY_REDIRECT)

        if get_cookies(request):
            request.send_header('Location', '/admin/blog/')
        else:
            request.send_header('Content-Type', 'text/html')

    elif request.HTTP_METHODS == "POST":
        request.send_response(HTTP_CODE.SEE_OTHER)

        db = DataAccessLayer()
        user_attr = method_POST(request)
        username = user_attr.get('username')
        password = user_attr.get('password')

        if db.is_login_correct(username, password):
            request.send_header('Set-Cookie', 'cookie_username=%s;path=/;' % username)
            request.send_header('Location', '/admin/blog/')
            print("Login Success")
        else:
            request.send_header('Content-Type', 'text/html')
            context["error"] = "Ошибка авторизации"
            print("Login Error")
    html = Template('login.html', context).render()
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def register(request):
    request.send_response(HTTP_CODE.OK)

    context = {'title': 'Регистрация'}
    db = DataAccessLayer()

    if request.HTTP_METHODS == "POST":

        user_attr = method_POST(request)
        username = user_attr.get('username')
        password = user_attr.get('password')
        email = user_attr.get('email')
        if not db.is_user_exist(username):
            db.create_user(username, password, email)
            print("Create success new login")
        else:
            print("Login don't register")
    html = Template('register.html', context).render()
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def logout(request):
    request.send_response(HTTP_CODE.TEMPORARY_REDIRECT)
    if get_cookies(request).get('cookie_username'):
        request.send_header("Set-Cookie", clear_cookie())
        request.send_header('Location', '/admin/')
    else:
        request.send_header('Content-Type', 'text/html')
    request.end_headers()


def handle_404(request):
    context = {'not-found': 'File Not found'}
    html = Template('404.html', context).render()
    request.send_response(HTTP_CODE.NOT_FOUND)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))

    return request


def error(request):
    context = {}
    html = Template('error.html', context).render()
    request.send_response(HTTP_CODE.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
