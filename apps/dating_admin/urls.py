from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.admin_login, name="admin_login"),
    url(r'^admin_login_validator$', views.admin_login_validator, name="admin_login_validator"),
    url(r'^admin_logout/$', views.admin_logout, name="admin_logout"),
    url(r'^web_index/$', views.web_index, name="web_index"),
    url(r'^admin_index/$', views.admin_index, name="admin_index"),
    url(r'^questions_answers/$', views.questions_answers, name="questions_answers"),
    url(r'^app_members/$', views.app_members, name="app_members"),
    url(r'^add_category/$', views.add_category, name="add_category"),
    url(r'^add_question/$', views.add_question, name="add_question"),
    url(r'^add_choice/$', views.add_choice, name="add_choice"),
    url(r'^category/delete/(?P<id>\d+)/$', views.delete_category, name="delete_category"),
    url(r'^question/delete/(?P<id>\d+)/$', views.delete_question, name="delete_question"),
    url(r'^choice/delete/(?P<id>\d+)/$', views.delete_choice, name="delete_choice"),
    url(r'^category/update/$', views.update_category, name="update_category"),
    url(r'^category/update/(?P<id>\d+)/$', views.update_add_category, name="update_add_category"),
    url(r'^question/update/$', views.update_question, name="update_question"),
    url(r'^question/update/(?P<id>\d+)/$', views.update_add_question, name="update_add_question"),
    url(r'^choice/update/$', views.update_choice, name="update_choice"),
    url(r'^choice/update/(?P<id>\d+)/$', views.update_add_choice, name="update_add_choice"),        
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
