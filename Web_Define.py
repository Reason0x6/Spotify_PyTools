import json
from collections import Counter

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

pitchClassNotation = [
                "C", "C#/Db", "D", "D#/Eb",
                "E", "F", "F#/Gb", "G",
                "G#/Ab", "A", "A#/Bb", "B"
                     ]

# Spotify Dev Details
cid     = << Get from Spotify Dev >>
secret  = << Get from Spotify Dev >>

#Authentication - without user
client_credentials_manager 
  = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp 
  = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link 
  = input("Spotify Playlist 'Share' Link: ")
playlist_URI 
  = playlist_link.split("/")[-1].split("?")[0]
track_uris 
  = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
size 
  = len(sp.playlist_tracks(playlist_URI)["items"])
print("Playlist Details: ")
print("--------------------------------------------")

val = 0
instru = 0
genres = []

for track in sp.playlist_tracks(playlist_URI)["items"]:

    #URI
    track_uri = track["track"]["uri"]
    #Track name
    track_name = track["track"]["name"]
    
    #Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    
    #Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]
    
    #Album
    album = track["track"]["album"]["name"]
    
    #Popularity of the track
    track_pop = track["track"]["popularity"]
    parse = str(sp.audio_features(track_uri))
    parse = parse.replace("'","\"").replace("[","").replace("]","")
    parsed_info = json.loads(parse)
    key = "Key:\t\t\t\t| " + pitchClassNotation[parsed_info['key']]
    if parsed_info['mode'] == 0:
         key = key + " Minor"
    else:
          key = key + " Major"
    
    #val calc
    val = val + parsed_info['valence']
    instru = instru + parsed_info['instrumentalness']
    genres.extend(artist_genres)
    
    << Printing Truncated >>
<< Printing Truncated >>
