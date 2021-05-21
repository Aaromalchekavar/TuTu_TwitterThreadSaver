import tweepy
from config import twitter_auth
import time


def findMentionAndSendDM(api):
    mentions = api.mentions_timeline()

    for mention in mentions:
        print("Bot is Running")
        user_ = mention.user
        recipent_id = user_.id_str
        inReply_to_status_id = mention.in_reply_to_status_id_str

        match_value = str(inReply_to_status_id)
        if inReply_to_status_id != None:
            status = api.get_status(inReply_to_status_id).text
            with open('./files/inReplyStatusId.txt') as file:
                idFileData = file.readlines()
                boolean = match_value not in idFileData
                file.close()
        else:
            status = "No Text in Tweet. Plese Reply to any valid tweet"
            boolean = False
        if boolean:
            print("Recipent ID : " + recipent_id)
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
                            "text": status + "\n\n >> Tweet Saved! \n\nClick on the link above to go to Root Tweet \nThankyou for using our Service"
                        }
                    }
                }
            }
            api.send_direct_message_new(event)
            with open('./files/inReplyStatusId.txt', 'a') as idFile:
                idFile.writelines("\n"+match_value)
                idFile.close()


def main():
    auth = twitter_auth()
    api = tweepy.API(auth)
    while True:
        findMentionAndSendDM(api)
        time.sleep(60)


if __name__ == "__main__":
    main()
