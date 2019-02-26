from django.db import models
from apps.login.models import User
from apps.dating_admin.models import Questionnaire

class Picture(models.Model):
    pictures = models.ImageField(upload_to='dating/photos/')
    is_profile_pic = models.CharField(max_length=45)
    user = models.ForiegnKey(User, related_name="pictures")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Question_answer(models.Model):
    user = models.ForiegnKey(User, related_name="questions_answers")
    question = models.ForiegnKey(Questionnaire, related_name="user_quetions")    
    selected_choice = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user_written_for = models.ForiegnKey(User, related_name="written_for")
    user_written_by = models.ForiegnKey(User, related_name="written_by")
    reply_to = models.ForiegnKey('self', related_name="reply_to", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
