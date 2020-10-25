import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "book_app_db"

app.config["MONGO_DBNAME"] = DATABASE
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)


@app.route('/')
@app.route('/view_books')
def view_books():
    return render_template('viewbooks.html', books=mongo.db.books.find())


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), 
            debug=True)
