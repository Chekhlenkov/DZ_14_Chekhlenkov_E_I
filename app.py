from flask import Flask, jsonify
from utils import get_by_title, get_by_genre, get_by_years, reiting_adult, reiting_child, reiting_family, get_by_cast

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/movie/<title>")
def get_fil_by_title(title):
    film = get_by_title(title)
    return jsonify(film)


@app.route("/<int:year_1>/to/<int:year_2>")
def get_fil_years(year_1, year_2):
    films = get_by_years(year_1, year_2)
    return jsonify(films)


@app.route("/rating/children")
def get_for_child():
    films = reiting_child()
    return jsonify(films)


@app.route("/rating/family")
def get_for_family():
    films = reiting_family()
    return jsonify(films)


@app.route("/rating/adult")
def get_for_adult():
    films = reiting_adult()
    return jsonify(films)


@app.route("/<actor1>/<actor2>")
def films_by_actors(actor1, actor2):
    films = get_by_cast(actor1, actor2)
    return jsonify(films)


@app.route("/genre/<genre>")
def films_by_genre(genre):
    films = get_by_genre(genre)
    return jsonify(films)


if __name__ == '__main__':
    app.run(debug=True)
