from django.shortcuts import render
from .models import Post, Author, Category
from marketing.models import Signup
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def get_category_count():
    category_count = Post.objects.values('categories__title').annotate(Count('categories__title'))
    # to count howmany times the object has been used and the result always stored in an dictionary
    print(category_count)
    return category_count

def index(request):
    queryset = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method =="POST":
        # this email variable is called from the form
        email = request.POST['email']
        new_email = Signup()
        # assign the email value which is retrieved from the html form
        new_email.email = email
        new_email.save()

    context = {
        'object_list': queryset,
        'latest':latest,
    }
    return render(request, 'index.html' , context)


def posts(request):
    return render(request, 'post.html')



def blogs(request):
    category_count  = get_category_count()
    post_list = Post.objects.all()
    latest_post = Post.objects.order_by('-timestamp')[:3]
    paginator = Paginator(post_list,2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    context = {
        'post_list':paginated_queryset,
        'latest_post':latest_post,
        'category_count':category_count,
        'page_request_var':page_request_var
    }
    return render(request, 'blog.html',context)