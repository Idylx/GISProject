from django.urls import path

from . import views

urlpatterns = [
    #path('',views.index, name='index'),
    path('status/', views.status, name='status'),
    path('difficulty/', views.difficulty, name='difficulty'),
    path('infos/', views.infos, name='infos'),
    path('slopesdata', views.slopesdata, name='slopesdata'),
    path('restaurantsdata', views.restaurantsdata, name='restaurantsdata'),
    path('grenouilleresdata', views.grenouilleresdata, name='grenouilleresdata'),
    path('parkingsdata', views.parkingsdata, name='parkingsdata'),
    path('liftsdata', views.liftsdata, name='liftsdata'),
    path('', views.infos, name='infos'),



]