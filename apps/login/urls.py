from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^homepage$',views.homepage),
    url(r'^search$',views.search),
    # url(r'^search_process$',views.search_process),
    # url(r'^posts$', views.post, name='posts'),
    url(r'^search/(?P<userid>[0-9]+)$',views.user_info_display),
    url(r'^message$',views.message_like),
]