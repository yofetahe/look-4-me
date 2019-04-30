from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import User
from django.contrib import messages
import bcrypt

# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'core/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'core/simple_upload.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['myfile']
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(fs.url(file_name))
    return render(request, 'login/index.html', {"uploaded_file_url": fs.url(file_name)})

def success(request):
    if 'user' in request.session:
        return redirect('/../dating/')
    else:
        return redirect(login_index)

def login_index(request):
    context = {
        "age_range": ['18 - 24', '25-35', '36-45', '46-55', '56-65', '66-75']
    }
    return render(request, 'login/index.html', context)

def register(request):

    if 'user' in request.session:
        return redirect(success)
    
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
        user = User.objects.filter(email=request.POST['email'])
        if user:
            messages.error(request, "This email address already exist", extra_tags="email")
            return render(request, 'login/index.html', context)
        #--- check if the email exist or not ---#
        
        hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        
        user = User.objects.create(name=request.POST['first_name'], dob=request.POST['dob'], email=request.POST['email'], password=hashedPw, gender=request.POST['iam'], seeking_for=request.POST['seekfor'], age_between=request.POST['age_between'], zip_code=request.POST['zipcode'], summery=request.POST['summery'])
        
        request.session['temp_user_id'] = user.id
        request.session['temp_user'] = user.name

        return redirect(getQuestionnaireForm)

def getQuestionnaireForm(request):

    questionnaire = [{'Which marital status do you prefer?':['No preference', 'Never Married', 'Currently Separated', 'Widow/Widower']},
                        {'Do you smoke?':['No, Never!', 'Yes-occasionally', 'Yes-daily', 'Yes -trying to quit']},
                        {'Do you have any kids?':['No', 'Yes', 'Yes, live away from home', 'yes - live at home']},
                        {'Do you want any Children?':['No', 'Definitely', 'Someday', 'Not Sure']},
                        {'How often do you drink?':['Never', 'Social drinker', 'Moderately', 'Regularly']},
                        {'What is your salary?':['$25,000 - $50,000', '$50,001 - $100,000', '$100,001 - $200,000', 'Greater than $200,001  ']},]

    context = {
        "questionnaire": questionnaire
    }

    return render(request, 'login/questionnaire.html', context)

def questionnaire_answer(request):

    request.session['user_id'] = request.session['temp_user_id']
    request.session['user'] = request.session['temp_user']
    request.session.pop('temp_user_id')
    request.session.pop('temp_user')

    return redirect(success)

def login(request):
    if 'user' in request.session:
        return redirect(success)
    
    errors = User.objects.login_validator(request.POST)
    
    if len(errors) > 0:
        for tag, value in errors.items():
            messages.error(request, value, extra_tags=tag)
        return redirect(get_login_form)
    else:
        user = User.objects.filter(email=request.POST['email'])
        for u in user:
            userdbpassword = u.password
        print(user)
        if user and bcrypt.checkpw(request.POST['password'].encode(), userdbpassword.encode()):
            request.session['user'] = user[0].name
            request.session['user_id'] = user[0].id
            return redirect(success)
        else:
            messages.error(request, "Invalid username or password", extra_tags='general')
            return redirect(get_login_form)    

def get_signup_form(request):
    context = {
        "age_range": ['25-35', '36-45', '46-55', '56-65', '66-75']
    }
    return render(request, 'login/signup_form.html', context)

def get_login_form(request):
    return render(request, 'login/login_form.html')

def admin_login(request):
    return redirect('/../dating_admin/')