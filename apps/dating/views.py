from django.shortcuts import render

def index(request):
    return render(request, 'dating/profile_index.html')

def get_profile_index(request):
    return render(request, 'dating/profile_index.html')

def get_profile(request):
    return render(request, 'dating/my_profile.html')

def get_questions_answers(request):
    return render(request, 'dating/questions_answers.html')

def get_statistics(request):
    return render(request, 'dating/activity_statistics.html')