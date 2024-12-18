from django.shortcuts import render, redirect
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from .util import *
from curses.ascii import SP
import json
import random
import requests
import logging
from .models import SpotifyToken

# Create your views here.

# View that authenticates our user/requests access
class AuthURL(APIView):

    # API endpoint that returns to us a url that will allow us to authenticate user
    def get(self, request, format=None):

        # What information we want to access..just be able modfiy user playlist.
        # Can add more here
        scopes = 'playlist-modify-private playlist-modify-public user-top-read'

        # state params is optional
        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code', # we are requesting we get sent a code back that will allow us to authenticate the user
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)

def spotify_callback(request, format=None):

    # code is how we authenticate our user
    code = request.GET.get('code')
    error = request.GET.get('error')

    # automatically send request, get response and turn that into json
    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    # We need to store this token for each user that is on our website
    # Create a database for each user using our website...all access and refresh tokens
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(request.session.session_key, access_token, token_type, expires_in, refresh_token)

    # return back to our original application
    return redirect('frontend:')

# End point we can hit that tells us whether or not we are authenticated
class IsAuthenticated(APIView):

    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(self.request.session.session_key)
        return Response({'status': is_authenticated}, status=status.HTTP_200_OK)

class CreatePlaylist(APIView):
    def get(self, response, format=None):
        #create_playlist(self.request.session.session_key)
        create_playlist()

# def create_playlist(self, format=None):#, lex_response):
#     # SETTINGS for Spotify
#     endpoint_url = "https://api.spotify.com/v1/recommendations?"

#     token = SpotifyToken.access_token
#     user_id = SpotifyToken.user

#     logging.basicConfig(level=logging.NOTSET)
#     logging.debug(token)
#     logging.debug(user_id)

#     # OUR FILTERS for Spotify
#     limit=50
#     market="US"
    
#     # Remove this once received lex response
#     lex_response = {"ResponseMetadata": {"RequestId": "c856d2ab-4fe9-49d0-a04f-32b5083995c5", "HTTPStatusCode": 200, "HTTPHeaders": {"x-amzn-requestid": "c856d2ab-4fe9-49d0-a04f-32b5083995c5", "date": "Tue, 19 Apr 2022 20:42:15 GMT", "content-type": "application/json", "content-length": "2914"}, "RetryAttempts": 0}, "messages": [{"content": "Perfect! We\u2019ve uploaded your playlist to Spotify. Enjoy!", "contentType": "PlainText"}, {"content": "Thanks for using Tune Link!", "contentType": "PlainText"}], "sessionState": {"dialogAction": {"type": "Close"}, "intent": {"name": "CreatePlaylist", "slots": {"Acoustic": {"value": {"originalValue": "I like electronic music!", "interpretedValue": "I like electronic music!", "resolvedValues": ["I like electronic music!"]}}, "Danceability": {"value": {"originalValue": "yes", "interpretedValue": "yes", "resolvedValues": ["Yes!"]}}, "Energy": {"value": {"originalValue": "Energized", "interpretedValue": "Energized", "resolvedValues": ["Energized!"]}}, "EnergyHigh": {"value": {"originalValue": "no", "interpretedValue": "no", "resolvedValues": ["No"]}}, "EnergyLow": None, "Familiarity": {"value": {"originalValue": "A bit of both", "interpretedValue": "A bit of both", "resolvedValues": ["A bit of both."]}}, "Instrumentalness": {"value": {"originalValue": "pass me the mic", "interpretedValue": "pass me the mic", "resolvedValues": ["Pass me the mic!"]}}, "Liveness": {"value": {"originalValue": "It doesn't matter!", "interpretedValue": "It doesn't matter!", "resolvedValues": ["It doesn't matter!"]}}, "Loudness": {"value": {"originalValue": "bring it on", "interpretedValue": "bring it on", "resolvedValues": ["Bring it on!"]}}, "Valence": {"value": {"originalValue": "I'm okay.", "interpretedValue": "I'm okay.", "resolvedValues": ["I'm okay. :/"]}}, "ValenceLow": None}, "state": "Fulfilled", "confirmationState": "None"}, "sessionAttributes": {}, "originatingRequestId": "4eb464af-d94c-4c71-9764-a71ff3e147ca"}, "interpretations": [{"nluConfidence": {"score": 1.0}, "intent": {"name": "CreatePlaylist", "slots": {"Acoustic": {"value": {"originalValue": "I like electronic music!", "interpretedValue": "I like electronic music!", "resolvedValues": ["I like electronic music!"]}}, "Danceability": {"value": {"originalValue": "yes", "interpretedValue": "yes", "resolvedValues": ["Yes!"]}}, "Energy": {"value": {"originalValue": "Energized", "interpretedValue": "Energized", "resolvedValues": ["Energized!"]}}, "EnergyHigh": {"value": {"originalValue": "no", "interpretedValue": "no", "resolvedValues": ["No"]}}, "EnergyLow": None, "Familiarity": {"value": {"originalValue": "A bit of both", "interpretedValue": "A bit of both", "resolvedValues": ["A bit of both."]}}, "Instrumentalness": {"value": {"originalValue": "pass me the mic", "interpretedValue": "pass me the mic", "resolvedValues": ["Pass me the mic!"]}}, "Liveness": {"value": {"originalValue": "It doesn't matter!", "interpretedValue": "It doesn't matter!", "resolvedValues": ["It doesn't matter!"]}}, "Loudness": {"value": {"originalValue": "bring it on", "interpretedValue": "bring it on", "resolvedValues": ["Bring it on!"]}}, "Valence": {"value": {"originalValue": "I'm okay.", "interpretedValue": "I'm okay.", "resolvedValues": ["I'm okay. :/"]}}, "ValenceLow": None}, "state": "Fulfilled", "confirmationState": "None"}}, {"intent": {"name": "FallbackIntent", "slots": {}}}], "sessionId": "taylor_session"}

#     # Start Spotify query here
#     query = f'{endpoint_url}limit={limit}&market={market}'

#     # Maybe if the values weren't able to be resolved, we remove them from the query?
#     # Acoustic
#     # Maybe we can incorporate min and max values for these as well
#     # min acousticness and max acousticness

#     if lex_response['interpretations'][0]['intent']['slots']['Acoustic']['value']['resolvedValues']:
#         acoustic = lex_response['interpretations'][0]['intent']['slots']['Acoustic']['value']['resolvedValues'][0]

#         if (acoustic == 'I like electronic music!'):
#             target_acousticness = 0.1 # low acousticness
#         elif (acoustic == 'I prefer music from instruments!'):
#             target_acousticness = 0.9 # high acousticness
#         elif (acoustic == 'A bit of both!'):
#             target_acousticness = 0.5 # mid acousticness
#         else:
#             target_acousticness = 0.5 # What do we do about unresolved values?
#     else:
#         target_acousticness = 0.5


#     # Danceability
#     if lex_response['interpretations'][0]['intent']['slots']['Danceability']['value']['resolvedValues']:
#         danceability = lex_response['interpretations'][0]['intent']['slots']['Danceability']['value']['resolvedValues'][0]

#         if (danceability == 'Yes!'):
#             target_danceability = 0.9 # high danceability
#         elif (danceability == 'Eh, try me!'):
#             target_danceability = 0.5 # mid danceability
#         elif (danceability == 'No.'):
#             target_danceability = 1.0 # low daneability
#         else:
#             target_danceability = 0.5 # what do we do about unresolved values?
#     else:
#         target_danceability = 0.5

#     # Energy (including EnergyHigh and EnergyLow)
#     if lex_response['interpretations'][0]['intent']['slots']['Energy']['value']['resolvedValues']:

#         energy = lex_response['interpretations'][0]['intent']['slots']['Energy']['value']['resolvedValues'][0]

#         if (energy == 'Energized!'):

#             target_energy = 0.9 # high energy values

#             # Look at value for EnergyHigh
#             if lex_response['interpretations'][0]['intent']['slots']['EnergyHigh']['value']['resolvedValues']:
#                 energy_high = lex_response['interpretations'][0]['intent']['slots']['EnergyHigh']['value']['resolvedValues'][0]

#                 if (energy_high == 'Yes'):
#                     target_energy = target_energy - 0.5 # lower target_energy to be more relaxing
#                 elif (energy_high == 'No'):
#                     target_energy = target_energy - 0 # leave target_energy unchanged
#                 else:
#                     target_energy = 0.5 # what do we do if the value is unresolved?
#             else:
#                 target_energy = 0.5


#         elif (energy == 'Slowly waking myself up.'):
#             target_energy = 0.5 # mid-energy values

#         elif (energy == 'Completely exhausted.'):

#             target_energy = 0.1 # low energy values

#             # Look at value for EnergyLow
#             if lex_response['interpretations'][0]['intent']['slots']['EnergyLow']['value']['resolvedValues']:
#                 energy_low = lex_response['interpretations'][0]['intent']['slots']['EnergyLow']['value']['resolvedValues'][0]
#                 if (energy_low == 'Yes, awake me from this mess'):
#                     target_energy = target_energy + 0.5 # increase target_energy value to be more energetic
#                 elif (energy_low == 'No, I wanna fall asleep'):
#                     target_energy = target_energy + 0 # leave target_energy unchanged
#                 else:
#                     target_energy = 0.5 # what do we do if the value is unresolved?
#             else:
#                 target_energy = 0.5

#         else:
#             target_energy = 0.5 # what do we do if the value is unresolved?
#     else:
#         target_energy = 0.5


#     # Familiarity
#     if lex_response['interpretations'][0]['intent']['slots']['Familiarity']['value']['resolvedValues']:
#         familiarity = lex_response['interpretations'][0]['intent']['slots']['Familiarity']['value']['resolvedValues'][0]

#         # Generate random two genres as seeds
#         genre_response = requests.get("https://api.spotify.com/v1/recommendations/available-genre-seeds",
#                                     headers={"Content-Type": "application/json",
#                                     "Authorization": f"Bearer {token}"})
#         genre_json_response= genre_response.json()
#         genre_parsed = genre_json_response['genres']
#         genre_seeds = random.sample(genre_parsed, 2)
#         seed_genres = ",".join(genre_seeds)
#         #print(seed_genres)

#         # Generate user's top three artists as seeds
#         top_items_response = requests.get(f"https://api.spotify.com/v1/me/top/artists?limit=3",
#                                 headers={"Content-Type": "application/json",
#                                         "Authorization": f"Bearer {token}"})
#         top_items_json_response = top_items_response.json()

#         top_items_parsed_1 = top_items_json_response['items'][0]['id']
#         top_items_parsed_2 = top_items_json_response['items'][1]['id']
#         top_items_parsed_3 = top_items_json_response['items'][2]['id']

#         seed_artists = top_items_parsed_1 + "," + top_items_parsed_2 + "," + top_items_parsed_3
#         #print(seed_artists)

#         if (familiarity == 'Yes!'):

#             # User wants entirely new music, concatenate seed_genres to QUERY
#             query += f'&seed_genres={seed_genres}'

#         elif (familiarity == 'No, only the songs I know.'):

#             # User wants only their own music, concatenate seed_artists to QUERY
#             query += f'&seed_artists={seed_artists}'

#         elif (familiarity == 'A bit of both.'):

#             # User wants a mix , concatenate both seed_genres and seed_artists to QUERY
#             query += f'&seed_genres={seed_genres}&seed_artists={seed_artists}'
#         else:
#             query += f'&seed_genres={seed_genres}&seed_artists={seed_artists}' # How to deal with unresolved values?
#     else:
#         query += f'&seed_genres={seed_genres}&seed_artists={seed_artists}'

#     # Instrumentalness
#     if lex_response['interpretations'][0]['intent']['slots']['Instrumentalness']['value']['resolvedValues']:
#         instrumentalness = lex_response['interpretations'][0]['intent']['slots']['Instrumentalness']['value']['resolvedValues'][0]

#         if (instrumentalness == 'Pass me the mic!'):
#             target_instrumentalness = 0.1 # low instrumental value
#         elif (instrumentalness == 'I don\'t mind.'):
#             target_instrumentalness = 0.5 # mid-instrumental value
#         elif (instrumentalness == 'I just want to zone out.'):
#             target_instrumentalness = 0.9 # high instrumental value
#         else:
#             target_instrumentalness = 0.5 # How to deal with unresolved values?
#     else:
#         target_instrumentalness = 0.5

#     # Liveness
#     if lex_response['interpretations'][0]['intent']['slots']['Liveness']['value']['resolvedValues']:
#         liveness = lex_response['interpretations'][0]['intent']['slots']['Liveness']['value']['resolvedValues'][0]

#         if (liveness == 'Yes!'):
#             target_liveness = 0.9 # filter for live music
#         elif (liveness == 'No.'):
#             target_liveness = 0.1 # filter for not-live music
#         elif (liveness == 'It doesn\'t matter!'):
#             target_liveness = 0.5 # mid values
#         else:
#             target_liveness = 0.5 # How to deal with unresolved values?
#     else:
#         target_liveness = 0.5

#     # Loudness
#     if lex_response['interpretations'][0]['intent']['slots']['Loudness']['value']['resolvedValues']:
#         loudness = lex_response['interpretations'][0]['intent']['slots']['Loudness']['value']['resolvedValues'][0]

#         if (loudness == 'Bring it on!'):
#             target_loudness = 0 # high loutdness
#         elif (loudness == 'Kind of.'):
#             target_loudness = -20 # mid loudness
#         elif (loudness == 'Not really.'):
#             target_loudness = -40 # low loudness (softer music)
#         else:
#             target_loudness = -20 # How to deal with unresolved values?
#     else:
#         target_loudness = -20

#     # Valence (including Valence low)
#     if lex_response['interpretations'][0]['intent']['slots']['Valence']['value']['resolvedValues']:
#         valence = lex_response['interpretations'][0]['intent']['slots']['Valence']['value']['resolvedValues'][0]

#         if (valence == 'I\'m feeling great! :)'):

#             target_valence = 0.9 # a high value

#         elif (valence == 'I\'m okay. :('):
#             target_valence = 0.5 # mid values

#         elif (valence == 'I\'ve been better. :('):

#             target_valence = 0.1

#             # Look at value for ValenceLow

#             if lex_response['interpretations'][0]['intent']['slots']['ValenceLow']['value']['resolvedValues']:
#                 valence_low = lex_response['interpretations'][0]['intent']['slots']['ValenceLow']['value']['resolvedValues'][0]

#                 if (valence_low == 'Yes'):
#                     target_valence = target_valence + 0.5 # a high value
#                 elif (valence_low == 'No'):
#                     target_valence = target_valence + 0 # leave target value unchanged
#                 else:
#                     target_valence = 0.5 # what do we do if the value is unresolved?
#             else:
#                 target_valence = 0.5

#         else:
#             target_valence = 0.5 # what do we do if the value is unresolved?
#     else:
#         target_valence = 0.5

#     # Down here, we make the spotify query
#     uris = []

#     # Add additional items to query (acousticness, energy, danceability, instrumentalness, liveness, loudness, valence)
#     query += f'&target_acousticness={target_acousticness}'
#     query += f'&target_energy={target_energy}'
#     query += f'&target_danceability={target_danceability}'
#     query += f'&target_instrumentalness={target_instrumentalness}'
#     query += f'&target_liveness={target_liveness}'
#     query += f'&target_loudness={target_loudness}'
#     query += f'&target_valence={target_valence}'

#     print(query)

#     response = requests.get(query,
#                 headers={"Content-Type":"application/json",
#                             "Authorization":f"Bearer {token}"})
#     json_response = response.json()

#     print('Recommended Songs:')
#     for i,j in enumerate(json_response['tracks']):
#                 uris.append(j['uri'])
#                 print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

#     request_body = json.dumps({
#             "name": "My Tune Link Playlist",
#             "description": "My custom playlist created by the Tune Link Chat Service",
#             "public": False
#             })
#     response = requests.post(url = f"https://api.spotify.com/v1/users/{user_id}/playlists", data = request_body, headers={"Content-Type":"application/json",
#                             "Authorization":f"Bearer {token}"})

#     #print(response.status_code)

#     playlist_id = response.json()['id']

#     request_body = json.dumps({
#             "uris" : uris
#             })

#     response = requests.post(url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", data = request_body, headers={"Content-Type":"application/json",
#                             "Authorization":f"Bearer {token}"})


