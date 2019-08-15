from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from AppTwo.models import Users
from AppTwo.forms import NewUserForm, UserForm, UserProfileInfoForm
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
	#return HttpResponse('<em>My Second App</em>')
	return render(request, 'sec_app/welcome.html')

def help(request):
	helpdict = {'help_insert': 'Help Page'}
	return render(request, 'sec_app/help.html', context=helpdict)

#def signup(request):
#	return render(request, 'sec_app/sign_up.html')

def user(request):
	user_list = Users.objects.order_by('last_name')
	user_dict = {'users': user_list}
	return render(request, 'sec_app/user.html', context=user_dict)

def signup(request):
	form = NewUserForm()

	if request.method == 'POST': #if someone hit the submit button
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request) #return to homepage
		else:
			print('Error form invalid')

	return render(request, 'sec_app/sign_up.html', {'form':form})

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request, 'sec_app/registration.html', {'user_form': user_form,
														 'profile_form': profile_form,
														 'registered':registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('welcome'))
			else:
				return HttpResponse('Account not active')
		else:
			print('Someone tried to login and failed')
			print('Username: {} and password {}'.format(username, password))
			return HttpResponse('invalid login details supplied')
	else:
		return render(request, 'sec_app/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
	return HttpResponse('You are logged in')





















