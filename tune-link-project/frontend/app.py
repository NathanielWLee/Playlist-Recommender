import boto3 
import json
import random
import string
import requests
from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
app = Flask(__name__)
#Set up Flask to bypass CORS:
cors = CORS(app)

accessKeyID = '' # secret
secretAccessKey = '' # secret
sessionID = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

def begin_session(accessKeyID, secretAccessKey):
    client = boto3.client(service_name = 'lexv2-runtime', region_name = 'us-east-1', aws_access_key_id = accessKeyID, aws_secret_access_key = secretAccessKey)
    return client
    #lex_client = boto3.client('lex-runtime', aws_access_key_id = config.aws_access_key_id, aws_secret_access_key = config.aws_secret_access_key , region_name= config.region)

# Helper function to submit text to the bot
def text_to_lex(client, message):
    global sessionID
    response = client.recognize_text(
        botId='JG38VXQ0KG',
        botAliasId='TSTALIASID',
        localeId='en_US',
        sessionId=sessionID,
        text = message)
    return response

client = begin_session(accessKeyID, secretAccessKey)

# msg = json.loads(json.dumps(text_to_lex(client, "create playlist")))

@app.route('/')
def home_page():
    example_embed = "This string is from python"
    return render_template('index.html', embed=example_embed)

# python to JS info
@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # print("testfn")
    # GET request
    if request.method == 'GET':
        # print("GET")
        # print("got to get")
        global msg
        # global start
        if(msg['sessionState']['intent']['name'] == 'FallbackIntent'):
            message = {'fallback': msg['messages'][0]['content']}
        else:
            lastSlot = msg['sessionState']['intent']['slots']['Acoustic']
            if lastSlot is None:
                question = msg['messages'][0]['content']
                message = {
                    'question': question,
                    'buttons': msg['messages'][1]['imageResponseCard']['buttons']
                }
            else:
                message = {
                    'ending': [
                        msg['messages'][0]['content'],
                        msg['messages'][1]['content']
                    ]
                }
                finalJSON = json.dumps(msg)
                jsonFile = open("../lex_output.json", "w")
                jsonFile.write(finalJSON)
                jsonFile.close()
            # print("message in get: ", message)
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        # print("POST")
        # print("got to post")
        print(request.get_json())  # parse as JSON
        msgPost = request.get_json()
        # print("msgPost: ", msg)
        return 'Sucesss', 200

    # POST request
    # if request.method == 'POST':
    #     print("got to post 2")
    #     print("request")
    #     print(request.get_json())  # parse as JSON
    #     return 'Sucesss', 200

# JS to python info
@app.route("/receiver", methods=['GET', 'POST'])
def postME():
    # data = request.get_json()
    # data = jsonify(data)
    # return data

    jsdata = request.json
    # print("start post part")
    print(jsdata["messageFromChat"])
    global msg
    msg = json.loads(json.dumps(text_to_lex(client, jsdata["messageFromChat"])))
    # print("msg: ", msg)
    # print("postME")
    # newLexJson = print(msg)
    # testfn(msg)

    # message = "starting message"
    # lastSlot = msg['sessionState']['intent']['slots']['Familiarity']
    # if lastSlot is None:
    #     question = msg['messages'][0]['content']
    #     message = {
    #         'question': question,
    #         'buttons': msg['messages'][1]['imageResponseCard']['buttons']
    #     }
    # else:
    #     message = {
    #         'end-one': msg['messages'][0]['content'],
    #         'end-two': msg['messages'][1]['content']
    #     }
    # print("message: ", message)
    # print("right before")

    # requests.post("http://127.0.0.1:5000/test", data=json.dumps(message))
    # newMessage = requests.get("http://127.0.0.1:5000/test")
    # print("newMessage: ", newMessage)
    # print("right after")
    return jsdata #data

# @app.route('/receiver', methods = ['POST'])
# def get_post_javascript_data():
#     jsdata = request.form['javascript_data']
#     print("ending")
#     return json.loads(jsdata)[0]


# print("initial message")
# print(msg['messages'][0]['content'])

# Kick off this bitch
# msg = json.loads(json.dumps(text_to_lex(client, "create playlist")))

# lastSlot = msg['sessionState']['intent']['slots']['Familiarity']
# while lastSlot is None:
#     question = msg['messages'][0]['content']
#     buttons = msg['messages'][1]['imageResponseCard']['buttons']
#     print(question)
#     for button in buttons:
#         print(button['text'])
#     userInput = input()
#     msg = json.loads(json.dumps(text_to_lex(client, userInput)))
#     lastSlot = msg['sessionState']['intent']['slots']['Familiarity']

# print(msg['messages'][0]['content'])
# print(msg['messages'][1]['content'])

if __name__ == "__main__":
    app.run(debug=True)