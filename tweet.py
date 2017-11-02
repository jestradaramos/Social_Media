# Author: Jeffrey Estrada

from twython import Twython
import argparse

parser = argparse.ArgumentParser(description='This is where actual tweets are sent')
parser.add_argument('app_key' , help='This is where the app key goes')
parser.add_argument('app_sec' , help='This is the secret key that comes with the app that you get')
parser.add_argument('auth_token', help='This will be retrieved using the auth_tweet.py')
parser.add_argument('auth_sec' , help='This will also be retrieved from auth_tweet.py')
parser.add_argument('tweet', help='The actual tweet')
args = parser.parse_args()
print("Sending tweet...")
twitter = Twython(args.app_key, args.app_sec, 
				args.auth_token, args.auth_sec)

with open(args.tweet, 'r') as status:
	tweet = status.read()

twitter.update_status(status=tweet)

print("Tweet Sent!")
