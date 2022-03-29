import SpotiPyTools as Spoti


# creates an authorised spotipy client
client = Spoti.getClient()

# Takes the playlist share link for example usage
ShareLink = input("Input your playlist ShareLink: ")

# Converts to the Playlist URI
PlaylistURI = Spoti.getPlaylistURI(ShareLink)

# Gets URI's pf Tracks in playlist
Tracks = Spoti.getTracksFromPlaylist(client, ShareLink)

# Outputs a dict with the info analysed by SpotiPyTools
print(Spoti.definePlaylist(client, ShareLink))
