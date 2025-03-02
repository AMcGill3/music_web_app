from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def create(self, album):
        rows = self.connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id', [
                                                            album.title, album.release_year, album.artist_id])
        row = rows[0]
        album.id = row['id']
        return album
    
    def delete(self, title):
        self.connection.execute('DELETE FROM albums WHERE title = %s', [title])
        return None
    
    def find_by_artist(self, artist_id):
        rows = self.connection.execute(
            'SELECT * from albums WHERE artist_id = %s', [artist_id])
        albums = []
        for row in rows:
            item = Album(row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def find_by_title(self, title):
        rows = self.connection.execute(
            'SELECT * from albums WHERE title = %s', [title])
        row = rows[0]
        album = Album(row["title"], row["release_year"], row["artist_id"])
        return album
    
    def find_by_release_year(self, release_year):
        rows = self.connection.execute(
            'SELECT * from albums WHERE release_year = %s', [release_year])
        albums = []
        for row in rows:
            album = Album(row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums
    
    def find_by_id(self, id):
        rows = self.connection.execute(
            'SELECT * from albums WHERE id = %s', [id])
        row = rows[0]
        album = Album(row["title"], row["release_year"], row["artist_id"])
        return album