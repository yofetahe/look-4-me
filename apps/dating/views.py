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
    blocked_user = UserBlock.objects.filter(block_by=current_user)    
    user_list = User.objects.filter(gender=current_user.seeking_for).exclude(id=request.session['user_id']).exclude(blocked__in=blocked_user)
    liked_user = UserLike.objects.filter(like_by=current_user)

    photo_url = {}
    for user in user_list:        
        for pic in user.pictures.all():
            photo_url[pic.id] = 'dating' + str(pic.pictures.url)

    for pic in current_user.pictures.all():
        photo_url[pic.id] = 'dating' + str(pic.pictures.url)
    
    # ----- to pick liked users ------#
    liked_user_array = []    
    for u in user_list:        
        for y in liked_user:
            if u == y.liked:               
                liked_user_array.append(y.liked)
    
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
    print(current_user.age)
    # ----- current user age ----- #

    context = {
        "user_list": user_list,
        "user": current_user,
        "liked_user": liked_user, 
        "liked_user_array": liked_user_array,
        "photo_url":photo_url
    }

    return render(request, 'dating/my_matches.html', context)

def search_matches(request):
    current_user = User.objects.get(id=request.session['user_id'])

    user_list = User.objects.all()
    photo_url = {}
    for user in user_list:
        for pic in user.pictures.all():
            photo_url[pic.id] = 'dating' + str(pic.pictures.url)

    # ----- current user age ----- #
    date_format = "%Y-%m-%d"
    today = datetime.strptime(str(datetime.now().date()), date_format)
    current_user_dob = datetime.strptime(str(current_user.dob.date()), date_format)
    delta = today - current_user_dob
    current_user.age = round(delta.days/365)
    print(current_user.age)
    # ----- current user age ----- #

    context = {
        "photo_url": photo_url,
        "user": current_user,
        "age_range": ['25-35', '36-45', '46-55', '56-65', '66-75'],
        "ethnic_group": ['White or Caucasian', 'Native American', 'Asian', 'Native Hawaiian or Pacific islander', 'Black or African', 'Latino or Hispanic', 'Middle Eastern', 'Other'],
        "religion": ['Christian', 'Catholic', 'Spiritual but not religious', 'Protestant', 'Agnostic', 'Other'],
        "educational_level": ["High School", "Some College", "Associates Degree", "Bachelors Degree", "Graduate Degree", "Post Doctoral"]
    }
    return render(request,'dating/search_matches.html', context)

def search_memebers(request):
    # seekfor = request.POST['seekfor']
    age_between = request.POST['age_between']
    ethnic_group = request.POST['ethnic_group']
    marital_status = request.POST['marital_status']
    zip_code = request.POST['zip_code']
    religion = request.POST['religion']
    educational_level = request.POST['educational_level']

    current_user = User.objects.get(id=request.session['user_id'])
    user_list = User.objects.all()
    liked_user = UserLike.objects.filter(like_by=current_user)

    photo_url = {}
    for user in user_list:
        for pic in user.pictures.all():
            photo_url[pic.id] = 'dating' + str(pic.pictures.url)

    liked_user_array = []    
    for u in user_list:        
        for y in liked_user:
            if u == y.liked:               
                liked_user_array.append(y.liked)

    # ----- age calculation ----- #
    date_format = "%Y-%m-%d"
    today = datetime.strptime(str(datetime.now().date()), date_format)    
    for user in user_list:
        dob = datetime.strptime(str(user.dob.date()), date_format)
        delta = today - dob
        user.age = round(delta.days/365)
    # ----- age calculation ----- #

    context = {
         "user": user_list,
         "liked_user_array":liked_user_array,
         "photo_url": photo_url
    }

    return render(request,'dating/search_result.html', context)

def user_info_display(request, user_id):
    user = User.objects.get(id=request.session['user_id'])
    selected_user=User.objects.get(id=user_id)
    liked_user = UserLike.objects.filter(like_by=user).filter(liked=selected_user)

    # ----- current user age ----- #
    date_format = "%Y-%m-%d"
    today = datetime.strptime(str(datetime.now().date()), date_format)    
    selected_user_dob = datetime.strptime(str(selected_user.dob.date()), date_format)
    delta = today - selected_user_dob
    selected_user.age = round(delta.days/365)
    print(selected_user.age)
    # ----- current user age ----- #
    
    photo_url = {}
    for pic in selected_user.pictures.all():
        photo_url[pic.id] = 'dating' + str(pic.pictures.url)
    for pic in user.pictures.all():
        photo_url[pic.id] = 'dating' + str(pic.pictures.url)

    context={
        "user": user,
        "selected_user": selected_user,
        "photo_url": photo_url,
        "liked_user": liked_user
    }
    return render(request,'dating/user_info.html', context)


def messages_likes(request):
    current_user = User.objects.get(id=request.session['user_id'])
    
    # ----- age calculation ----- #
    date_format = "%Y-%m-%d"
    today = datetime.strptime(str(datetime.now().date()), date_format)    
    dob = datetime.strptime(str(current_user.dob.date()), date_format)
    delta = today - dob
    current_user.age = round(delta.days/365)
    # ----- age calculation ----- #
    
    current_user.dob.date()

    photo_url = {}
    for pic in current_user.pictures.all():
        photo_url[pic.id] = 'dating' + str(pic.pictures.url)

    user = User.objects.get(id=request.session['user_id'])
    messages = Message.objects.filter(user_written_for=user)
    
    context={
        "messages": messages,    
        "user": current_user,
        "photo_url": photo_url
    }

    return render(request,'dating/message_like.html', context)

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
    UserLike.objects.create(like_by=current_user, liked=user)
    return redirect(my_matches)

def upload_picture(request):
    if request.method == 'POST':
        
        # myfile = request.FILES['prof_picture']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        # print("uploaded_file_url --- ", uploaded_file_url)
        current_user = User.objects.get(id=request.session['user_id'])
        x = Picture.objects.create(pictures=request.FILES['prof_picture'], is_profile_pic='0', user=current_user)
       
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



# ----------------------------- Message UPDATE--------------------------

def push_message(request, user_id):
    user = User.objects.get(id=request.session['user_id'])
    send_to = User.objects.get(id=user_id)
    obj = Message.objects.create(title=request.POST['title'],content=request.POST['content'],user_written_for=send_to,user_written_by=user)
    return redirect('../search/'+str(user_id))


#ajax
def message_picker(request):
    data = request.GET
    messageid = data.get('message_id')
    message = Message.objects.get(id=messageid)
    context={
        'mes_id':message
    }
    return render(request,'dating/message_pick.html',context)

#ajax
def like_pic_dispaly(request):
    current_user = User.objects.get(id=request.session['user_id'])    
    liked_user = UserLike.objects.filter(like_by=current_user)
    
    photo_url = {}
    for user in liked_user:
        for pic in user.liked.pictures.all():
            photo_url[pic.id] = 'dating' + str(pic.pictures.url)

    # ----- age calculation ----- #
    date_format = "%Y-%m-%d"
    today = datetime.strptime(str(datetime.now().date()), date_format)    
    for user in liked_user:
        dob = datetime.strptime(str(user.liked.dob.date()), date_format)
        delta = today - dob
        user.liked.age = round(delta.days/365)
    # ----- age calculation ----- #
    
    context = {
        "user_list": liked_user,
        "photo_url": photo_url
    }
    return render(request,'dating/like_pic_dispaly.html',context)

#ajax
def display_messages(request):
    user = User.objects.get(id=request.session['user_id'])
    messages = Message.objects.filter(user_written_for=user)

    context={
        'messages': messages
    }
    return render(request,'dating/messages.html', context)

def delete_message(request,mesg_id):
    m=Message.objects.get(id=mesg_id)
    m.delete()
    return redirect('../messages_likes')


    

#ajax
def mes_reply(request,user_wb_id):
    u=User.objects.get(id=request.session['user_id'])
    se_to=User.objects.get(id=user_wb_id)
    rep_to=Message.objects.get(id=request.POST['mes_id'])
    Message.objects.create(title=request.POST['title'],content=request.POST['reply_content'],user_written_for=se_to,user_written_by=u,reply_to=rep_to)
    return redirect('/dating/messages_likes')


def test(request):
    return render(request, 'dating/test.html')