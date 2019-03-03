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
    url(r'^get_signup_form/$', views.get_signup_form, name="get_signup_form"),
    url(r'^get_login_form/$', views.get_login_form, name="get_login_form"),
    url(r'^success/$', views.success, name="success"),
    url(r'^questionnaire_answer/$', views.questionnaire_answer, name="questionnaire_answer"),
    url(r'^admin_login/$', views.admin_login, name="admin_login"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)