# Author: Jeffrey Estrada

import time
from facepy import GraphAPI

api_key = 'EAACEdEose0cBAPvakqu8ZCqHZBo6VGGuK6k0OjLdYmm4pmfXXJX5acchbvSYltgKJKYssOi69jvMpHzPMzZB0ZAsZBRWfkmB4l15uxF49VZBXZBdBpZAISIpOuPNsRbhwZB8Arm8fbBZB2bTb3k0fdPmXhOjl8QWX9olrwrnZAuWYRZBzdmJXJl800ZBd2kkRqGufGbOaxJHepYIvKQZDZD' # Jeff's API number
graph = GraphAPI(api_key)

message = input("Type out your message") # Might make a form that takes in data.

group_id = 735408263327568 #Used www.lookup-id.com to find this number

print("Posting to " + "http://www.facebook.com/groups/" + str(group_id))

graph.post(path =str(group_id) + '/feed', message=message)
time.sleep(10)
print("Done")
