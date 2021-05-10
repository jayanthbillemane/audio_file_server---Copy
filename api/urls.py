from django.urls import path
from .import views

urlpatterns = [



    path('song-list/', views.songList, name="song-list"),
	path('song-create/', views.songCreate, name="song-create"),
	path('song-update/<str:pk>/', views.songUpdate, name="song-update"),	
	path('song-delete/<str:pk>/', views.songDelete, name="song-delete"),

    path('podcast-list/', views.podcastList, name="poscast-list"),
	path('podcast-update/<str:pk>/', views.podcastUpdate, name="podcast-update"),    
	path('podcast-create/', views.podcastCreate, name="poscast-create"),
	path('podcast-delete/<str:pk>/', views.podcastDelete, name="poscast-delete"),


    path('audiobook-list/', views.audiobooktList, name="poscast-list"),
	path('audiobook-update/<str:pk>/', views.audiobookUpdate, name="audiobook-update"),    
	path('audiobook-create/', views.audiobookCreate, name="poscast-create"),
	path('audiobook-delete/<str:pk>/', views.audiobookDelete, name="poscast-delete"),






]
