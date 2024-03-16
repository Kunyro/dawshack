from dominant_color.dominant_color import sort_images_by_color
from get_spotify import *


def get_albums():
    spotify = Get_spotify()
    albums = spotify.get_random_album(spotify.token, 1, "album")
    covers_sorted = sort_images_by_color(albums)
    return covers_sorted

get_albums()