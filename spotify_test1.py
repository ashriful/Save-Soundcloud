# Save-Soundcloud v1.0
# SpotifyScrape.py


# Contributors
# Ash
# Julian Marks
# Richa Wadaskar



## Some libraries that might be useful later

# import io
# import os
# import time
# import serial
# from bs4 import BeautifulSoup
# from flask import Flask

import requests
import json
import base64



## URL Navigation

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
URL = 'https://api.spotify.com'

SCOPES = "playlist-read-private" 
## Client authorization information

# Client ID and Secret are given to developers when they register their app with a website.
# Spotify needs a base64 encoded response so here we format the authorization information.


CLIENT_ID = "24c3f8d05a4b499886011a488ac313e5"
CLIENT_SECRET = "146c0bdbe3e7408b868ca32e0419ddc8"
temp1 = CLIENT_ID + ":"+ CLIENT_SECRET 
temp2 = temp1.encode('utf-8','strict')
HEADER_64 = base64.standard_b64encode(temp2)
PARAMS = {'grant_type':'client_credentials'}				# Requested by Spotify for this particular authorization format
AUTH_HEADERS = {'Authorization':b'Basic '+HEADER_64}		# Provides base64 authorization with requests, also particular for this authorization format



## Useful for other types of authorization.

#REDIRECT_URI = "http://localhost:8888"   
#HEADERS = {'client_id':CLIENT_ID, 'response_type':'code', 'redirect_uri':REDIRECT_URI}



print('Begin Program')

# Workflow for obtaining a token. Could be written into a function.

r = requests.post(TOKEN_URL, data=PARAMS, headers=AUTH_HEADERS)
dict = json.loads(r.content)
print(dict['access_token'])
TOKEN=dict['access_token']


# Using token to make API calls

TOKEN_HEADERS = {'Authorization':'Bearer ' +dict['access_token']}
r=requests.get('https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V', headers=TOKEN_HEADERS)	# API URL call to endpoint, authorization provided in headers
print(r.text)																						# Can split urls into (URL+NODE) for NODE=/v1/artist.../
TRACK = json.loads(r.content)			
print('\n \n')
print(TRACK['album']['id'])



print('\n End Program')
