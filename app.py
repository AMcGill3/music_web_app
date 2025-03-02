import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from flask import Flask, request, Response, redirect

# Create a new Flask app
app = Flask(__name__)
    
# == Your Routes Here ==
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    albums = repo.all()
    return render_template('albums/all_albums.html', albums=albums)

@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    al_repo = AlbumRepository(connection)
    album = al_repo.find_by_id(id)
    return render_template('albums/one_album.html', album=album)


@app.route('/albums/new', methods=['GET'])
def get_album_form():
    return render_template('albums/new_album.html')

@app.route('/albums', methods=['POST'])
def create_album():
    title = request.form['title']
    release_year = request.form['release_year']
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    album = Album(title, release_year, None)
    new_album = repo.create(album)

    return redirect(f'/albums/{new_album.id}')

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    ar_repo = ArtistRepository(connection)
    artists = ar_repo.all()
    return render_template('artists/all_artists.html', artists=artists)

@app.route('/artists/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    connection = get_flask_database_connection(app)
    ar_repo = ArtistRepository(connection)
    artist = ar_repo.find(artist_id)
    return render_template('artists/one_artist.html', artist=artist, artist_id=artist_id)


@app.route('/artists/new', methods=['GET'])
def get_artist_form():
    return render_template('artists/new_artist.html')

@app.route('/artists', methods=['POST'])
def create_artist():
    name = request.form['Name']
    genre = request.form['Genre']
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)

    artist = Artist(id, name, genre)
    new_artist = repo.create(artist)
    return redirect(f'artists/{new_artist.id}')
    # return Response(status=204)


@app.route('/artists/<artist_id>/albums', methods=['GET'])
def get_albums_by_artist(artist_id):
    connection = get_flask_database_connection(app)
    al_repo = AlbumRepository(connection)
    ar_repo = ArtistRepository(connection)
    albums = al_repo.find_by_artist(artist_id)
    artist = ar_repo.find(artist_id)
    return render_template('artists/albums_by_artist.html', albums=albums, artist=artist)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
