from email.policy import default
from enum import unique
from pyexpat import model
from django.db import models

def generate_playlist():
    print("Playlist created.")

# class Room(models.Model):
#     host = models.CharField(max_length=50, unique=True)
#     temp_var = models.BooleanField(null=False, default=True)

# class Room(models.Model):
#     user = models.CharField(max_length=50, default="", unique=True)
#     mood = models.CharField(max_length=15, default="")
#     numSongs = models.IntegerField(default=1)