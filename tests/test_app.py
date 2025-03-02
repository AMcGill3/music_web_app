from playwright.sync_api import expect


def test_get_all_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/albums")

    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        'Title: Doolittle\nReleased: 1989\n',
        'Title: Surfer Rosa\nReleased: 1988\n',
        'Title: Waterloo\nReleased: 1974\n',
        'Title: Super Trouper\nReleased: 1980\n',
        'Title: Lover\nReleased: 2019\n',
        'Title: Folklore\nReleased: 2020\n',
        'Title: I Put a Spell on You\nReleased: 1965\n',
        'Title: Baltimore\nReleased: 1978\n'
    ])

def test_get_one_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        'Title: Doolittle\nReleased: 1989'
    ])

def test_get_all_artists(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/artists")

    link_tags = page.locator("a")
    expect(link_tags).to_have_text([
        'Name: Pixies',
        'Name: ABBA',
        'Name: Taylor Swift',
        'Name: Nina Simone',
        'Add a new artist',
        'Return to home'
    ])

def test_get_one_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/artists/4")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        'Name: Nina Simone\nGenre: Jazz'
    ])

def test_follow_link_to_albums_by_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/artists/2/albums")
    artist_info = page.locator("div").nth(0)
    expect(artist_info).to_have_text([
        'Name: ABBA\nGenre: Pop'
    ])

    album_1 = page.locator('div').nth(1)
    expect(album_1).to_have_text([
        'Title: Waterloo\nReleased: 1974\n'
    ])

    album_2 = page.locator('div').nth(2)
    expect(album_2).to_have_text([
        'Title: Super Trouper\nReleased: 1980\n'
    ])
    
def test_create_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add a new album'")
    page.fill('input[name=title]', 'test album')
    page.fill('input[name=release_year]', '1999')
    page.click("text='Create album'")
    title = page.locator('.t-title')
    release_year = page.locator('.t-release_year')

    expect(title).to_have_text('Title: test album')
    expect(release_year).to_have_text('Released: 1999')

def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add a new artist'")
    page.fill('input[name=Name]', 'test artist')
    page.fill('input[name=Genre]', 'Jazz')
    page.click("text='Create artist'")
    name = page.locator('.t-name')
    genre = page.locator('.t-genre')

    expect(name).to_have_text('Name: test artist')
    expect(genre).to_have_text('Genre: Jazz')

    