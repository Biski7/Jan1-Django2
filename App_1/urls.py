# from django.conf.urls import url
from App_1 import views
from django.urls import path

urlpatterns = [
    path("",views.index, name="index"),
    path("keanu/", views.help, name='keanu'),
    path('form_1', views.knowledge_view, name='form'),
    path('form_2', views.for_user_view, name='form2')
]
