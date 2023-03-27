import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import os
import copy

username = "alm.davidso" #go to spotify developers and then go to dahsboard and choose application
client_id = "2d9971b26c3a4aba8668dc3b80159fb6" 
client_secret = "95ac5748cc6b4272b02789bec4f5d1cb"
redirect_uri = "http://localhost:8888/callback"
scope = "playlist-modify-private"
playlist_id = "4PnNhaIDL3kU5QcFeJJSgK"

# Authenticate with Spotify API
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id = "2d9971b26c3a4aba8668dc3b80159fb6", client_secret = "95ac5748cc6b4272b02789bec4f5d1cb", redirect_uri = "http://localhost:8888/callback"))

# Get tracks from playlist
results = sp.playlist_items(playlist_id)
tracks = results["items"]

# Elem0 = tracks[0]
# print(Elem0)

# Get all tracks in the playlist
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])


# Create a set of track IDs to identify duplicates
track_ids = set()
duplicate_tracks = []


# Create list of tracks and concatenate them
for track in tracks:
    track_id = track["track"]["id"]
    track_name = track["track"]["name"]
    artist_info = track["track"]["artists"][0]
    artist_name = artist_info['name']
    track_uri = track['track']["uri"]


    # Check if the track ID is already in the set
    if track_id in track_ids:
        duplicate_tracks.append(track)
    else:
        track_ids.add(track_id)


# print(track_ids)

# Remove duplicate tracks from the playlist
for track in duplicate_tracks:
    sp.playlist_remove_all_occurrences_of_items(playlist_id, [track['track']['uri']])
    