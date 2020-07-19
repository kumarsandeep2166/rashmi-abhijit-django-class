from django.shortcuts import render

# Create your views here.
def posts(request):
    return render(request, 'post.html')

def index(request):
    return render(request, 'index.html')

def blogs(request):
    return render(request, 'blog.html')