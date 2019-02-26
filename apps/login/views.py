from django.shortcuts import render

def login(request):
    return render(request, 'login/index.html')

def homepage(request):
    return render(request,'login/homepage.html')


def search(request):
    return render(request,'login/search.html')


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
    return render(request,'login/user_info.html',)


def message_like(request):
    return render(request,'login/message_like.html',)

