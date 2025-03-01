from django import forms
from .models import NewPost

class PostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ('post',)
        labels = {
            "post": (""),
            }
        widgets = {
            "post": forms.Textarea(attrs={'placeholder': 'Write new post...','class': 'form-control', 'rows':3, 'style':'width: 90%;'}),
        }
   
