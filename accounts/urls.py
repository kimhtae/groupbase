from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
	path('login/', auth_views.login, name='login', kwargs={
		'template_name': 'accounts/login_form.html',
	}),
	path('logout/', auth_views.logout, name='logout', kwargs={
		'next_page': '/',
	}),
	path('signup/', views.signup, name='signup'),
	path('profile/', views.profile, name='profile'),
    path('password_change', views.change_password, name='password_change'),
	
	# path('password_change/', auth_views.password_change, 
	# {'post_change_redirect':'/password_change/done/'}),
	# path('password_change/done/', auth_views.password_change_done),
	
	path('password_reset/', views.reset_password, name='password_reset'),
]
