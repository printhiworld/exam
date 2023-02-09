from flask import Flask
import sqlite3

app = Flask(__name__)


def connect(query, params, db="netflix.db"):
    with sqlite3.connect(db) as con:
        cur = con.cursor()
        cur.execute(query, params)
        result = cur.fetchall()

    return result


@app.route("/movie/<title>/")
def page_Title(title):
    rows = ['title', 'country', 'release_year', 'description', 'listed_in']
    query = f"""SELECT {', '.join(rows)} 
            FROM netflix 
            WHERE title LIKE ? 
            ORDER BY release_year"""

    response = connect(query, (f"%{title}%",))
    result = {}
    for movie in response:
        for i in range(len(rows)):
            result[rows[i]] = movie[i]
    return result

@app.route("/movie/<year_start>/to/<year_end>")
def page_year(year_start, year_end):
    rows = ['title', 'release_year']
    query = f"""SELECT {', '.join(rows)} 
            FROM netflix 
            WHERE release_year BETWEEN ? AND ?
            ORDER BY release_year"""

    response = connect(query, (year_start, year_end,))
    result = []
    for j in range(min(100, len(response))):
        movie = {}
        for i in range(len(rows)):
            movie[rows[i]] = response[j][i]
        result.append(movie)
    return result



@app.route("/rating/children")
def page_children():
    rows = ['title', 'rating', 'description']
    query = f"""SELECT {', '.join(rows)} 
            FROM netflix 
            WHERE rating LIKE ? 
            ORDER BY release_year"""

    response = connect(query, ('G',))
    result = []
    for j in range(min(100, len(response))):
        movie = {}
        for i in range(len(rows)):
            movie[rows[i]] = response[j][i]
        result.append(movie)
    return result



@app.route("/rating/family")
def page_family():
    rows = ['title', 'rating', 'description']
    query = f"""SELECT {', '.join(rows)} 
            FROM netflix 
            WHERE rating=? or rating=? or rating=?
            ORDER BY release_year"""

    response = connect(query, ('G', 'PG', 'PG-13'))
    result = []
    for j in range(min(100, len(response))):
        movie = {}
        for i in range(len(rows)):
            movie[rows[i]] = response[j][i]
        result.append(movie)
    return result



@app.route("/rating/adult")
def page_adult():
    rows = ['title', 'rating', 'description']
    query = f"""SELECT {', '.join(rows)} 
            FROM netflix 
            WHERE rating=? or rating=?
            ORDER BY release_year"""

    response = connect(query, ('R', 'NC-17'))
    result = []
    for j in range(min(100, len(response))):
        movie = {}
        for i in range(len(rows)):
            movie[rows[i]] = response[j][i]
        result.append(movie)
    return result



@app.route("/genre/<genre>")
def page_genre(genre):
    rows = ['title', 'description']
    query = f"""SELECT {', '.join(rows)} 
            FROM netflix 
            WHERE listed_in LIKE ? 
            ORDER BY release_year"""

    response = connect(query, (f"%{genre}%",))
    result = []
    for j in range(min(10, len(response))):
        movie = {}
        for i in range(len(rows)):
            movie[rows[i]] = response[j][i]
        result.append(movie)
    return result


def step5(actor1, actor2):
    #актеры игравшие с ними двумя более 2 раз
    pass




if __name__ == '__main__':
    app.run(debug=True)
'''order by  выводит старые фильмы'''