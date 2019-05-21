from django.urls import path

from . import views

urlpatterns = [
    #path('',views.index, name='index'),
    path('status/', views.status, name='status'),
    path('difficulty/', views.difficulty, name='difficulty'),
    path('infos/', views.infos, name='infos'),

]