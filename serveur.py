from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymongo
from pymongo import MongoClient
import pandas as pd
from connect_mongo import connect_mongo_db


app = Flask(__name__)


def render_result(result):
    data = [r for r in result]
    df = pd.DataFrame(data)
    df.columns = ['trackName', 'artistName']
    html_table = df.to_html()
    return render_template('index.html', result=html_table)


@app.route('/get-result-from-lettre', methods=['GET'])
def get_result_from_lettre():
    lettre = request.args.get('lettre')
    query = {'trackName': {'$regex': '^' + lettre}}
    projection = {'trackName': 1, 'artistName': 1, '_id': 0}
    result = collection.find(query, projection)
    return render_result(result)



@app.route('/get-result-from-genre', methods=['GET'])
def get_result_from_genre():
    genre = request.args.get('genre')
    query = {'genre': {'$regex': genre, '$options': 'i'}}
    projection = {'genre': 1, 'artistName': 1, '_id': 0}
    result = collection.find(query, projection)
    count = collection.count_documents(query)
    if count == 0:
        errormessage="Aucun résultat trouvé pour le genre spécifié."
        return render_template('index.html', errormessage=errormessage)
    else :
        errormessage=None
        return render_result(result)


@app.route('/get-result-sorted', methods=['GET'])
def get_result_sorted():
    sort_required = request.args.get('sorting')
    sort_order = request.args.get('order')
    projection = {'trackName': 1, 'artistName': 1, '_id':0}
    if sort_order == "Ascending":
      order = pymongo.ASCENDING
    else :
      order = pymongo.DESCENDING
    result = collection.find(projection=projection).sort(sort_required, direction=order)
    return render_result(result)


@app.route('/analytics', methods=['GET'])
def analytics():
    genre_danceability = {}
    genre_count = {}
    genres_list = []
    for document in collection.find():
        if 'genre' in document and 'danceability' in document:
            genre = document.get('genre')
            danceability = document.get('danceability')
            if genre in genre_count:
                genre_count[genre] += 1
                genre_danceability[genre] += danceability
            else:
                genre_count[genre] = 1
                genre_danceability[genre] = danceability
    
    for document in collection.find():
        if 'danceability' in document :
            danceability=document.get('danceability')
        if 'genre' in document:
            genre=document.get('genre')
            if genre not in genres_list:
                genres_list.append(genre)
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1
                
    average_danceability_by_genre = {}
    for genre in genre_count:
        average_danceability_by_genre[genre] = genre_danceability[genre] / genre_count[genre]
                            
    return render_template('analytics.html',**locals())
 
@app.route('/search', methods=['GET'])
def search():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('search'))

if __name__ == '__main__':
    collection = connect_mongo_db()
    app.run(host='0.0.0.0')