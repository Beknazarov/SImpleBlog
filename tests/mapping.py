host_url = "http://127.0.0.1:8080/register/"

site_mapping = {
    "register_user": {
        "url": host_url,
        "username": "username",
        "password": "password",
        "email": "email",
        "register": "input[type='submit']"
    },
    "login_user": {
        "url": "http://127.0.0.1:8080/admin/",
        "username": "username",
        "password": "password",
        "login": "input[type='submit']"
    },
    "create_post": {
        "url": "http://127.0.0.1:8080/admin/create/",
        "title": "title",
        "description": "description",
        "create": "input[type='submit']"
    },
    "update_post": {
        "url": "http://127.0.0.1:8080/admin/blog/",
        "update_link": ".update a",
        "title": "title",
        "description": "description",
        "update": "input[type='submit']"
    },
    "delete_post": {
        "url": "http://127.0.0.1:8080/admin/blog/",
        "delete": "//a[@href='/admin/delete/blog/2/']",
    },
    "logout": {
        "url": "http://127.0.0.1:8080/admin/blog/",
        "logout_link": "//a[@href='/logout/']",
    },
    "home": {
        "url": "http://127.0.0.1:8080/index/",
    }

}
