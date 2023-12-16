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

def TextMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": "~ arnaldobenavides.ab@gmail.com\n~ arnaldobenavides@uninorte.edu.co\n~ https://github.com/elaRnold/elaRnold\n~ https://www.linkedin.com/in/arnaldobr/"
                }
            }
    return data

def DocumentMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": "A continuación, te dejo el link público del CV de mi creador:\nBelow, I leave you the public link of my creator's CV:\nhttps://uninorte-my.sharepoint.com/:b:/g/personal/arnaldobenavides_uninorte_edu_co/Ed-xKJHgCyBPjsqFMsKIn4UBY-q5Gv-y3NjyHqBXnOvaEQ?e=DaduJS"
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
                        "text": "¡Hola 👋!, Gracias por contactarte con el Ing. Arnaldo Benavides. Soy su asistente bot👾 y es un placer atenderte 😊. En breve serás contactado, mientras, te dejo algunas opciones que podrían serte de utilidad 😎.\n\nHello 👋!, Thank you for contacting Engineer Arnaldo Benavides. I am his bot's assistant👾 and it is a pleasure to serve you 😊. You will be contacted shortly, meanwhile, I leave you some options that could be useful to you 😎."
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "001",
                                    "title": "Social networks"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "002",
                                    "title": "CV"
                                }
                            }
                        ]
                    }
                }
            }
    return data