from django.shortcuts import render, redirect

def login_index(request):
    return render(request, 'login/index.html')

def register(request):    
    return redirect(getQuestionnaireForm)

def getQuestionnaireForm(request):
    return render(request, 'login/questionnaire.html')

def login(request):
    return redirect('/../dating/')

    