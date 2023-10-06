from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymongo
from pymongo import MongoClient
import json
from time import time


app = Flask(__name__)

def connect_mongo_db():
    print("Connecting to MongoDB...................")
    client = MongoClient('mongodb://mon_user:mon_mot_de_passe@localhost:27017/')
    db = client['spotify']
    collection = db['spotifyCollection']
    return collection



@app.route('/get-result-from-lettre', methods=['GET'])
def get_result_from_lettre():
    lettre = request.args.get('lettre')
    query = {'trackName': {'$regex': '^' + lettre}}
    projection = {'trackName': 1, 'artistName': 1, '_id': 0}
    result = collection.find(query, projection)
    data = [r for r in result]
    return render_template('index.html', result=data)






@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    collection = connect_mongo_db()
    app.run(host='0.0.0.0')