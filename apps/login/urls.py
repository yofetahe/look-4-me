from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.login_index, name="login_index"),
    url(r'^register/$', views.register, name="register"),    
    url(r'^getQuestionnaireForm/$', views.getQuestionnaireForm, name="getQuestionnaireForm"),
    url(r'^login/$', views.login, name="login"),
    url(r'^upload/$', views.upload, name="upload"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)