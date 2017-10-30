# Author: Jeffrey Estrada
import argparse
import time
from facepy import GraphAPI

parser = argparse.ArgumentParser(description='This is for posting on a facebook group')
parser.add_argument('api_key',help='Enter your facebook api key')
parser.add_argument('group_id', help='Enter your facebook group id')
parser.add_argument('msg', help='Enter your facebook post')

args = parser.parse_args()

graph = GraphAPI(args.api_key)

print("Posting to " + "http://www.facebook.com/groups/" + str(args.group_id))

graph.post(path =str(args.group_id) + '/feed', message=args.msg)
time.sleep(10)
print("Done posting to facebook")
