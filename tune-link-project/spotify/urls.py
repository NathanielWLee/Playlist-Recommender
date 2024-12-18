from django.urls import path
from .views import AuthURL, spotify_callback, IsAuthenticated, CreatePlaylist
# from .util import 
# from .spotify_function import create_playlist

urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('redirect', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view()),
    path('create-playlist', CreatePlaylist.as_view()) # make another url from button pressed to spotify_functions in home page
]
