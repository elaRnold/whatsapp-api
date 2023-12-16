from flask import Flask, request
import util
import whatsappservice

app = Flask(__name__)
@app.route('/welcome', methods=['GET'])
def index():
    return "welcome dev"

@app.route('/whatsapp', methods=['GET'])
def VerifyToken():
    try:
        accessToken = "19HNDHJAHJ3B3KHBJD8F73NBDJH2"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
        return "", 400

@app.route('/whatsapp', methods=['POST'])
def ReceivedMessage():
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]
        text = util.getTextUser(message)
        generateMessage(text, number)
        return "EVENT_RECEIVED"

    except:
        return "EVENT_RECEIVED"

def generateMessage(text, number):
    if text == "Social networks":
        data = util.TextMessage(number)
    elif text == "CV":
        data = util.DocumentMessage(number)
    else:
        data = util.ButtonsMessage(number)

    whatsappservice.sendMessageWhatsapp(data)
    
if(__name__ == "__main__"):
    app.run()