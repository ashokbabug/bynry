from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User  #here if u save the form it get into User model or in simple the form save to user
		fields = ['username','email','password1','password2']
		
class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['full_name','address','phone']
	