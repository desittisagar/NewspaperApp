from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		#fields = UserCreationForm.Meta.fields + ('age',)
		fields = ('username', 'email', 'age',)

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		#fields = UserChangeForm.Meta.fields
		fields = ('username', 'email', 'age',)
# 		

# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser


# class CustomUserCreationForm(UserCreationForm):
# 	class Meta(UserCreationForm.Meta):
# 		model = CustomUser
# 		fields = UserCreationForm.Meta.fields + ('age',)


# class CustomUserChangeForm(UserChangeForm):
# 	class Meta:
# 		model = CustomUser
# 		fields = UserChangeForm.Meta.fields