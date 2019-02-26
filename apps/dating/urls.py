from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="dating_index"),
    url(r'^get_profile_index/$', views.get_profile_index, name="get_profile_index"),
    url(r'^get_profile/$', views.get_profile, name="get_profile"),
    url(r'^get_questions_answers/$', views.get_questions_answers, name="get_questions_answers"),
    url(r'^get_statistics/$', views.get_statistics, name="get_statistics"),
]