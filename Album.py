import Track
import Artist
import spotipy


class Album:

    def __init__(self, uri):
        sp = spotipy.Spotify()
        album = sp.album(uri)

        self.name = album['name']
        self.tracks = Track.create_from_list(album['tracks']['items'])
