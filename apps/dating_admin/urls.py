from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^admin_index/$', views.admin_index, name="admin_index"),
    url(r'^questions_answers/$', views.questions_answers, name="questions_answers"),
    url(r'^app_members/$', views.app_members, name="app_members"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
