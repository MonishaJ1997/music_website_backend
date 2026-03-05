from django.urls import path
from .views import get_album_songs, get_all_songs,get_single_song
from .views import AuthBannerListView,FilmListView
from .views import RegisterView, LoginView,LogoutView,CheckAuthView
from . import spotify_views
from .views import SongSearchView


urlpatterns = [
    path("songs/", get_all_songs, name="all-songs"),
    path('song/<int:song_id>/', get_single_song),
   # urls.py
path('album/<int:film_id>/', get_album_songs, name='album-songs'),
    path('auth-banner/', AuthBannerListView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
   path("logout/", LogoutView.as_view()),
    path("check-auth/", CheckAuthView.as_view()),
    path("films/", FilmListView.as_view()),
    
    path("spotify/token/", spotify_views.spotify_token),
 
    path("songs/search/", SongSearchView.as_view()),
]



