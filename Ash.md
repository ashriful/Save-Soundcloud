WHAT WE NEED: requests, numpy, oauth(possibly), pick(possibly)

OAuth 2 is what Spotify uses to authenticate interactions. There's still a lot of information needed about authentication. But as far as I know, it seems best to go with implicit grant flow. Meaning, we have the user sign into their Spotify account and request for permission using "Scopes" to get tokens and access to private playlist and such. 
https://developer.spotify.com/web-api/authorization-guide/#implicit_grant_flow

## 1. Grab User's Info
Variable = input()
Ask for user name and password and implement Scopes 

## 2. Grab Playlists
point api to /v1/users/{user_id}/playlists using requests (http://www.pythonforbeginners.com/scripts/using-the-youtube-api/)

https://developer.spotify.com/web-api/get-list-users-playlists/

## 3. Present list of Playlist to User 
Present list of playlists to user, let user pick a playlists, input playlist as a request.
Possibly use pick to do this? (https://github.com/wong2/pick)

## 4. Grab Playlist
Using requests we need to grab the specific playlist and create and array of track name and id.
https://developer.spotify.com/web-api/get-playlist/

## 5. Grab Track Information
Using the id's, we can use this function to grab audio features of the array of tracks.
https://developer.spotify.com/web-api/get-several-audio-features/
Make a data array of tempo, name, and id from results. 

## 5. Using Numpy for Bell Curve
Use numpy to rearrange tempo into bell curve (https://stackoverflow.com/questions/43506980/python-fit-a-distribution-to-a-bell-curve/43507391)

## 6. Create Playlist with Requests
Ask user for the name of the playlist.
https://developer.spotify.com/web-api/create-playlist/ 
Create a playlist with the given user input 

## 7. Add Tracks to Playlist with Requests
Using the new data array, ad tracks based on track id. 
https://developer.spotify.com/web-api/add-tracks-to-playlist/

                    
