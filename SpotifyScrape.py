<<<<<<< HEAD
import requests
import io
import os
import json
# import time
# import serial
import base64
# from bs4 import BeautifulSoup
# from flask import Flask
import json


AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
URL = 'https://api.spotify.com'
REDIRECT_URI = "http://localhost:8888"
=======
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


## Client authorization information

# Client ID and Secret are given to developers when they register their app with a website.
# Spotify needs a base64 encoded response so here we format the authorization information.
>>>>>>> edc08ffb986e0e46f05a9fdce4918abe96c9a81b

CLIENT_ID = 'ab33af147e5b4cf689dae74fa5e21710'
CLIENT_SECRET = '8fe4c00ac62045e6ac5240b78c62c794'
temp1 = CLIENT_ID + ":"+ CLIENT_SECRET
temp2 = temp1.encode('utf-8','strict')
HEADER_64 = base64.standard_b64encode(temp2)
<<<<<<< HEAD
CLIENT_AUTH = requests.auth.HTTPBasicAuth(CLIENT_ID,CLIENT_SECRET)
HEADERS = {'client_id':CLIENT_ID, 'response_type':'code', 'redirect_uri':REDIRECT_URI}
=======
PARAMS = {'grant_type':'client_credentials'}				# Requested by Spotify for this particular authorization format
AUTH_HEADERS = {'Authorization':b'Basic '+HEADER_64}		# Provides base64 authorization with requests, also particular for this authorization format



## Useful for other types of authorization.

# REDIRECT_URI = "http://localhost:8888"   
# HEADERS = {'client_id':CLIENT_ID, 'response_type':'code', 'redirect_uri':REDIRECT_URI}

>>>>>>> edc08ffb986e0e46f05a9fdce4918abe96c9a81b


print('Begin Program')

<<<<<<< HEAD

PARAMS = {'grant_type':'client_credentials'}
HEADERS = {'Authorization':b'Basic '+HEADER_64}
r = requests.post(TOKEN_URL, data=PARAMS, headers=HEADERS)
# print(r.headers)
dict = json.loads(r.content)
print(dict['access_token'])

HEADERS_AUTH = {'Authorization': 'Bearer ' + dict['access_token']}
r = requests.get('https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V', headers = HEADERS_AUTH)
#print r.text

parsed_json = json.loads(r.text)
artists = parsed_json["artists"]
print(artists[0]["id"])
=======
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




#### Scrapped code testing mostly for authorization types
>>>>>>> edc08ffb986e0e46f05a9fdce4918abe96c9a81b

# r = requests.get(AUTH_URL,params=HEADERS
# print(r.url)
# print(r.headers)
# print(r.status_code)
# print(r.history)




# ## Obtain Permanent Authorization: Learn later
# s = requests.Session()
# r = s.get(AUTH_URL, data=HEADERS)
# print(r.status_code)
# # print(r.text)
# print(r.headers)
# print(r.url)

# ## Token Authorization.
# HEADERS = {'client_id':CLIENT_ID, 'client_secret':CLIENT_SECRET}
# r = requests.post(TOKEN_URL,params=PARAMS, headers = HEADERS)
# print(r.text)

# ### r.headers

# # {'Server': 'nginx'
# #  'Date': 'Sat, 22 Jul 2017 15:40:58 GMT'
# #  'Content-Type': 'application/json'
# #  'Content-Length': '69'
# #  'Connection': 'keep-alive'
# #  'Keep-Alive': 'timeout=600'}


# r = s.get(URL+'/v1/search?type=queen', auth=CLIENT_AUTH)
# print(r.status_code)
# print(r.headers)

# ### r.headers

# # {'Server': 'nginx'
# #  'Date': 'Sat, 22 Jul 2017 15:40:58 GMT'
# #  'Content-Type': 'application/json'
# #  'Transfer-Encoding': 'chunked'
# #  'Connection': 'keep-alive'
# #  'Keep-Alive': 'timeout=600'
# #  'WWW-Authenticate': 'Bearer realm="spotify", error="invalid_request", error_description="Only valid bearer authentication supported"'
# #  'Access-Control-Allow-Origin': '*'
# #  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, DELETE'
# #  'Access-Control-Allow-Credentials': 'true'
# #  'Access-Control-Max-Age': '604800'
# #  'Access-Control-Allow-Headers': 'Accept, Authorization, Origin, Content-Type'
# #  'Content-Encoding': 'gzip'}




# # soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.prettify())