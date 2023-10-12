from pymongo import MongoClient

def connect_mongo_db():
    print("Connecting to MongoDB...................")
    client = MongoClient('mongodb://mon_user:mon_mot_de_passe@localhost:27017/')
    db = client['spotify']
    collection = db['spotifyCollection']
    return collection