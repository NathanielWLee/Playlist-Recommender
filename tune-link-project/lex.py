import boto3 
import json

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
