from lib.album import *

def test_album_exists_with_title_release_year_artist_id():
    al = Album('Surrealistic Pillow', 1967, 1)
    assert al.title == 'Surrealistic Pillow'
    assert al.release_year == 1967
    assert al.artist_id == 1

