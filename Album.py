import Track
import Artist
import spotipy


class Album:

    def __init__(self, uri):
        sp = spotipy.Spotify()
        album = sp.album(uri)

        self.name = album['name']
        self.artists = Artist.create_from_list(album['artists'])
        self.uri = uri

    def get_tracks(self):
        sp = spotipy.Spotify()
        self.tracks = Track.create_from_list(sp.album_tracks(self.uri)['items'])

        return self.tracks


def create_from_list(data):
    result_list = []
    for i, t in enumerate(data):
        result_list.append(Album(t['uri']))

    return result_list
