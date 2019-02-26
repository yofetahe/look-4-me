from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dating_index, name="dating_index"),
    url(r'^get_profile_index/$', views.get_profile_index, name="get_profile_index"),
    url(r'^get_profile/$', views.get_profile, name="get_profile"),
    url(r'^get_questions_answers/$', views.get_questions_answers, name="get_questions_answers"),
    url(r'^get_statistics/$', views.get_statistics, name="get_statistics"),
    url(r'^my_matches$',views.my_matches, name="my_matches"),
    url(r'^search_matches$',views.search_matches, name="search_matches"),
    # url(r'^search_process$',views.search_process),
    # url(r'^posts$', views.post, name='posts'),
    url(r'^search/(?P<userid>[0-9]+)$',views.user_info_display),
    url(r'^messages_likes$',views.messages_likes, name="messages_likes"),
    url(r'^logout$',views.logout, name="logout"),
]