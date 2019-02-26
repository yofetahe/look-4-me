from django.shortcuts import render

def admin_index(request):
    return render(request, 'dating_admin/index.html')

def questions_answers(request):
    return render(request, 'dating_admin/questions_answers.html')

def app_members(request):
    context = {
        "arrays": [1,2,3,4,5,6]
    }
    return render(request, 'dating_admin/app_members.html', context)