import json
from collections import Counter

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

pitchClassNotation = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

# Spotify Dev Details
cid     = << Get from Spotify Dev >>
secret  = << Get from Spotify Dev >>


def getClient():
    #Authentication - without user
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    return sp

def getTracksFromPlaylist(sp, shareLink):
        playlist_link = shareLink
        playlist_URI = playlist_link.split("/")[-1].split("?")[0]
        track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

        return track_uris

def getPlaylistURI(shareLink):
        playlist_link = shareLink
        playlist_URI = playlist_link.split("/")[-1].split("?")[0]

        return playlist_URI


def definePlaylist(sp, playlistURI):
    size = len(sp.playlist_tracks(playlistURI)["items"])
    genres = []
    keys = []
    val = 0
    instru = 0
    for track in sp.playlist_tracks(playlistURI)["items"]:

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
        
        key = pitchClassNotation[parsed_info['key']]
        if parsed_info['mode'] == 0:
            key = key + " Minor"
        else:
            key = key + " Major"
        keys.append(key)

        #val calc
        val = val + parsed_info['valence']
        instru = instru + parsed_info['instrumentalness']
        genres.extend(artist_genres)
        
    genreOut = ""
    for x in Counter(genres).most_common(5):
        genreOut = genreOut + str(x[0]) + ", "
    genreOut = genreOut[:-2]

    keysOut = ""
    for x in Counter(keys).most_common(5):
        keysOut = keysOut + str(x[0]) + ", "
    keysOut = keysOut[:-2]


    return {"Valence" : str(parsed_info['valence']), "Instrumentalness" : str(parsed_info['instrumentalness']), "Top Genres" : genreOut, "Top Keys" : keysOut }
