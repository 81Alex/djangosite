from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name='index'),
    path('registrastion/', views.registrastion, name='registrastion'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('main_menu/', views.main_menu, name='main_menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]