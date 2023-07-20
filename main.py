import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace with your own Spotify API credentials
client_id = ''
client_secret = ''
redirect_uri = 'http://localhost:8888/'
# Replace with the ID of the Spotify playlist you want to add tracks to
playlist_id = ''
tracks_uri = []

f = open('uri_tracks.txt','r')
for i in f:
    i.strip()
    tracks_uri.append(f'spotify:track:{i.strip()}')


scope = 'playlist-modify-public'  
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                                redirect_uri=redirect_uri, scope=scope))

# Add the specified tracks to the playlist with the given playlist ID
sp.playlist_add_items(playlist_id=playlist_id, items=tracks_uri)

