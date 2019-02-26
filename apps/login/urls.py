from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_index, name="login_index"),
    url(r'^register/$', views.register, name="register"),    
    url(r'^getQuestionnaireForm/$', views.getQuestionnaireForm, name="getQuestionnaireForm"),
    url(r'^login/$', views.login, name="login"),
        
]