from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Post, Author, Category, PostView
from marketing.models import Signup
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, PostForm
from django.views.generic import View, CreateView, UpdateView, ListView, DeleteView, DetailView
from marketing.forms import EmailSignupForm
# Create your views here.

form = EmailSignupForm()

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def get_category_count():
    category_count = Post.objects.values('categories__title').annotate(Count('categories__title'))
    # to count howmany times the object has been used and the result always stored in an dictionary
    # print(category_count)
    return category_count

def search(request):
    post = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = post.filter(
            Q(title__icontains=query)|
            Q(overview__icontains=query) 
        ).distinct()
    context = {
        'queryset':queryset
    }
    return render(request, 'search_results.html', context)

class SearchView(View):
    def search(self, request, *args, **kwargs):
        post = Post.objects.all()
        query = request.GET.get('q')
        if query:
            queryset = post.filter(
                Q(title__icontains=query)|
                Q(overview__icontains=query) 
            ).distinct()
        context = {
            'queryset':queryset
        }
        return render(request, 'search_results.html', context)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.filter(featured=True)
        latest = Post.objects.order_by('-timestamp')[0:3]
        context = {
            'queryset':queryset,
            'latest':latest,
            'form':form
        }
        return render(request, 'index.html' , context)
    
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        new_email = EmailSignupForm()
        # assign the email value which is retrieved from the html form
        new_email.email = email
        new_email.save()
        return redirect('home')

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


class BlogListView(ListView):
    model = Post
    form = EmailSignupForm()
    template_name = 'blog.html'
    context_object_name = 'queryset'
    paginate_by = 4
    allow_empty = True
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_post'] = Post.objects.order_by('-timestamp')[:3]
        context['category_count'] = get_category_count()
        context['form'] = self.form
        return context


def blogs(request):
    category_count  = get_category_count()
    post_list = Post.objects.all()
    latest_post = Post.objects.order_by('-timestamp')[:3]
    paginator = Paginator(post_list,4)
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

class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    form = CommentForm

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(post=obj, user=self.request.user)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_post'] = Post.objects.order_by('-timestamp')[:3]
        context['page_request_var'] = 'page'
        context['category_count'] = get_category_count()
        context['form'] = self.form
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'pk':post.pk
            }))

    




def posts(request, pk):
    category_count  = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post, pk=pk)
    
    if request.user.is_authenticated:
        PostView.objects.get_or_create(post=post, user=request.user)

    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save(commit=True)
            return redirect(reverse('post-detail', kwargs={'pk':post.pk}))
    
    context = {
        'form':form,
        'category_count':category_count,
        'most_recent':most_recent,
        'post':post,
    }
    return render(request, 'post.html', context)

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.user = get_author(self.request.user)
        form.save()
        return redirect(reverse('post-detail', kwargs={
                'pk':form.instance.pk
            }))
 



def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        form.instance.author = get_author(request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'pk':form.instance.id
            }))
    context = {
        'title':title,
        'form':form
    }
    return render(request, 'post_create.html', context)

def post_update(request, pk):
    title = 'Update'
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST":        
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'pk':form.instance.id
            }))
    context = {
        'title':title,
        'form':form,
    }
    return render(request, 'post_create.html', context)

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect(reverse('blogs'))