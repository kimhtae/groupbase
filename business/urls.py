from django.urls import path, include
from . import views 

app_name='business'

urlpatterns = [
	path('info_search/', views.info_search, name='info_search'),

]

