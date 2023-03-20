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


# Create list of tracks and concatenate them
for track in tracks:
    track_id = track["track"]["id"]
    track_name = track["track"]["name"]
    artist_info = track["track"]["artists"][0]
    artist_name = artist_info['name']
    # track_uri = track['track']["uri"]

    # print (track_name)
    # print (track_id)
    # print (artist_name)
    # print (track_uri)
    
    merged = '_'.join([track_id]+[track_name]+[artist_name])

    # print(merged) 

    # new_list = merged.split('_')
    
    # print(new_list)

    # id = new_list[0]
    # Name = new_list[1]

    # print(id)
    # print(Name)

    # duplicates = []
    
    # for item in track_uri:
    #     if track_uri.count(item) > 1 and item not in duplicates:
    #         duplicates.append(item)
    
    # print(duplicates)

    # sp.playlist_remove_all_occurrences_of_items



