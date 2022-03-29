import SpotiPyTools as Spoti
import pprint

#https://github.com/Reason0x6/Spotify_PyTools/blob/main/SpotiPyTools.py

# creates an authorised spotipy client
client = Spoti.getClient()

# Takes the playlist share link for example usage
ShareLink = input("Input your playlist ShareLink: ")

# Converts to the Playlist URI
PlaylistURI = Spoti.getPlaylistURI(ShareLink)

# Gets URI's pf Tracks in playlist
Tracks = Spoti.getTracksFromPlaylist(client, ShareLink)

# gets a dict with the info analysed by SpotiPyTools
info = Spoti.definePlaylist(client, ShareLink)
# prints playlist's instrumentalness
print("Playlist Instrumentalness: " + str(info.get("Instrumentalness")))

# get the song previews for the playlist as a dict
songs = Spoti.getSongPreviews(client, ShareLink)

# pretty print the dict
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(songs)
