from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_index, name="login_index"),
    url(r'^register/$', views.register, name="register"),    
    url(r'^getQuestionnaireForm/$', views.getQuestionnaireForm, name="getQuestionnaireForm"),
    url(r'^login/$', views.login, name="login"),
    url(r'^message$',views.message_like),
    url(r'^homepage$',views.homepage),
    url(r'^search$',views.search),
    # url(r'^search_process$',views.search_process),
    # url(r'^posts$', views.post, name='posts'),
    url(r'^search/(?P<userid>[0-9]+)$',views.user_info_display),    
]