from django.urls import path
from App_3 import views


app_name = 'App_3'

urlpatterns = [
    path('',views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
]