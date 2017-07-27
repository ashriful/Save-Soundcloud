WHAT WE NEED: requests, numpy, oauth(possibly)

OAuth 2 is what Spotify uses to authenticate interactions. I don't know much about 
https://developer.spotify.com/web-api/authorization-guide/#implicit_grant_flow




function to get input of person's user name and password 
use that to authenticate token with scopes 
point api to 		/v1/users/{user_id}/playlists
Present list of playlists to user 
Let user pick a playlists 
Input playlist as a request 
	/v1/users/{user_id}/playlists/{playlist_id}/tracks
	curl -X GET "https://api.spotify.com/v1/audio-features/?ids=4JpKVNYnVcJ8tuMKjAj50A,2NRANZE9UCmPAS5XVbXL40,24JygzOLM0EmRQeGtFcIcG" -H "Authorization: Bearer {your access token}"
	
Grab tempo 
make a data array of tempo name and id 
use numpy to rearrange tempo into bell curve 
make that into a data array

Create a playlist  with 
curl -X POST "https://api.spotify.com/v1/users/thelinmichael/playlists" -H "Authorization: Bearer {your access token}" -H "Content-Type: application/json" --data "{\"name\":\"A New Playlist\", \"public\":false}"
make another array into data frame and add to 
curl -i -X POST "https://api.spotify.com/v1/users/wizzler/playlists/7oi0w0SLbJ4YyjrOxhZbUv/tracks?uris=spotify%3Atrack%3A4iV5W9uYEdYUVa79Axb7Rh,spotify%3Atrack%3A1301WleyT98MSxVHPZCA6M" -H "Authorization: Bearer {your access token}" -H "Accept: application/json"                       
                    
