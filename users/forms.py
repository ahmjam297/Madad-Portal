from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','password1', 'password2']


class ProfileForm(forms.ModelForm):
	
	class Meta:
		model = Profile
		fields = ['user','UID','residence','room_no','Gender']