import Album
import Track
import Artist
import spotipy

sp = spotipy.Spotify()

album = Album.Album('spotify:album:4In2V4QylBdWT8HJ0dLDw5')

print(Artist.Artist('spotify:artist:0MG4LXIw7n4x0wjDc6WYXk').get_albums())
