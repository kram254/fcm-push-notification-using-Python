import requests
import json


serverToken = 'your own server token from firebase account'
deviceToken = 'paste your device token hrere'

headers = {
    'Content-Type' : 'application/json',
    'Authorization' : 'key'+ serverToken
}

body = {'notification' : {
                        'title' : 'The title to your message goes here eg my first FCM',
                        'body' : 'Message body'
                     },

        'to':  deviceToken,

        'priority': 'high',
         
         }

response = requests.post("https://fcm.googleapis.com/fcm/send", headers= headers, data=json.dumps(body))

print(response.status_code)

print(response.json())