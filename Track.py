import Artist
import spotipy
import webbrowser



class Track:

    def __init__(self, uri):
        sp = spotipy.Spotify()
        track = sp.track(uri)

        self.name = track['name']
        self.length = track['duration_ms']
        self.url = track['preview_url']
        self.albumURI = track['album']['uri']
        self.artists = Artist.create_from_list(track['artists'])

    def play(self):
        webbrowser.open_new_tab(self.url)


def create_from_list(data):
    result_list = []
    for i, t in enumerate(data):
        result_list.append(Track(t['uri']))

    return result_list
