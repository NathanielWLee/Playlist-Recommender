# Will take a model in Python and translate into JSON response
# from rest_framework import serializers
# from .models import ChatBox
from rest_framework import serializers
# from .models import Room#Playlist#, Authorize

# # serializes a chatbox object
# class ChatBoxSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChatBox
#         fields = ('id', 'user', 'mood', 'username', 'password')

# # serializes a request
# class CreateChatBoxSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChatBox
#         # only send the fields that we want to be sent as a part of the post request
#         fields = ['mood'] 

# serializes a playlist object
# class PlaylistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Playlist
#         fields = ('id', 'user', 'mood', 'numSongs')

# # serializes a request
# class CreatePlaylistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Playlist
#         # only send the fields that we want to be sent as a part of the post request
#         fields = ['mood', 'numSongs'] 

# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = '__all__'#('host','temp_var')

# class CreateRoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = '__all__'#('temp_var')