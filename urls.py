import views
from method import HTTP_METHODS
from router import Url

patterns = [
    Url(HTTP_METHODS.GET, '/admin/blog/\d+/', views.admin_detail_post),
    Url(HTTP_METHODS.GET, '/admin/delete/blog/\d+/', views.admin_delete_post),
    Url(HTTP_METHODS.GET, '/admin/edit/blog/\d+/', views.admin_edit_post),
    Url(HTTP_METHODS.POST, '/admin/update/', views.admin_update_post_method),
    Url(HTTP_METHODS.GET, '/admin/blog/', views.admin_blog_view),
    Url(HTTP_METHODS.GET, '/admin/create/', views.admin_create_post),
    Url(HTTP_METHODS.POST, '/admin/create/', views.admin_create_blog_method_post),
    Url(HTTP_METHODS.GET, '/register/', views.register_page),
    Url(HTTP_METHODS.POST, '/register/', views.register_page_method_post),
    Url(HTTP_METHODS.GET, '/logout/', views.logout),
    Url(HTTP_METHODS.GET, '/admin/', views.login_page),
    Url(HTTP_METHODS.POST, '/admin/', views.login_page_post),
    Url(HTTP_METHODS.GET, '/index/post/\d+', views.index_blog_detail),
    Url(HTTP_METHODS.GET, '/index/', views.index_blog),
    Url(HTTP_METHODS.GET, '/static/', views.static),
    Url(HTTP_METHODS.GET, '/error/', views.error),

]
