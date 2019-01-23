from django.urls import path, include
from django.conf.urls import url
#from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views 



urlpatterns = [
	path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
	
	path('logout/', LogoutView.as_view(), name='logout', kwargs={
		'next_page': '/',
	}),
	path('signup/', views.signup, name='signup'),
	path('profile/', views.profile, name='profile'),
    path('password_change', views.change_password, name='password_change'),
	
	# path('password_change/', auth_views.password_change, 
	# {'post_change_redirect':'/password_change/done/'}),
	# path('password_change/done/', auth_views.password_change_done),
	
	#path('password_reset/', views.reset_password, name='password_reset'),
	path('reset_password/', PasswordResetView.as_view(), name='password_reset'),
	path('reset_password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
	url('reset_password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset_password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

