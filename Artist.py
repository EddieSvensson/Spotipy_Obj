import Track
import Album
import spotipy


class Artist:
    def __init__(self, data):
        sp = spotipy.Spotify()