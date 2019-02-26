from django.shortcuts import render, redirect

def dating_index(request):
    return render(request, 'dating/my_matches.html')

def get_profile_index(request):
    return render(request, 'dating/mp_profile_index.html')

def get_profile(request):
    return render(request, 'dating/mp_my_profile.html')

def get_questions_answers(request):
    return render(request, 'dating/mp_questions_answers.html')

def get_statistics(request):
    return render(request, 'dating/mp_activity_statistics.html')


   
def my_matches(request):
    return render(request,'dating/my_matches.html')


def search_matches(request):
    return render(request,'dating/search_matches.html')


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


def user_info_display(request,userid):
    return render(request,'dating/user_info.html',)


def messages_likes(request):
    return render(request,'dating/message_like.html',)

def logout(request):
    print("logout")
    return redirect('../login/')

