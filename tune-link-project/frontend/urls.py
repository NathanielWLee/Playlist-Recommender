from django.urls import path
from .views import index

# django neesd to know that this urls.py belongs to the frontend app
app_name = 'frontend'

urlpatterns = [
    path('', index, name=''),
    path('login', index),
    path('create', index),
    path('songs', index)
]
