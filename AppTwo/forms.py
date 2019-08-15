from django import forms
from AppTwo.models import Users, UserProfileInfo
from django.contrib.auth.models import User

class NewUserForm(forms.ModelForm):
	verify_email = forms.EmailField(label='Enter your email again:')
	class Meta():
		model = Users
		#field = '__all__'
		exclude = ()

	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']

		if email != vmail:
			raise forms.ValidationError('Make sure email match')

class UserForm(forms.ModelForm):
	#password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
	#portfolio = forms.URLField(required=False)
	#picture = forms.ImageField(required=False)
	class Meta():
		model = UserProfileInfo
		exclude = ('user',)