from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymongo
from pymongo import MongoClient
import pandas as pd


app = Flask(__name__)

def connect_mongo_db():
    print("Connecting to MongoDB...................")
    client = MongoClient('mongodb://mon_user:mon_mot_de_passe@localhost:27017/')
    db = client['spotify']
    collection = db['spotifyCollection']
    return collection


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
    data = [r for r in result]
    return render_template('index.html', result=data)


@app.route('/get-result-from-genre', methods=['GET'])
def get_result_from_genre():
    genre = request.args.get('genre')
    query = {'genre': {'$regex': genre, '$options': 'i'}}
    projection = {'genre': 1, 'artistName': 1, '_id': 0}
    result = collection.find(query, projection)
    data = [r for r in result]
    return render_template('index.html', result=data)
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



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    collection = connect_mongo_db()
    app.run(host='0.0.0.0')