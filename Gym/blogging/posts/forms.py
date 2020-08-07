from django import forms
from .models import Author, Post, Comment, Category
from tinymce import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCEWidget(attrs={'required':False,'cols':10, 'rows':5}))
    class Meta:
        model = Post
        fields = ('title','overview','content','thumbnail','categories','featured','previous_post','next_post')

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Type your comment',
        'id':"usercomment",
        'rows':'4',
    }))
    class Meta:
        model = Comment
        fields = ('content',)