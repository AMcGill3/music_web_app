from lib.album_repository import *
from lib.album import *

def test_album_repository_get_takes_connection_argument(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    assert repository.connection == db_connection

def test_album_repository_returns_all(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)

    albums = [Album('Doolittle', 1989, 1),
              Album('Surfer Rosa', 1988, 1),
              Album('Waterloo', 1974, 2),
              Album('Super Trouper', 1980, 2),
              Album('Lover', 2019, 3),
              Album('Folklore', 2020, 3),
              Album('I Put a Spell on You', 1965, 4),
              Album('Baltimore', 1978, 4)]
    
    assert repository.all() == albums

def test_album_repository_creates_new_album(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    repository.create(Album('Revolver', 1966, 5))

    albums = [Album('Doolittle', 1989, 1),
              Album('Surfer Rosa', 1988, 1),
              Album('Waterloo', 1974, 2),
              Album('Super Trouper', 1980, 2),
              Album('Lover', 2019, 3),
              Album('Folklore', 2020, 3),
              Album('I Put a Spell on You', 1965, 4),
              Album('Baltimore', 1978, 4),
              Album('Revolver', 1966, 5)]

    assert repository.all() == albums

def test_album_repository_finds_all_albums_by_one_artist(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find_by_artist(2) == [
              Album('Waterloo', 1974, 2),
              Album('Super Trouper', 1980, 2)]
    
def test_album_repository_finds_album_by_title(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find_by_title('Waterloo') == Album('Waterloo', 1974, 2)

def test_album_repository_finds_album_by_release_year(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find_by_release_year(1980) == [
                Album('Super Trouper', 1980, 2)
    ]

def test_album_repository_delete(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    repository.delete('Folklore')
    albums = [Album('Doolittle', 1989, 1),
              Album('Surfer Rosa', 1988, 1),
              Album('Waterloo', 1974, 2),
              Album('Super Trouper', 1980, 2),
              Album('Lover', 2019, 3),
              Album('I Put a Spell on You', 1965, 4),
              Album('Baltimore', 1978, 4)]
    
    assert repository.all() == albums