from django.forms import ModelForm
from .models import *

class NewPostForm(ModelForm):

    class Meta:
        model =  Post
        fields = ['title', 'text', 'author', 'published']