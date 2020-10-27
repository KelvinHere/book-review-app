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
    formResults['reviews'] = 0
    mongo.db.books.insert(formResults)
    return redirect(url_for('view_books'))


@app.route('/add_review/<book_id>')
def add_review(book_id):
    return render_template('addreview.html', book=mongo.db.books.find_one({"_id": ObjectId(book_id)}))


@app.route('/insert_review', methods=['POST'])
def insert_review():
    formResults = request.form.to_dict()
    # Format reviewer name
    formResults['name'] = formResults['name'].lower()
    # Stop rating average manipulation
    formResults['rating'] = int(formResults['rating'])
    if formResults['rating'] > 5:
        formResults['rating'] = 5
    if formResults['rating'] < 0:
        formResults['rating'] = 0
    
    # Increment number of reviews books.book._id has
    bookID = formResults['book_id']
    reviews = mongo.db.books.find_one({"_id": bookID})
    print(type(bookID))
    print('##############################################')
    for k, v in formResults.items():
        print(k, v)
    print(reviews)


    mongo.db.books.update({'_id': formResults['book_id']}, {"$set": {"reviews": 5}})
    # Update review collection with new review
    mongo.db.reviews.insert(formResults)
    return redirect(url_for('view_books'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), 
            debug=True)

