import sqlite3

def get_by_title(title):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title LIKE '%{title}%'
                ORDER BY release_year DESC
                """
        )
        data = cursor.fetchone()
        film = {
            "title": data[0],
            "country": data[1],
            "release_year": data[2],
            "genre": data[3],
            "description": data[4]
        }
        return film

def get_by_years(year_1, year_2):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN {year_1} and {year_2}
                LIMIT 100
                """
        )
        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {
            "title": data[0],
            "release_year": data[1]
            }
            film_list.append(film)
        return film_list

def reiting_child():
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, rating, description
                FROM netflix
                WHERE rating = 'G'
                LIMIT 100
                """
        )
        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {
            "title": data[0],
            "rating": data[1],
            "description": data[2]
            }
            film_list.append(film)
        return film_list

def reiting_family():
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, rating, description
                FROM netflix
                WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13'
                LIMIT 100
                """
        )
        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {
            "title": data[0],
            "rating": data[1],
            "description": data[2]
            }
            film_list.append(film)
        return film_list

def reiting_adult():
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, rating, description
                FROM netflix
                WHERE rating = 'R' OR rating = 'NC-17'
                LIMIT 100
                """
        )
        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {
            "title": data[0],
            "rating": data[1],
            "description": data[2]
            }
            film_list.append(film)
        return film_list

def get_by_genre(genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, description
                FROM netflix
                WHERE  listed_in LIKE '%{genre}%'
                ORDER BY release_year DESC
                LIMIT 10
                """
        )
        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {
            "title": data[0],
            "description": data[1]
            }
            film_list.append(film)
        return film_list

def get_by_cast(actor_1, actor_2):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT COUNT(netflix.cast), netflix.cast
                FROM netflix
                WHERE netflix.cast LIKE '%{actor_1}%' and netflix.cast LIKE '%{actor_2}%'  
                GROUP BY netflix.cast                
                """
        )

    return cursor.fetchall()

def find_a_movie(film_type, release_year, genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, description
                FROM netflix
                WHERE  type = '%{film_type}%' AND release_year = '%{release_year}%' AND listed_in LIKE '%{genre}%'
                """
        )
        return cursor.fetchall()