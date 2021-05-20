import tweepy
from config import twitter_auth

idFile = open('./files/inReplyStatusId.txt', 'a')
file = open('./files/inReplyStatusId.txt')
idFileData = file.readlines()

auth = twitter_auth()
api = tweepy.API(auth)

user = api.get_user("ChekavarAaromal")
mentions = api.mentions_timeline()


for mention in mentions:
    user_ = mention.user
    recipent_id = user_.id_str
    print("Recipent ID : " + recipent_id)
    inReply_to_status_id = mention.in_reply_to_status_id_str
    print(inReply_to_status_id)
    match_value = str(inReply_to_status_id)
    if inReply_to_status_id != None:
        status = api.get_status(inReply_to_status_id).text
        boolean = match_value not in idFileData
    else:
        status = "No Text in Tweet. Plese Reply to any valid tweet"
        boolean = False
    if boolean:
        print(match_value + " not found thus sending tweets to dm")
        print(status)
        event = {
        "event": {
            "type": "message_create",
            "message_create": {
            "target": {
                "recipient_id": recipent_id
            },
            "message_data": {
                "text": status
            }
            }
        }
        }
        api.send_direct_message_new(event)
        idFile.writelines("\n"+match_value)





