from django.db import models
from apps.login.models import User
from apps.dating_admin.models import Questionnaire

class Picture(models.Model):
    pictures = models.ImageField(upload_to='photos', default = 'login/photo/default_male.gif')
    pictures_url = models.CharField(max_length=255, null=True)
    is_profile_pic = models.CharField(max_length=45)
    user = models.ForeignKey(User, related_name="pictures", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Question_answer(models.Model):
    user = models.ForeignKey(User, related_name="questions_answers", on_delete=models.PROTECT)
    question = models.ForeignKey(Questionnaire, related_name="user_quetions", on_delete=models.PROTECT)    
    selected_choice = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user_written_for = models.ForeignKey(User, related_name="written_for", on_delete=models.PROTECT)
    user_written_by = models.ForeignKey(User, related_name="written_by", on_delete=models.PROTECT)
    reply_to = models.ForeignKey('self', related_name="reply_from", null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
