from django.db import models
import re

class UserManager(models.Manager):

    def basic_validator(self, postData):

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        NAME_REGEX = re.compile(r'^[a-zA-Z ]')
        PASSWORD_1_REGEX = re.compile(r'^[A-Z]')
        PASSWORD_2_REGEX = re.compile(r'^[0-9]')

        errors = {}
        
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be filled or should be longer than 2 character"
        else:
            if not NAME_REGEX.match(postData['first_name']):
                errors['first_name'] = "First name must contain only character"        
        if len(postData['email']) == 0:
            errors['email'] = "Email is required"
        else:
            if not EMAIL_REGEX.match(postData['email']):
                errors['email'] = "Please enter valid email address"
        if len(postData['password']) == 0:
            errors['password'] = "Password is required"
        if len(postData['confirmpw']) == 0:
            errors['confirmpw'] = "Password is required"
        if (len(postData['confirmpw']) > 0 and len(postData['password']) > 0) and postData['password'] != postData['confirmpw']:
            errors['password'] = "Password doesn't match"
        if not 'iam' in postData:
            errors['iam'] = "Please select your gender"
        if not 'seekfor' in postData:
            errors['seekfor'] = "Please select your sexaul oritation"
        if postData['age_between']=='':
            errors['age_between'] = "Please select age"
        if len(postData['zipcode']) == 0:
            errors['zipcode'] = "Zipcode is required"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) == 0 or len(postData['password']) == 0:
            errors['general'] = "Email and password are required to login to the app"
                
        return errors

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
    # user_like = models.ManyToManyField('self', related_name='likes')
    # user_block = models.ManyToManyField('self', related_name='blockes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    age = 0
    like_status = ''
    block_status = ''

    objects = UserManager()

class UserLike(models.Model):
    like_by = models.ForeignKey(User, related_name='like_by', default=1, on_delete=models.PROTECT)
    liked = models.ForeignKey(User, related_name='liked', default=1, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserBlock(models.Model):
    block_by = models.ForeignKey(User, related_name='block_by', default=1, on_delete=models.PROTECT)
    blocked = models.ForeignKey(User, related_name='blocked', default=1, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)