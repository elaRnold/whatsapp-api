import requests
import json

def sendMessageWhatsapp(data):
    try:
        token = "EAAC3ZBTmC13wBO7diVSfacdOYhN1ncxLNDb7msZBdAJCad8bAn4ZApj6C8ZCcl18zr7r6m1wdk1rg5JLaXhOTU9PDfkjGl6nhskwcdoZBZAFoZCPYyy5ov2jV1N9aSCWMJJmvbsM3utvGUW6172zesJerQZCETnS0LPL7ta7WtmaDFTZBvqWVzWQOF8qXieq8t6CI"
        api_url = "https://graph.facebook.com/v17.0/189485997580116/messages"
        headers = {"Content-type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)

        if response.status_code == 200:
            return True
        
        return False

    except Exception as exc:
        print(exc)
        return False