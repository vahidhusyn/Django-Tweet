from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    text = forms.CharField(
        label="Write your blog-",
        widget=forms.Textarea(
            attrs={'class': ''})
    )
    photo = forms.ImageField(
        label="Upload your image-",
        widget=forms.ClearableFileInput(
            attrs={'class': ''}
        )
    )
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
