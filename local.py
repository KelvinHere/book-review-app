import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

print('##################')
appt = Flask(__name__)
appt.config["MONGO_DBNAME"] = "book_app_db"
appt.config["MONGO_URI"] = 'mongodb://localhost:27017/testdb'
mongo = PyMongo(appt)

appt.config.update({
    'TESTING': True,
    'WTF_CSRF_ENABLED': False
    })

#mongo.db.books.insert_one({'TestTitle': 'TitleContent'})
books = mongo.db.books.find()
for each in books:
    print(each)
colls = mongo.db.list_collection_names()
for each in colls:
    print(each)

#print(mongo.db.books.find())