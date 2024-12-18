import boto3
import json
import random
import requests

# SETTINGS for Spotify
endpoint_url = "https://api.spotify.com/v1/recommendations?"

# Change these every time based on user...hopefully authorization will fix this
# To get token: go to this link below, and select scopes playlist-modify-public, playlist-modify-private, and user-top-read
# https://developer.spotify.com/console/get-recommendations/

token = "BQDYio23AaTKcwb3eWIN_GefUpa9dd_AJhEBfY_E_6xt009xWbL91qmfBjsTbrPRqstjHqmQDuUUp1w91CTWZelj4f6eT5Cyx-eXnAACYgq8woBdpW656GuZ4sL-JBKhLw8tAihezAoep1-IZkzoRWObVlsFSxhyp9Huf1-38MFXLAO8bMMA7GHZHo6LfMA7iJV9Jn9RlJMDL5yls_O6BJnlGop-bIXH3-Bt"
user_id = "apspunky"

# OUR FILTERS for Spotify
limit=50
market="US"

# AWS Credentials
accessKeyID = '' # secret
secretAccessKey = '' # secret

def begin_session(accessKeyID, secretAccessKey):
    client = boto3.client(service_name = 'lexv2-runtime', region_name = 'us-east-1', aws_access_key_id = accessKeyID, aws_secret_access_key = secretAccessKey)
    return client
    #lex_client = boto3.client('lex-runtime', aws_access_key_id = config.aws_access_key_id, aws_secret_access_key = config.aws_secret_access_key , region_name= config.region)

# Helper function to submit text to the bot
def text_to_lex(client, message):
    response = client.recognize_text(
        botId='JG38VXQ0KG',
        botAliasId='TSTALIASID',
        localeId='en_US',
        sessionId="taylor_session",
        text = message)
    return response

client = begin_session(accessKeyID, secretAccessKey)
# Kick off this bitch
msg = json.loads(json.dumps(text_to_lex(client, "create playlist")))

lastSlot = msg['sessionState']['intent']['slots']['Familiarity']
while lastSlot is None:
    question = msg['messages'][0]['content']
    buttons = msg['messages'][1]['imageResponseCard']['buttons']
    print(question)
    for button in buttons:
        print(button['text'])
    userInput = input()
    msg = json.loads(json.dumps(text_to_lex(client, userInput)))
    lastSlot = msg['sessionState']['intent']['slots']['Familiarity']

print(msg['messages'][0]['content'])
print(msg['messages'][1]['content'])

lex_response = json.loads(json.dumps(msg))
print(lex_response)

with open('lex_output.json', 'w') as outfile:
    json.dump(lex_response, outfile)
outfile.close()

# Start Spotify query here
query = f'{endpoint_url}limit={limit}&market={market}'

# Maybe if the values weren't able to be resolved, we remove them from the query?
# Acoustic
# Maybe we can incorporate min and max values for these as well
# min acousticness and max acousticness

if lex_response['interpretations'][0]['intent']['slots']['Acoustic']['value']['resolvedValues']:
    acoustic = lex_response['interpretations'][0]['intent']['slots']['Acoustic']['value']['resolvedValues'][0]

    if (acoustic == 'I like electronic music!'):
        target_acousticness = 0.1 # low acousticness
    elif (acoustic == 'I prefer music from instruments!'):
        target_acousticness = 0.9 # high acousticness
    elif (acoustic == 'A bit of both!'):
        target_acousticness = 0.5 # mid acousticness
    else:
        target_acousticness = 0.5 # What do we do about unresolved values?
else:
    target_acousticness = 0.5


# Danceability
if lex_response['interpretations'][0]['intent']['slots']['Danceability']['value']['resolvedValues']:
    danceability = lex_response['interpretations'][0]['intent']['slots']['Danceability']['value']['resolvedValues'][0]

    if (danceability == 'Yes!'):
        target_danceability = 0.9 # high danceability
    elif (danceability == 'Eh, try me!'):
        target_danceability = 0.5 # mid danceability
    elif (danceability == 'No.'):
        target_danceability = 1.0 # low daneability
    else:
        target_danceability = 0.5 # what do we do about unresolved values?
else:
    target_danceability = 0.5

# Energy (including EnergyHigh and EnergyLow)
if lex_response['interpretations'][0]['intent']['slots']['Energy']['value']['resolvedValues']:

    energy = lex_response['interpretations'][0]['intent']['slots']['Energy']['value']['resolvedValues'][0]

    if (energy == 'Energized!'):

        target_energy = 0.9 # high energy values

        # Look at value for EnergyHigh
        if lex_response['interpretations'][0]['intent']['slots']['EnergyHigh']['value']['resolvedValues']:
            energy_high = lex_response['interpretations'][0]['intent']['slots']['EnergyHigh']['value']['resolvedValues'][0]

            if (energy_high == 'Yes'):
                target_energy = target_energy - 0.5 # lower target_energy to be more relaxing
            elif (energy_high == 'No'):
                target_energy = target_energy - 0 # leave target_energy unchanged
            else:
                target_energy = 0.5 # what do we do if the value is unresolved?
        else:
            target_energy = 0.5


    elif (energy == 'Slowly waking myself up.'):
        target_energy = 0.5 # mid-energy values

    elif (energy == 'Completely exhausted.'):

        target_energy = 0.1 # low energy values

        # Look at value for EnergyLow
        if lex_response['interpretations'][0]['intent']['slots']['EnergyLow']['value']['resolvedValues']:
            energy_low = lex_response['interpretations'][0]['intent']['slots']['EnergyLow']['value']['resolvedValues'][0]
            if (energy_low == 'Yes, awake me from this mess'):
                target_energy = target_energy + 0.5 # increase target_energy value to be more energetic
            elif (energy_low == 'No, I wanna fall asleep'):
                target_energy = target_energy + 0 # leave target_energy unchanged
            else:
                target_energy = 0.5 # what do we do if the value is unresolved?
        else:
            target_energy = 0.5

    else:
        target_energy = 0.5 # what do we do if the value is unresolved?
else:
    target_energy = 0.5


# Familiarity
if lex_response['interpretations'][0]['intent']['slots']['Familiarity']['value']['resolvedValues']:
    familiarity = lex_response['interpretations'][0]['intent']['slots']['Familiarity']['value']['resolvedValues'][0]

    # Generate random two genres as seeds
    genre_response = requests.get("https://api.spotify.com/v1/recommendations/available-genre-seeds",
                                headers={"Content-Type": "application/json",
                                "Authorization": f"Bearer {token}"})
    genre_json_response= genre_response.json()
    genre_parsed = genre_json_response['genres']
    genre_seeds = random.sample(genre_parsed, 2)
    seed_genres = ",".join(genre_seeds)
    #print(seed_genres)

    # Generate user's top three artists as seeds
    top_items_response = requests.get(f"https://api.spotify.com/v1/me/top/artists?limit=3",
                            headers={"Content-Type": "application/json",
                                    "Authorization": f"Bearer {token}"})
    top_items_json_response = top_items_response.json()

    top_items_parsed_1 = top_items_json_response['items'][0]['id']
    top_items_parsed_2 = top_items_json_response['items'][1]['id']
    top_items_parsed_3 = top_items_json_response['items'][2]['id']

    seed_artists = top_items_parsed_1 + "," + top_items_parsed_2 + "," + top_items_parsed_3
    #print(seed_artists)

    if (familiarity == 'Yes!'):

        # User wants entirely new music, concatenate seed_genres to QUERY
        query += f'&seed_genres={seed_genres}'

    elif (familiarity == 'No, only the songs I know.'):

        # User wants only their own music, concatenate seed_artists to QUERY
        query += f'&seed_artists={seed_artists}'

    elif (familiarity == 'A bit of both.'):

        # User wants a mix , concatenate both seed_genres and seed_artists to QUERY
        query += f'&seed_genres={seed_genres}&seed_artists={seed_artists}'
    else:
        query += f'&seed_genres={seed_genres}&seed_artists={seed_artists}' # How to deal with unresolved values?
else:
    query += f'&seed_genres={seed_genres}&seed_artists={seed_artists}'

# Instrumentalness
if lex_response['interpretations'][0]['intent']['slots']['Instrumentalness']['value']['resolvedValues']:
    instrumentalness = lex_response['interpretations'][0]['intent']['slots']['Instrumentalness']['value']['resolvedValues'][0]

    if (instrumentalness == 'Pass me the mic!'):
        target_instrumentalness = 0.1 # low instrumental value
    elif (instrumentalness == 'I don\'t mind.'):
        target_instrumentalness = 0.5 # mid-instrumental value
    elif (instrumentalness == 'I just want to zone out.'):
        target_instrumentalness = 0.9 # high instrumental value
    else:
        target_instrumentalness = 0.5 # How to deal with unresolved values?
else:
    target_instrumentalness = 0.5

# Liveness
if lex_response['interpretations'][0]['intent']['slots']['Liveness']['value']['resolvedValues']:
    liveness = lex_response['interpretations'][0]['intent']['slots']['Liveness']['value']['resolvedValues'][0]

    if (liveness == 'Yes!'):
        target_liveness = 0.9 # filter for live music
    elif (liveness == 'No.'):
        target_liveness = 0.1 # filter for not-live music
    elif (liveness == 'It doesn\'t matter!'):
        target_liveness = 0.5 # mid values
    else:
        target_liveness = 0.5 # How to deal with unresolved values?
else:
    target_liveness = 0.5

# Loudness
if lex_response['interpretations'][0]['intent']['slots']['Loudness']['value']['resolvedValues']:
    loudness = lex_response['interpretations'][0]['intent']['slots']['Loudness']['value']['resolvedValues'][0]

    if (loudness == 'Bring it on!'):
        target_loudness = 0 # high loutdness
    elif (loudness == 'Kind of.'):
        target_loudness = -20 # mid loudness
    elif (loudness == 'Not really.'):
        target_loudness = -40 # low loudness (softer music)
    else:
        target_loudness = -20 # How to deal with unresolved values?
else:
    target_loudness = -20

# Valence (including Valence low)
if lex_response['interpretations'][0]['intent']['slots']['Valence']['value']['resolvedValues']:
    valence = lex_response['interpretations'][0]['intent']['slots']['Valence']['value']['resolvedValues'][0]

    if (valence == 'I\'m feeling great! :)'):

        target_valence = 0.9 # a high value

    elif (valence == 'I\'m okay. :('):
        target_valence = 0.5 # mid values

    elif (valence == 'I\'ve been better. :('):

        target_valence = 0.1

        # Look at value for ValenceLow

        if lex_response['interpretations'][0]['intent']['slots']['ValenceLow']['value']['resolvedValues']:
            valence_low = lex_response['interpretations'][0]['intent']['slots']['ValenceLow']['value']['resolvedValues'][0]

            if (valence_low == 'Yes'):
                target_valence = target_valence + 0.5 # a high value
            elif (valence_low == 'No'):
                target_valence = target_valence + 0 # leave target value unchanged
            else:
                target_valence = 0.5 # what do we do if the value is unresolved?
        else:
            target_valence = 0.5

    else:
        target_valence = 0.5 # what do we do if the value is unresolved?
else:
    target_valence = 0.5

# Down here, we make the spotify query
uris = []

# Add additional items to query (acousticness, energy, danceability, instrumentalness, liveness, loudness, valence)
query += f'&target_acousticness={target_acousticness}'
query += f'&target_energy={target_energy}'
query += f'&target_danceability={target_danceability}'
query += f'&target_instrumentalness={target_instrumentalness}'
query += f'&target_liveness={target_liveness}'
query += f'&target_loudness={target_loudness}'
query += f'&target_valence={target_valence}'

print(query)

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {token}"})
json_response = response.json()

print('Recommended Songs:')
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

request_body = json.dumps({
          "name": "My playlist for 3/29/22",
          "description": "Pop and Rock songs for how I'm feeling today",
          "public": False
        })
response = requests.post(url = f"https://api.spotify.com/v1/users/{user_id}/playlists", data = request_body, headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {token}"})

print(response.status_code)

playlist_id = response.json()['id']

request_body = json.dumps({
          "uris" : uris
        })

response = requests.post(url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", data = request_body, headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {token}"})

print(response.status_code)
