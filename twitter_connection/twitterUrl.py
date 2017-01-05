import tweepy
from twitter_connection import hidden


def getapi():
    secrets = hidden.oauth()
    auth = tweepy.OAuthHandler(secrets['customerKey'], secrets['customerSecret'])
    auth.set_access_token(secrets['accessToken'], secrets['accessTokenSecret'])
    api = tweepy.API(auth)
    return api

"""def augment(url, parameters):

    consumer = oauth.Consumer(key=secrets['customerKey'], secret=secrets['customerSecret'])
    token = oauth.Token(key=secrets['acessToken'], secret=secrets['acessTokenSecret'])
    oauth_request = oauth.Request.from_consumer_and_token(consumer=consumer, token=token,http_method='GET', http_url=url, parameters=parameters)
    if oauth_request:
        oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(),consumer,token)
        return oauth_request.to_url()
    else:
        return None
"""