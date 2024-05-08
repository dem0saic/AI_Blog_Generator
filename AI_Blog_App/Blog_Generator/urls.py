from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.usr_login, name='login'),
    path('signup', views.usr_signup, name='signup'),
    path('logout', views.usr_logout, name='logout'),
]
