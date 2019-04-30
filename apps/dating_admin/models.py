from django.db import models

class Category(models.Model):
    cat_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Questionnaire(models.Model):
    question_content = models.TextField()
    question_type = models.CharField(max_length=15)  #-- 1, 2, 11, 22
    category = models.ForeignKey(Category, related_name='questions', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Choice(models.Model):
    choice_content = models.CharField(max_length=255)
    questions = models.ForeignKey(Questionnaire, related_name='choices', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
