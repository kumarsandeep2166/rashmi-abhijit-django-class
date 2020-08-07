from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField

# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media/profile/')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post',related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class PostView(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # comment_count = models.IntegerField()
    # view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    thumbnail = models.ImageField(upload_to='media/')
    featured = models.BooleanField()
    content = HTMLField('content')
    previous_post = models.ForeignKey('self',related_name='previous',on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next',on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    # look_up_field = 'id'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'pk':self.pk
        })
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()
    
    def get_update_url(self):
        return reverse('post-update',kwargs={
            'id':self.id
        })
    def get_delete_url(self):
        return reverse('post-delete',kwargs={
            'id':self.id
        })

