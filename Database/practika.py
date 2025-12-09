# from unittest import result

import psycopg2

class MusicDB:
    def __init__(self):
        self.DB_CONNECTION = psycopg2.connect(
            dbname='music1',
            user='postgres',
            password='1973',
            host='localhost',
            port=5432
        )
        self.DB_CURSOR  = self.DB_CONNECTION.cursor()
        self.__create_tables()

    def __create_tables(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS artists (
            id SERIAL PRIMARY KEY,
            artist VARCHAR(200),
            genre VARCHAR(200));
        
        
        CREATE TABLE IF NOT EXISTS albums (
            id SERIAL PRIMARY KEY,
            album VARCHAR(200),
            album_year INT,
            artist_id INT REFERENCES artists(id),
            album_rework__id INT REFERENCES albums(id));
        """
        self.DB_CURSOR.execute(create_table_query)
        self.DB_CONNECTION.commit()

    def add_artist_and_genre(self):
        artist_name = input("Enter a artist name: ")
        genre = input("Enter a artist genre: ")
        add_artist_query = """
                        INSERT INTO artists (artist, genre) VALUES (%s, %s);
                    """
        self.DB_CURSOR.execute(add_artist_query, (artist_name, genre))
        self.DB_CONNECTION.commit()

    def add_albums(self):
        album_name = input("Enter a album name: ")
        album_year = input("Enter a album year: ")
        artist_id = int(input("Enter artist ID: "))
        album_rework = input("Reworked album ID (press Enter if none): ")
        if album_rework == "":
            album_rework = None
        add_album_query = """
            INSERT INTO albums (album, album_year, artist_id, album_rework__id) VALUES (%s, %s, %s, %s);
        """
        self.DB_CURSOR.execute(add_album_query, (album_name, album_year, artist_id, album_rework))
        self.DB_CONNECTION.commit()

    def album_by_id(self):
        album_year = input("Enter an album year: ")
        album_year_query = """SELECT album FROM albums WHERE album_year = %s;"""
        self.DB_CURSOR.execute(album_year_query, (album_year,))
        result = self.DB_CURSOR.fetchall()
        if not result:
            print("No albums found for this year.")
        else:
            print(f"Albums for year: {result}")




music_db = MusicDB()

while True:
    user_choice = input("Enter an action (1 - exit, 2 - add artist, 3 - add album, 4 - find album by year): ")
    if user_choice == "1":
        break
    elif user_choice == "2":
        music_db.add_artist_and_genre()
    elif user_choice == "3":
        music_db.add_albums()
    elif user_choice == "4":
        music_db.album_by_id()





