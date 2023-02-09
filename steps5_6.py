
import json
from main import connect
def step6(type, year, genre):
    with open("movies.json", "w", encoding="utf-8") as file:
        rows = ['title', 'description']
        query = f"""SELECT {', '.join(rows)} 
                    FROM netflix 
                    WHERE `type` LIKE ? AND release_year LIKE ? AND listed_in LIKE ?"""
        response = connect(query, (f'%{type}%', f'%{year}%', f'%{genre}%'))
        result = {}
        for movie in response:
            for i in range(len(rows)):
                result[rows[i]] = movie[i]

        json.dump(result, file)

        return result



def step5(actor1, actor2):
    with open("actors.json", "w", encoding="utf-8") as file:
        rows = ["cast"]
        query = f"""SELECT `cast`
                    FROM netflix 
                    WHERE `cast` LIKE ? AND `cast` LIKE ?"""
        response = connect(query, (f'%{actor1}%', f'%{actor2}%'))
        result = {}
        for movie in response:
            for i in range(len(rows)):
                result[rows[i]] = movie[i]
        json.dump(result, file)
        return result


