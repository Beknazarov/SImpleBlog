import views
from method import HTTP_METHODS
from router import Url
from system import static

patterns = [
    Url(HTTP_METHODS.GET, '/admin/delete/blog/\d+/', views.delete_post),
    Url(HTTP_METHODS.GET, '/admin/edit/blog/\d+/', views.update_post),
    Url(HTTP_METHODS.POST, '/admin/update/', views.update_post),
    Url(HTTP_METHODS.GET, '/admin/blog/', views.admin_page),
    Url(HTTP_METHODS.GET, '/admin/create/', views.create_post),
    Url(HTTP_METHODS.POST, '/admin/create/', views.create_post),
    Url(HTTP_METHODS.GET, '/register/', views.register),
    Url(HTTP_METHODS.POST, '/register/', views.register),
    Url(HTTP_METHODS.GET, '/logout/', views.logout),
    Url(HTTP_METHODS.GET, '/admin/', views.login),
    Url(HTTP_METHODS.POST, '/admin/', views.login),
    Url(HTTP_METHODS.GET, '/index/post/\d+', views.detail_post),
    Url(HTTP_METHODS.GET, '/index/', views.index_page),
    Url(HTTP_METHODS.GET, '/static/', static),
    Url(HTTP_METHODS.GET, '/error/', views.error),

]
