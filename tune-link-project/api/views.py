from django.shortcuts import render
from html5lib import serialize
from django.http import HttpResponse
from rest_framework import generics, status
# from .serializers import RoomSerializer#, CreateRoomSerializer#PlaylistSerializer, CreatePlaylistSerializer#, AuthorizeSerializer
from .models import Room#Playlist#Authorize
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# def main(request):
#     return HttpResponse("Hello, World!")

# class RoomView(generics.ListAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer

# class CreateRoomView(APIView):
#     serializer_class = CreateRoomSerializer

#     def post(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             # guest_can_pause = serializer.data.get('guest_can_pause')
#             # votes_to_skip = serializer.data.get('votes_to_skip')
#             temp_var = serializer.data.get('temp_var')
#             host = self.request.session.session_key
#             queryset = Room.objects.filter(host=host)
#             if queryset.exists():
#                 room = queryset[0]
#                 # room.guest_can_pause = guest_can_pause
#                 # room.votes_to_skip = votes_to_skip
#                 room.temp_var = temp_var
#                 # room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
#                 room.save(update_fields=['temp_var'])
#                 return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
#             else:
#                 room = Room(host=host, temp_var=temp_var)
#                 room.save()
#                 return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

#         return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

# class PlaylistView(generics.CreateAPIView):
#     queryset = Playlist.objects.all()
#     serializer_class = PlaylistSerializer

# class CreatePlaylistView(APIView): # APIView is the base class; lets us override default methods
#     serializer_class = CreatePlaylistSerializer

#     # dispatches post requests (that were sent to this APIView) to the correct method
#     def post(self, request, format=None):
        
#         # Need to access session key to identify user
#         # if there isn't already a session, create one
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             mood = serializer.data.get('mood')
#             numSongs = serializer.data.get('numSongs')
#             user = self.request.session.session_key

#             # Check if user visited recently, update their playlist instead of creating new
#             queryset = Playlist.objects.filter(user=user)
#             if (queryset.exists)():
#                 playlist = queryset[0]
#                 # update params
#                 playlist.mood = mood
#                 playlist.numSongs = numSongs
#                 playlist.save(update_fields=['mood', 'numSongs'])
#                 # Return the playlist in a json format and let the user know it was a valid request
#                 return Response(PlaylistSerializer(playlist).data, status=status.HTTP_200_OK)
#             else: # Create a new playlist
#                 playlist = Playlist(user=user,mood=mood, numSongs=numSongs)
#                 playlist.save()
#                 # Return the playlist in a json format and let the user know it was created
#                 return Response(PlaylistSerializer(playlist).data, status=status.HTTP_201_CREATED)

#         return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)