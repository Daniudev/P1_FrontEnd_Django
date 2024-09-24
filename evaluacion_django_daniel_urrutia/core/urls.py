from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path ('', views.login, name='login'),
    path ('/register', views.register, name='register'),
    path ('/index', views.index, name='index'),
    path ('/contact', views.contact, name='contact'),
]