from TwitterAPI import TwitterAPI
import json
import devcredentials

api = TwitterAPI(devcredentials.API_Key, 
                 devcredentials.API_Secret_Key,
                 devcredentials.Acess_Token,
                 devcredentials.Acess_Token_Secret)



def sendDM(user_id,message_text):
    event = {
        "event": {
            "type": "message_create",
            "message_create": {
                "target": {
                    "recipient_id": user_id
                },
                "message_data": {
                    "text": message_text
                }
            }
        }
    }

    r = api.request('direct_messages/events/new', json.dumps(event))
    print('SUCCESS' if r.status_code == 200 else 'PROBLEM: ' + r.text)

