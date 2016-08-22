import Album
import Track
import Artist
import spotipy
import pprint

sp = spotipy.Spotify()

album = Album.Album('spotify:album:4In2V4QylBdWT8HJ0dLDw5')

album.tracks[0].play()