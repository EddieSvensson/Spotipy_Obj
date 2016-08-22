import Artist
import Album
import spotipy
import urllib.request
import winsound


class Track:

    def __init__(self, uri):
        sp = spotipy.Spotify()
        track = sp.track(uri)

        self.name = track['name']
        self.length = track['duration_ms']
        self.url = track['preview_url']
        self.preview = open(self.name + '.mp3')

    def download_track(self):
        response = urllib.request.urlopen(self.url)
        data = response.read()
        file = self.preview
        file.read(data)
        return data

    def play(self):
        self.download_track()
        winsound.PlaySound(self.preview, winsound.SND_FILENAME)


def create_from_list(data):
    result_list = []
    for i, t in enumerate(data):
        result_list.append(Track(t['uri']))

    return result_list
