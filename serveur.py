from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymongo
from pymongo import MongoClient
import json


def connect_mongo_db():
    # Connexion à la base de données. User: mon_user, pswd: mon_mot_de_passe
    client = MongoClient('mongodb://mon_user:mon_mot_de_passe@localhost:27017/')
    # Récupération de la base de données
    db = client['spotify']
    collection = db['spotifyCollection']
    print("Connexion à la base de données réussie !")


app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    connect_mongo_db()
    app.run(host='0.0.0.0')