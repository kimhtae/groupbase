from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [

    url('', views.index, name = 'index'),
    url('business_kpi/', views.business_kpi, name = 'business_kpi'),

]