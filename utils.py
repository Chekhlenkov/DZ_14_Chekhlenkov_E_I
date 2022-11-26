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
            f"""
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN {year_1} AND {year_2}
            LIMIT 100
            """
        )
        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {
                "title": i[0],
                "release_year": i[1]
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
            "title": i[0],
            "rating": i[1],
            "description": i[2]
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
            "title": i[0],
            "rating": i[1],
            "description": i[2]
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
            "title": i[0],
            "rating": i[1],
            "description": i[2]
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
            "title": i[0],
            "description": i[1]
            }
            film_list.append(film)
        return film_list


def get_by_cast(actor_1, actor_2):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        actors = []
        answer = []
        cursor.execute(
            f"""SELECT netflix.cast
                FROM netflix
                WHERE netflix.cast LIKE '%{actor_1}%' AND netflix.cast LIKE '%{actor_2}%'  
                GROUP BY netflix.cast                
                """
        )
        data = cursor.fetchall()
        for string in data:
            string = str(string).replace('(','').replace(')','').replace("'","")
            spisok = string.split(', ')
            spisok.remove(actor_1)
            spisok.remove(actor_2)
            for name in spisok:
                actors.append(name)
        all_actors = set(actors)
        for i in all_actors:
            kolvo = actors.count(i)
            if kolvo >2:
                answer.append(i)
    return answer


def find_a_movie(film_type, release_year, genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT title, description
            FROM netflix
            WHERE  type = {film_type} AND release_year = {release_year} AND listed_in LIKE '%{genre}%'
            """
        )
        return cursor.fetchall()