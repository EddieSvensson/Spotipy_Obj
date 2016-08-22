import Track
import Album
import spotipy


class Artist:
    def __init__(self, uri):
        sp = spotipy.Spotify()
        artist = sp.artist(uri)

        self.name = artist['name']
        self.uri = uri


    def get_pop_tracks(self):
        sp = spotipy.Spotify()
        self.pop_tracks = Track.create_from_list(sp.artist_top_tracks(self.uri)['tracks'])

        return self.pop_tracks

    def get_albums(self):
        sp = spotipy.Spotify()
        self.albums = Album.create_from_list(sp.artist_albums(artist_id=self.uri, limit=50)['items'])

        return self.albums


def create_from_list(data):
    result_list = []
    for i, t in enumerate(data):
        result_list.append(Artist(t['uri']))

    return result_list
