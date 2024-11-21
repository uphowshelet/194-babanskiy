from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lab1 import setup_database, create_session, NationalNames, StateNames  # Подключаем модели из ORM

# Инициализация базы данных
engine = setup_database("sqlite:///Chinook_Sqlite.sqlite")
session = create_session(engine)

# CREATE (Создание)


def add_nationalname(id, name,, media_type_id, genre_id, composer, milliseconds, bytes_, unit_price):
    new_baby = NationalNames(
        Name=name,
        AlbumId=album_id,
        MediaTypeId=media_type_id,
        GenreId=genre_id,
        Composer=composer,
        Milliseconds=milliseconds,
        Bytes=bytes_,
        UnitPrice=unit_price
    )
    session.add(new_track)
    session.commit()
    print(f"Baby with name '{name}' added with ID: {new_baby.Id}")
    return new_baby.Id

# READ (Чтение)
def get_artist_by_id(artist_id):
    artist = session.query(Artist).filter_by(ArtistId=artist_id).first()
    if artist:
        print(f"Artist: {artist.Name}")
        return artist
    else:
        print(f"Artist with ID {artist_id} not found.")
        return None

def get_all_albums():
    albums = session.query(Album).all()
    for album in albums:
        print(f"Album ID: {album.AlbumId}, Title: {album.Title}")
    return albums

def get_tracks_by_album(album_id):
    tracks = session.query(Track).filter_by(AlbumId=album_id).all()
    print(f"Tracks in Album ID {album_id}:")
    for track in tracks:
        print(f"- {track.Name}")
    return tracks

# UPDATE (Обновление)
def update_artist_name(artist_id, new_name):
    artist = session.query(Artist).filter_by(ArtistId=artist_id).first()
    if artist:
        artist.Name = new_name
        session.commit()
        print(f"Artist ID {artist_id} updated to '{new_name}'")
        return artist
    else:
        print(f"Artist with ID {artist_id} not found.")
        return None

def update_album_title(album_id, new_title):
    album = session.query(Album).filter_by(AlbumId=album_id).first()
    if album:
        album.Title = new_title
        session.commit()
        print(f"Album ID {album_id} updated to '{new_title}'")
        return album
    else:
        print(f"Album with ID {album_id} not found.")
        return None

# DELETE (Удаление)
def delete_artist(artist_id):
    artist = session.query(Artist).filter_by(ArtistId=artist_id).first()
    if artist:
        session.delete(artist)
        session.commit()
        print(f"Artist ID {artist_id} deleted.")
    else:
        print(f"Artist with ID {artist_id} not found.")

def delete_album(album_id):
    album = session.query(Album).filter_by(AlbumId=album_id).first()
    if album:
        session.delete(album)
        session.commit()
        print(f"Album ID {album_id} deleted.")
    else:
        print(f"Album with ID {album_id} not found.")

def delete_track(track_id):
    track = session.query(Track).filter_by(TrackId=track_id).first()
    if track:
        session.delete(track)
        session.commit()
        print(f"Track ID {track_id} deleted.")
    else:
        print(f"Track with ID {track_id} not found.")

# Примеры использования
if __name__ == "__main__":
    # Создание
    artist_id = add_artist("New Artist")
    album_id = add_album("New Album", artist_id)
    add_track("New Track", album_id, media_type_id=1, genre_id=1, composer="Composer", milliseconds=300000, bytes_=5000000, unit_price=0.99)

    # Чтение
    get_artist_by_id(artist_id)
    get_all_albums()
    get_tracks_by_album(album_id)

    # Обновление
    update_artist_name(artist_id, "Updated Artist")
    update_album_title(album_id, "Updated Album")

    # Удаление
    delete_track(1)  # Удаление трека по ID
    delete_album(album_id)
    delete_artist(artist_id)