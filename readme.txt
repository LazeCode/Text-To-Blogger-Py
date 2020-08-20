This Python script allows you to upload files from a folder to blogger.

Requirements:
Python 3.8

Packages to install on python:
pickle
google_auth_oauthlib.flow
googleapiclient.discovery
google.auth.transport.requests
google_auth_httplib2

How to use:

1. Download the script
2. Install all the necessary packages from pip or by downloading them.
3. Create an API with Google for BLogger API.
4. Download the API keys and put it in the local folder.
5. Open Config.py and insert the Blog ID from blogger
   This is the blog the script is going to post to.
6. Add the files to be uploaded to the folder "FileToPublish".
7. To run on windows just run the RunPublisher.bat file or on mac run the "Publisher.py"