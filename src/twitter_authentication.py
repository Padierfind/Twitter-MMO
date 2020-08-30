print("In File: src/twitter_authentication.py")

from tweepy import OAuthHandler
from configs.twitter_api import api_key, api_secret, access_token, access_token_secret


def get_auth():
    print('In Method: get_auth()')

    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth
