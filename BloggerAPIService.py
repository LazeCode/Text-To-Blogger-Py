
import pickle
import os
from pprint import pprint as pp
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import google_auth_httplib2

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'blogger'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/blogger']

cred = None

if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        cred = pickle.load(token)

if not cred or not cred.valid:
    if cred and cred.expired and cred.refresh_token:
        cred.refresh(Request())

    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPE)
        cred = flow.run_local_server()

    with open('token.pickle', 'wb') as token:
        pickle.dump(cred, token)

try:
    Blog = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
    print('Service created successfully')
    # print(service)
except Exception as e:
    print(e)

# resp = service.blogs().get(blogId=BlogId).execute()
# print(resp)