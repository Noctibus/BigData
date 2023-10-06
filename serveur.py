from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymongo
from pymongo import MongoClient
import json
from time import time


def connect_mongo_db(lettre:str):
    print("Connecting to MongoDB...................")
    client = MongoClient('mongodb://mon_user:mon_mot_de_passe@localhost:27017/')
    db = client['spotify']
    collection = db['spotifyCollection']
    # trackname must start with the letter lettre.
    query = {'trackName': {'$regex': '^' + lettre}}
    # get only the values of trackName and artistName
    projection = {'trackName': 1, 'artistName': 1, '_id': 0}
    # get the result of the query
    result = collection.find(query, projection)
    return result


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/home', methods=['GET'])
def home():
    query = request.args.get('query')
    print("Query1: ", query)
    if query is None:
        query = ""
    print("Query2: ", query)
    result = connect_mongo_db(query)
    documents = [document for document in result]
    return render_template('index.html', result=documents)


if __name__ == '__main__':
    app.run(host='0.0.0.0')