import json
from collections import Counter

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

pitchClassNotation = ["C","C#/Db", "D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B"]

# Spotify Dev Details
cid     = 'e3f8b4b5934845b6b8384d57f64ed7cf'
secret  = '218f56726b6143b6be0d567ae542fc75'

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = input("Spotify Playlist 'Share' Link: ")
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
size = len(sp.playlist_tracks(playlist_URI)["items"])
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
    
    print(key)
    print("Valence (0-1) -> Sad-Happy:\t| " + str(parsed_info['valence']))
    print("Instrumentalness (0-1):\t\t| " + str(parsed_info['instrumentalness']))
    print("Track Name:\t\t\t| " + track_name)
    print("Artist:\t\t\t\t| " + artist_name)
    print("Album:\t\t\t\t| " + album)
    print("Artist Genres:\t\t\t| " + str(artist_genres))
    print("--------------------------------------------")

print("Playlist Size:\t\t" + str(size) + " songs")
print("Playlist Happiness:\t%.3f" % ((val/size)*100), end="%\n")
print("Instrumentalness:\t%.3f" % ((instru/size)*100), end="%\n")
genreOut = "\t\t"
for x in Counter(genres).most_common(5):
    genreOut = genreOut + str(x[0]) + ",\n\t\t\t"
genreOut = genreOut[:-5]
print("Genre Mix:" + genreOut)
