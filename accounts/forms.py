from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):

	email = forms.CharField(max_length=256, required=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
		widgets = {
			'email': forms.EmailInput()
		}