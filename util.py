def getTextUser(message):
    text = ""
    typeMesagge = message["type"]

    if typeMesagge == "text":
        text = (message["text"])["body"]

    elif typeMesagge == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]

        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]

        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]

        else:
            print("sin mensaje")

    else:
        print("sin mensaje")
    
    return text

def TextMessage(text, number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": text
                }
            }
    return data

def ButtonsMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": "¿confirmas tu registro?😜"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "001",
                                    "title": "Si"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "002",
                                    "title": "No"
                                }
                            }
                        ]
                    }
                }
            }
    return data