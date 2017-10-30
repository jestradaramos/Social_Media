# Author: Jeffrey Estrada

from twython import Twython
import webbrowser
import argparse

parser = argparse.ArgumentParser(description='This script is meant to post tweets')
parser.add_argument('app_key', help='This is the twitter app key, which can be found when creating an app on the twitter site')
parser.add_argument('app_sec', help='This is the the secret key that comes with the app you create on their site')
args = parser.parse_args()


APP_KEY = args.app_key
APP_SECRET = args.app_sec


twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens() 
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

webbrowser.open_new(auth['auth_url'])

oauth_verifier = input("Give me code: ")


twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
final_step = twitter.get_authorized_tokens(oauth_verifier)


OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

with open('mykeys', 'a') as keys:
	keys.write("Auth Token:%s\n" % OAUTH_TOKEN)
	keys.write("Auth Secret:%s\n" % OAUTH_TOKEN_SECRET)




