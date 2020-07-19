from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Comment, Post
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('komentar',)

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

