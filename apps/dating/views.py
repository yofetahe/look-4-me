from django.shortcuts import render, redirect
from apps.login.models import User, UserLike, UserBlock
from .models import Picture, Question_answer, Message
from django.utils.timezone import datetime
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.utils.dateformat import DateFormat
from django.contrib import messages
import bcrypt

def dating_index(request):

    if 'user' not in request.session:
        return redirect('../login/')

    return redirect(my_matches)

def get_profile_index(request):
    user = User.objects.get(id=request.session['user_id'])
    pictures = Picture.objects.filter(user=user)

    context = {
        "user":user,
        "age_range": ['25-35', '36-45', '46-55', '56-65', '66-75'],
        "pictures": pictures
    }
    return render(request, 'dating/mp_profile_index.html', context)

def get_profile(request):
    user = User.objects.get(id=request.session['user_id'])
    
    context = {
        "user":user,
        "age_range": ['25-35', '36-45', '46-55', '56-65', '66-75']
    }
    return render(request, 'dating/mp_my_profile.html', context)

def update_profile_info(request, user_id):

    if 'user' not in request.session:
        return redirect('../login/')
    
    errors = User.objects.basic_validator(request.POST)
    
    context = {
        "first_name": request.POST['first_name'],        
        "email": request.POST['email'],
        "age_range": ['25-35', '36-45', '46-55', '56-65', '66-75']
    }

    if len(errors) > 0:
        for tag, value in errors.items():
            messages.error(request, value, extra_tags=tag)
        
        return render(request, 'login/index.html', context)
    else:
        
        #--- check if the email exist or not ---#
        user = User.objects.filter(email=request.POST['email']).exclude(id=user_id)
        print(User)
        if user:
            messages.error(request, "This email address already exist", extra_tags="email")
            return redirect(get_profile_index)
        #--- check if the email exist or not ---#
        
        hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        
        user = User.objects.get(id=user_id)
        user.name=request.POST['first_name']
        user.dob=request.POST['dob']
        user.email=request.POST['email']
        user.password=hashedPw
        user.gender=request.POST['iam']
        user.seeking_for=request.POST['seekfor']
        user.age_between=request.POST['age_between']
        user.zip_code=request.POST['zipcode']
        user.summery=request.POST['summery']
        user.save()

    return redirect(get_profile_index)

def get_questions_answers(request):
    return render(request, 'dating/mp_questions_answers.html')

def get_statistics(request):
    return render(request, 'dating/mp_activity_statistics.html')
   
def my_matches(request):

    if 'user' not in request.session:
        return redirect('../login/')

    current_user = User.objects.get(id=request.session['user_id'])
    user_list = User.objects.filter(gender=current_user.seeking_for).exclude(id=request.session['user_id'])
    
    # ----- age calculation ----- #
    date_format = "%Y-%m-%d"
    today = datetime.strptime(str(datetime.now().date()), date_format)    
    for user in user_list:        
        dob = datetime.strptime(str(user.dob.date()), date_format)
        delta = today - dob
        user.age = round(delta.days/365)
    # ----- age calculation ----- #

    # ----- current user age ----- #
    current_user_dob = datetime.strptime(str(current_user.dob.date()), date_format)
    delta = today - current_user_dob
    current_user.age = round(delta.days/365)
    # ----- current user age ----- #

    context = {
        "user_list": user_list,
        "user": current_user
    }

    return render(request, 'dating/my_matches.html', context)

def search_matches(request):
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        "user": current_user
    }
    return render(request,'dating/search_matches.html', context)


# def search_process(request):
#     context = {
#         'posts': Post.objects.all(),
#         'new_post_form' : PostForm()
#     }
#     return render(request, 'login/search.html', context)


# def post(request):  
#     if request.method == 'POST':
#         bound_form = PostForm(request.POST)
 
#     if bound_form.is_valid():
#         Post.objects.create(description=request.POST['description'])
#     context = {
# 		'posts': Post.objects.all()
#     }
#     return render(request, 'login/search_result.html', context)


def user_info_display(request, user_id):
    return render(request,'dating/user_info.html',)


def messages_likes(request):
    return render(request,'dating/message_like.html',)

def logout(request):
    request.session.pop('user')
    request.session.pop('user_id')
    return redirect('../login/')

def block_member(request, user_id):
    current_user = User.objects.get(id=request.session['user_id'])
    user = User.objects.get(id=user_id)
    UserBlock.objects.create(block_by=current_user, blocked=user)
    return redirect(my_matches)

def like_person(request, user_id):
    current_user = User.objects.get(id=request.session['user_id'])
    user = User.objects.get(id=user_id)
    user_like = UserLike.objects.all()
    print(len(user_like))
    print(current_user)
    print(user)
    user_l = UserLike.objects.create()
    user_l.like_by.add(current_user)
    user_l.liked.add(user)        
    return redirect(my_matches)

def upload_picture(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['prof_picture']
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(fs.url(file_name))
        current_user = User.objects.get(id=request.session['user_id'])
        Picture.objects.create(pictures=request.FILES['prof_picture'], pictures_url=fs.url(file_name), is_profile_pic='0', user=current_user)

    return redirect(get_profile_index)

def change_profile_picture(request, pic_id):

    user = User.objects.get(id=request.session['user_id'])
    pictures = Picture.objects.filter(user=user)

    for pic in pictures:
        photos = Picture.objects.get(id=pic.id)
        photos.is_profile_pic = 'FALSE'
        photos.save()

    picture = Picture.objects.get(id=pic_id)
    picture.is_profile_pic = 'TRUE'
    picture.save()
    picture = Picture.objects.get(id=pic_id)

    return redirect(get_profile_index)

def delete_picture(request, pic_id):    
    picture = Picture.objects.get(id=pic_id)
    picture.delete()
    return redirect(get_profile_index)