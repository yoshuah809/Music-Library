from django.urls import path, include
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    #path('127.0.0.1:8000/', views.SongList.as_view()),
    

]