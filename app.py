import json

from flask import (Flask, request)

app = Flask(__name__)

ID = 0
animes = [];

@app.route('/anime', methods=('GET',))
def get_animes():
    if request.method == 'GET':
        return json.dumps(animes)


@app.route('/anime', methods=('POST',))
def create():
    if request.method == 'POST':
        anime = dict()
        anime['id'] = ID
        anime['title'] = request.form['title']
        anime['format'] = request.form['format']
        anime['season'] = request.form['season']
        anime['score'] = int(request.form['score'])
        print(request.form['genre'])
        animes.append(anime)
        ID+=1

        return json.dumps(anime)

@app.route('/anime/<int:id>', methods=('GET',))
def get_anime(id):
    for anime in animes:
        if anime['id'] == id:
            return json.dumps(anime)
    return "{}"

@app.route('/anime/<int:id>', methods=('PUT',))
def update_anime(id):
    for anime in animes:
        if anime['id'] == id:
            for key in request.form:
                anime[key]=request.form[key]
            return json.dumps(anime)
    return "{}"

@app.route('/anime/<int:id>', methods=('PATCH',))
def patch_anime(id):
    for anime in animes:
        if anime['id'] == id:
            for key in request.form:
                anime[key]=request.form[key]
            return json.dumps(anime)
    return "{}"

@app.route('/anime/<int:id>', methods=('DELETE',))
def delete_anime(id):
    for i in range(len(animes)):
        if animes[i]['id'] == id:
            animes.pop(i)
            return json.dumps(animes[i])
    return "{}"
