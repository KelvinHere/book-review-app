import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

# Create flask app and configure database
app = Flask(__name__)
app.config["MONGO_DBNAME"] = "book_app_db"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)


# -------------------------------------------------- Book realted views
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
    formResults['title'] = formResults['title'].lower()
    formResults['author'] = formResults['author'].lower()
    # Initialise variables not included in form
    formResults['rating'] = 0
    formResults['reviews'] = []
    mongo.db.books.insert(formResults)
    return redirect(url_for('view_books'))


@app.route('/edit_book/')
def edit_book():
    return render_template('editbook.html', books=mongo.db.books.find())


@app.route('/update_book/<book_id>', methods=['POST'])
def update_book(book_id):
    return redirect(url_for('view_books'))


# -------------------------------------------------- Review realted views
@app.route('/view_reviews/<book_id>')
def view_reviews(book_id):
    reviewInfo = mongo.db.books.find_one({'_id': ObjectId(book_id)},
                                         {'title': (),
                                          'rating': (),
                                          'reviews': (),
                                          '_id': 0})
    bookTitle = reviewInfo['title']
    bookRating = reviewInfo['rating']
    reviews = reviewInfo['reviews']
    return render_template('viewreviews.html', reviews=reviews, bookTitle=bookTitle, bookRating=bookRating, book_id=book_id)


@app.route('/add_review/<book_id>')
def add_review(book_id):
    return render_template('addreview.html', book=mongo.db.books.find_one({"_id": ObjectId(book_id)}))


@app.route('/insert_review', methods=['POST'])
def insert_review():
    formResults = request.form.to_dict()
    formResults['name'] = formResults['name'].lower()  # Format reviewer name

    # Stop rating average manipulation
    formResults['rating'] = int(formResults['rating'])
    if formResults['rating'] > 10:
        formResults['rating'] = 10
    if formResults['rating'] < 0:
        formResults['rating'] = 0

    # Update book with new review
    mongo.db.books.update_one({'_id': ObjectId(formResults['book_id'])},
                              {"$push": {'reviews':
                                         {'_id': ObjectId(),
                                          'reviewer': formResults['name'],
                                          'rating': formResults['rating'],
                                          'review': formResults['review']}}})
    # Update average book score
    update_average_score(formResults['book_id'])
    return redirect(url_for('view_books'))


@app.route('/delete_review/<book_id>/<review_id>')
def delete_review(book_id, review_id):
    mongo.db.books.update_one({'_id': ObjectId(book_id)},
                          {'$pull': {'reviews':
                                     {'_id': ObjectId(review_id)}}})
    update_average_score(book_id)
    return redirect(url_for('view_reviews', book_id=book_id))

def update_average_score(book_id):
    # Updates the average review score by book_id
    currentBookReviews = mongo.db.books.find_one({'_id': ObjectId(book_id)},
                                                 {'reviews': (),
                                                  '_id': 0})['reviews']
    totalReviews = len(currentBookReviews)
    totalRating = 0
    for review in currentBookReviews:
        totalRating += int(review['rating'])
    if totalReviews > 0:
        newRating = round(totalRating / totalReviews)
    else:
        newRating = 0
    mongo.db.books.update_one({'_id': ObjectId(book_id)},
                              {'$set': {'rating': newRating}})


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
