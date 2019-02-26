from django.db import models

class User(models.Model):   
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dob = models.DateTimeField()
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=15)
    seeking_for = models.CharField(max_length=15)
    age_between = models.CharField(max_length=45)
    zip_code = models.CharField(max_length=45)
    summery = models.TextField(null=True)
    user_like = models.ManyToManyField('self', related_name='likes', null=True)
    user_block = models.ManyToManyField('self', related_name='blockes', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
