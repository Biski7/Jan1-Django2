from App_2 import views
from django.urls import path

app_name = 'App_2'

urlpatterns = [
    path('', views.index, name='index'),
    path('other', views.other, name='other'),
    path('another', views.another, name='another'),
]
