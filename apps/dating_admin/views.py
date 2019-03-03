from django.shortcuts import render, redirect
from apps.dating_admin.models import Questionnaire, Category, Choice
from apps.login.models import User


def admin_login(request):
    return render(request, 'dating_admin/admin_login.html')

def admin_login_validator(request):
    if request.POST['email'] == 'yofetahe@gmail.com' or request.POST['email'] == 'datingadmin@gmail.com' and request.POST['password'] == 'django1234':
        request.session['user'] = request.POST['email']
        return redirect(admin_index)
    else:
        return redirect(admin_login)

def admin_logout(request):
    request.session.pop('user')
    return redirect(admin_login)

def web_index(request):
    return redirect('/../')

def admin_index(request):
    if 'user' not in request.session:
        return redirect(admin_login)
    users = User.objects.all()    
    return render(request, 'dating_admin/index.html', {"users": users})

def questions_answers(request):
    if 'user' not in request.session:
        return redirect(admin_login)
    category_query = Category.objects.all()
    question_query = Questionnaire.objects.all()
    choice_query = Choice.objects.all()
    content = {
        "category_all":category_query,
        "questions_all":question_query,
        "choice_all" :choice_query
    }
    return render(request, 'dating_admin/questions_answers.html', content)

def app_members(request):
    if 'user' not in request.session:
        return redirect(admin_login)
    context = {
        "arrays": [1,2,3,4,5,6]
    }
    return render(request, 'dating_admin/app_members.html', context)

def add_category(request):
    if 'user' not in request.session:
        return redirect(admin_login)
    category_add = Category.objects.create(cat_title =request.POST['category_title'])
    print(category_add)
    return redirect(admin_index)

def delete_category(request, id):
    if 'user' not in request.session:
        return redirect(admin_login)
    cate_query = Category.objects.get(id =id)
    cate_query.delete()
    return redirect(admin_index)

def update_category(request):
    if 'user' not in request.session:
        return redirect(admin_login)
    data=request.GET
    category_id=data.get('id')
    print(category_id)
    category_query = Category.objects.get(id = category_id)
    context={
    "category_id":category_id,
    "category_all":category_query,
    }
    return render(request, "dating_admin/form_update.html",context)

def update_add_category(request, id):
    if 'user' not in request.session:
        return redirect(admin_login)
    category = Category.objects.get(id =id)
    category.cat_title = request.POST['category_title']
    category.save()
    return redirect(admin_index)

def add_question(request):
    if 'user' not in request.session:
        return redirect(admin_login)
    cate_query = Category.objects.get(id = request.POST['category_option'])
    question = Questionnaire.objects.create(question_content = request.POST['question_content'], category = cate_query, question_type = request.POST['question_type'])
    print(question)
    return redirect(admin_index)

def delete_question(request, id):
    if 'user' not in request.session:
        return redirect(admin_login)
    ques_query = Questionnaire.objects.get(id =id)
    ques_query.delete()
    return redirect(admin_index)

def update_question(request):
    if 'user' not in request.session:
        return redirect(admin_login)
    data=request.GET
    question_id=data.get('id')
    question_query = Questionnaire.objects.get(id = question_id)
    category_query = Category.objects.all()

    context={
        "question_id":question_id,
        "question":question_query,
        "category_all": category_query,
    }
    return render(request, "dating_admin/update_question.html",context)

def update_add_question(request, id):
    if 'user' not in request.session:
        return redirect(admin_login)
    question = Questionnaire.objects.get(id =id)
    question.question_content = request.POST['question_content']
    question.question_type =request.POST['question_type'] 
    cate_query = Category.objects.get(id = request.POST['category_option'])
    question.category=cate_query
    question.save()
    return redirect(admin_index)

def add_choice(request):
    if 'user' not in request.session:
        return redirect(admin_login)
    question_query = Questionnaire.objects.get(id =request.POST['question_option'])
    choice = Choice.objects.create(choice_content= request.POST['question_choice'], questions= question_query)
    return redirect(admin_index)

def delete_choice(request, id):
    if 'user' not in request.session:
        return redirect(admin_login)
    choice_query = Choice.objects.get(id =id)
    choice_query.delete()
    return redirect(admin_index)

def update_choice(request):
    if 'user' not in request.session:
        return redirect(admin_login)
    data=request.GET
    choice_id=data.get('id')    
    question_query = Questionnaire.objects.all()
    query = Choice.objects.get(id =choice_id)
    context={
        "choice_id":choice_id,
        "questions_all":question_query,
        "choice":query,
    }
    return render(request, "dating_admin/update_choice.html",context)


def update_add_choice(request, id):
    if 'user' not in request.session:
        return redirect(admin_login)
    choice= Choice.objects.get(id= id)
    choice.choice_content = request.POST['question_choice']
    question_query = Questionnaire.objects.get(id = request.POST['question_option'])
    choice.questions =question_query
    choice.save()
    return redirect(admin_index)
    