import tweepy
import logging
import devcredentials


logger = logging.getLogger()


def create_api():

    auth = tweepy.OAuthHandler(
        devcredentials.API_Key, devcredentials.API_Secret_Key)
    auth.set_access_token(devcredentials.Acess_Token,
                          devcredentials.Acess_Token_Secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api


def twitter_auth():
    auth = tweepy.OAuthHandler(
        devcredentials.API_Key, devcredentials.API_Secret_Key)
    auth.set_access_token(devcredentials.Acess_Token,
                          devcredentials.Acess_Token_Secret)
    return auth