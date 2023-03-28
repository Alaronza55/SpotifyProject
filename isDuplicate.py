import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import os
import copy
import re

username = "alm.davidso" #go to spotify developers and then go to dahsboard and choose application
client_id = "2d9971b26c3a4aba8668dc3b80159fb6" 
client_secret = "95ac5748cc6b4272b02789bec4f5d1cb"
redirect_uri = "http://localhost:8888/callback"
scope = "playlist-modify-private"
playlist_id = "746dSpQ348vkqT9pd6ZXyb"



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
duplicate_ids = []

track_names = set()
duplicate_names = []
duplicate_names_doublons = []
to_add = []

track_artists = set()
duplicate_artists = []

track_uris = set()
duplicate_uri = []


# Create list of tracks and concatenate them
for track in tracks:
    track_id = track["track"]["id"]
    track_name = track["track"]["name"]
    artist_info = track["track"]["artists"][0]
    artist_name = artist_info['name']
    track_uri = track['track']["uri"]

    # track_name_without_spaces = [re.sub(r"\s+", "", track_name)]
    # print(track_name_without_spaces)

    # Check if the track ID is already in the set
    if track_id in track_ids:
        duplicate_ids.append(track)
    else:
        track_ids.add(track_id)

    if track_name in track_names:
        duplicate_names.append(track)
    else:
        track_names.add(track_name)

    if track_uri in track_uris:
        duplicate_uri.append(track)
    else:
        track_uris.add(track_name)
    
    if artist_name in track_artists:
        duplicate_artists.append(track)
    else:
        track_artists.add(track_name)



def remove_duplicates_id() :
    # Remove duplicate tracks from the playlist
    for track in duplicate_ids:
        sp.playlist_remove_all_occurrences_of_items(playlist_id, [track['track']['uri']])

    # for track in duplicate_ids:
    #     sp.playlist_add_items(playlist_id, [track['track']['uri']])
        
remove_duplicates_id()

# Creating another list with only duplicate names
def Duplicates_of_duplicates():
    for track in duplicate_ids:
        if duplicate_ids.count(track) > 1:
            duplicate_names_doublons.append(track)
        else :
            to_add.append(track)

Duplicates_of_duplicates()

for track in duplicate_names_doublons:
    print(track["track"]["name"])




# def remove_duplicates_name() :
#     # Remove duplicate tracks from the playlist
#     for track in duplicate_names:
#         sp.playlist_remove_all_occurrences_of_items(playlist_id, [track['track']['uri']])

#     for track in to_add:
#         sp.playlist_add_items(playlist_id, [track['track']['uri']])
        
# remove_duplicates_name()

# def remove_duplicates_uri() :
#     # Remove duplicate tracks from the playlist
#     for track in duplicate_uri:
#         sp.playlist_remove_all_occurrences_of_items(playlist_id, [track['track']['uri']])

#     # for track in duplicate_uri:
#     #     sp.playlist_add_items(playlist_id, [track['track']['uri']])

# # remove_duplicates_uri()

# def remove_duplicates_artists() :
#     # Remove duplicate tracks from the playlist
#     for track in duplicate_artists	:
#         sp.playlist_remove_all_occurrences_of_items(playlist_id, [track['track']['uri']])

#     # for track in duplicate_artists:
#     #     sp.playlist_add_items(playlist_id, [track['track']['uri']])

# # remove_duplicates_artists()




