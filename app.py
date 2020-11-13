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
    bookOrder = mongo.db.books.find().sort('title', 1)
    return render_template('viewbooks.html', books=bookOrder, sortParameters={'sortField': 'title', 'sortDirection': 1})


@app.route('/sort_books', methods=['POST'])
def sort_books():
    sortField = request.form.get('sortField')
    sortDirection = int(request.form.get('sortDirection'))
    bookOrder = mongo.db.books.find().sort(sortField, sortDirection)
    return render_template('viewbooks.html', books=bookOrder, sortParameters={'sortField': sortField, 'sortDirection': sortDirection})


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
    mongo.db.books.insert_one(formResults)
    return redirect(url_for('view_books'))


@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    return render_template('editbook.html', genres=mongo.db.genres.find(), book=mongo.db.books.find_one({"_id": ObjectId(book_id)}))


@app.route('/update_book/<book_id>', methods=['POST'])
def update_book(book_id):
    formResults = request.form.to_dict()
    # Format form results before submitting to database
    formResults['title'] = formResults['title'].lower()
    formResults['author'] = formResults['author'].lower()
    mongo.db.books.update_one({'_id': ObjectId(book_id)},
                              {'$set': {
                                'title': formResults['title'],
                                'author': formResults['author'],
                                'genre': formResults['genre'],
                                'summary': formResults['summary'],
                                'link': formResults['link'],
                                'buy_link': formResults['buy_link']
                                 }})
    return redirect(url_for('view_books'))


@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.delete_one({'_id': ObjectId(book_id)})
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
    formResults['rating'] = check_review_score(formResults['rating']) # Stop rating average manipulation
    # Insert new review into book
    mongo.db.books.update_one({'_id': ObjectId(formResults['book_id'])},
                              {"$push": {'reviews':
                                         {'_id': ObjectId(),
                                          'reviewer': formResults['name'],
                                          'rating': formResults['rating'],
                                          'review': formResults['review']}}})
    # Update average book score
    update_average_score(formResults['book_id'])
    return redirect(url_for('view_reviews', book_id=formResults['book_id']))


@app.route('/edit_review/<book_id>/<review_id>')
def edit_review(book_id, review_id):
    reviewInfo = list(mongo.db.books.find({'_id': ObjectId(book_id)}, {'reviews': {'$elemMatch': {'_id': ObjectId(review_id)}}}))
    review = reviewInfo[0]['reviews'][0]['review']
    rating = reviewInfo[0]['reviews'][0]['rating']
    return render_template('editreview.html', book_id=book_id, review_id=review_id, review=review, rating=rating)


@app.route('/update_review/<book_id>/<review_id>', methods=['POST'])
def update_review(book_id, review_id):
    checkedReviewScore = check_review_score(request.form.get('new_rating'))
    mongo.db.books.update_one({'_id': ObjectId(book_id), 'reviews._id': ObjectId(review_id)},
                              {'$set': {'reviews.$.review': request.form.get('new_review'),
                                        'reviews.$.rating': checkedReviewScore}})
    update_average_score(book_id)
    return redirect(url_for('view_reviews', book_id=book_id))


@app.route('/delete_review/<book_id>/<review_id>')
def delete_review(book_id, review_id):
    mongo.db.books.update_one({'_id': ObjectId(book_id)},
                              {'$pull': {'reviews':
                                         {'_id': ObjectId(review_id)}}})
    update_average_score(book_id)
    return redirect(url_for('view_reviews', book_id=book_id))


def check_review_score(score):
    score = int(score)
    if score > 10:
        score = 10
    if score < 0:
        score = 0
    return score


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
