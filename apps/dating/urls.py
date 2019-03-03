from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.dating_index, name="dating_index"),
    url(r'^get_profile_index/$', views.get_profile_index, name="get_profile_index"),
    url(r'^get_profile/$', views.get_profile, name="get_profile"),
    url(r'^update_profile_info/(?P<user_id>\d+)/$', views.update_profile_info, name="update_profile_info"),
    url(r'^get_questions_answers/$', views.get_questions_answers, name="get_questions_answers"),
    url(r'^get_statistics/$', views.get_statistics, name="get_statistics"),
    url(r'^my_matches$',views.my_matches, name="my_matches"),
    url(r'^search_matches$',views.search_matches, name="search_matches"),
    url(r'^search_memebers/$', views.search_memebers, name="search_memebers"),    
    url(r'^search/(?P<user_id>\d+)$',views.user_info_display, name="search"),
    url(r'^messages_likes$',views.messages_likes, name="messages_likes"),
    url(r'^logout$',views.logout, name="logout"),
    url(r'^like_person/(?P<user_id>\d+)$',views.like_person, name="like_person"),
    url(r'^block_person/(?P<user_id>\d+)$',views.block_member, name="block_person"),    
    url(r'^upload_picture$',views.upload_picture, name="upload_picture"),
    url(r'^change_profile_picture/(?P<pic_id>\d+)$', views.change_profile_picture, name="change_profile_picture"),
    url(r'^delete_picture/(?P<pic_id>\d+)$', views.delete_picture, name="delete_picture"),
    url(r'^push_message/(?P<user_id>\d+)$', views.push_message, name="push_message"),
    url(r'^display_messages$',views.display_messages, name="display_messages"),
    url(r'^message_picker$',views.message_picker, name="message_picker"),
    url(r'^like_pic_dispaly$',views.like_pic_dispaly, name="like_pic_dispaly"),
    url(r'^mes_reply/(?P<user_wb_id>[0-9]+)$',views.mes_reply),
    url(r'^delete_message/(?P<mesg_id>\d+)$',views.delete_message),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)