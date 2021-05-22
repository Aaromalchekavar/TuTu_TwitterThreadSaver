import tweepy
from config import twitter_auth
import time
from send_message import sendDM


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
            with open('./files/inReplyStatusId.txt','r') as file:
                file.seek(0)
                idFileData = file.read().strip()
                boolean = match_value not in idFileData

        else:
            status = "No Text in Tweet. Plese Reply to any valid tweet"
            boolean = False
        if boolean:
            print("Recipent ID : " + recipent_id)
            print(match_value + " not found thus sending tweets to dm")
            print(status)
            message_text ="🤖 TuTu Thread Saver v1 🤖 "+"\n\nTweet: "+ "\n"+status + "\n\n 🤖 Thread Saved! \n\nClick the given link  >> "+" https://twitter.com/"+status.user.screen_name+"/status/"+status.id_str +" << to go to Root Thread \n\nThankyou for using our Service 🤘"
            sendDM(recipent_id,message_text)
            with open('./files/inReplyStatusId.txt','a') as idFile:
                idFile.write("\n"+match_value)


def main():
    auth = twitter_auth()
    api = tweepy.API(auth)
    while True:
        findMentionAndSendDM(api)
        time.sleep(60)


if __name__ == "__main__":
    main()
