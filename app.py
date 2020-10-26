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


@app.route('/add_book')
def add_book():
    return render_template('addbook.html', genres=mongo.db.genres.find().sort([('genre_name', 1)]))


@app.route('/insert_book', methods=['POST'])
def insert_book():
    formResults = request.form.to_dict()
    # Format form results before submitting to database
    for k, v in formResults.items():
        if k != 'summary':
            formResults[k] = v.lower()

    formResults['rating'] = 0
    mongo.db.books.insert(formResults)
    return redirect(url_for('view_books'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), 
            debug=True)

