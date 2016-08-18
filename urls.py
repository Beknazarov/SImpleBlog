import views
from method import HTTP_METHODS
from router import Url
from system import static

patterns = [
    Url(HTTP_METHODS.GET, '/admin/delete/blog/\d+/', views.deletePost),
    Url(HTTP_METHODS.GET, '/admin/edit/blog/\d+/', views.updatePost),
    Url(HTTP_METHODS.POST, '/admin/update/', views.updateMethodPost),
    Url(HTTP_METHODS.GET, '/admin/blog/', views.adminPage),
    Url(HTTP_METHODS.GET, '/admin/create/', views.createPostPage),
    Url(HTTP_METHODS.POST, '/admin/create/', views.createPostMethodPost),
    Url(HTTP_METHODS.GET, '/register/', views.register),
    Url(HTTP_METHODS.POST, '/register/', views.registerMethodPost),
    Url(HTTP_METHODS.GET, '/logout/', views.logout),
    Url(HTTP_METHODS.GET, '/admin/', views.login),
    Url(HTTP_METHODS.POST, '/admin/', views.loginMethodPost),
    Url(HTTP_METHODS.GET, '/index/post/\d+', views.postDetail),
    Url(HTTP_METHODS.GET, '/index/', views.indexPage),
    Url(HTTP_METHODS.GET, '/static/', static),
    Url(HTTP_METHODS.GET, '/error/', views.error),

]
