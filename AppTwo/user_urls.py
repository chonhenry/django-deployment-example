#from django.conf.urls import url
from AppTwo import views
from django.urls import path

#template tagging
app_name = 'app_two'

urlpatterns = [
	path('', views.user, name='user'),
	path('sign_up', views.signup, name='signup'),
	path('register', views.register, name='register'),
	path('login', views.user_login, name='login'),
	path('logout', views.user_logout, name='user_logout'),
]