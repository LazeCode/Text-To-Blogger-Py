# Text to Blogger Python Script

This Python script allows you to upload multiple files (txt format) from a folder to blogger.
Automatically uploades a set number of (10,000 default) lines per post from any text document to blogger blog.
Automatically calculates the lines uploaded previously using an SQL database.
Also calculates how many parts are there for each post (if the lines in the text file are larger than set 10,000 amount).

# Requirements:
Python 3.8
pickle
google_auth_oauthlib.flow
googleapiclient.discovery
google.auth.transport.requests
google_auth_httplib2

# Setup
## Installing dependencies and running the script
1. Make sure you have [Python 3.7](https://www.python.org/downloads/) installed on your system
2. If needed, install [pipenv](https://pypi.org/project/pipenv/) via `pip install pipenv`
3. Change to the directory where you installed this script
4. Run `pipenv install` to download and install all the dependencies
5. Run `pipenv shell` to open a shell with all the dependencies available (you'll need to do this every time you want to run the script)
6. Now run the script.

## Setting up the Script
1. Download the script
2. Install all the necessary packages from pip or by downloading them.
3. Create an API with Google for BLogger API.
4. Download the API keys (client.json) and put it in the local folder.
5. Open Config.py and insert the Blog ID from blogger
   This is the blog the script is going to post to.
6. Add the files to be uploaded to the folder "FileToPublish".
7. To run on windows just run the RunPublisher.bat file or on mac run the "Publisher.py"

## Obtaining a Google Photos API key

1. Obtain a Google Photos API key (Client ID and Client Secret) by following the instructions on [Getting started with Google Photos REST APIs](https://developers.google.com/photos/library/guides/get-started)

**NOTE** When selecting your application type in Step 4 of "Request an OAuth 2.0 client ID", please select "Other". There's also no need to carry out step 5 in that section.

2. Download the credentials as client_id.json file and save it on the local folder containing this script.
