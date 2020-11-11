import unittest
import app as appModule
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

#Grap book review app
app = appModule.app

# Set app to use local mongoDB database
app.config.update({
    'TESTING': True,
    'WTF_CSRF_ENABLED': False,
    'MONGO_URI': 'mongodb://localhost:27017/testBookDb'})

mongo = PyMongo(app)  # setup PyMongo object
appModule.mongo = mongo  # overwrite app.py mongo object with this modifed version


class MongoDbTests(unittest.TestCase):
    # Test all app routes that edit delete or update database

    def setUp(self):
        self.app = app.test_client(self)

    def tearDown(self):
        # Remove all test database entries
        mongo.db.books.delete_many({})

    def test_insert_book(self):
        # Test when book inserted its contents appears on viewbooks.html
        self.app.post('insert_book', follow_redirects=True, data=dict(title= 'my test title',
                                                               author= 'author test',
                                                               rating= '5',
                                                               reviews= [],
                                                               link= 'www.testlink.com',
                                                               buy_link= 'www.testbuylink.com',
                                                               genre= 'test genre',
                                                               summary= 'test summary'))
        response = self.app.get("/")
        # Assert all relevent book information is present on view books page
        self.assertTrue(b'my test title' in response.data)
        self.assertTrue(b'Author Test' in response.data)
        self.assertTrue(b'www.testlink.com' in response.data)
        self.assertTrue(b'www.testbuylink.com' in response.data)
        self.assertTrue(b'test summary' in response.data)


    def test_update_book(self):
        # Test update_book route can take an ID and update all fields from form
        bookId = get_id_from_cursor(add_book_return_cursor())  # Create a valid book and get _id
        self.app.post(f'update_book/{bookId}', follow_redirects=True, data=dict(title= 'my test title altered',
                                                               author= 'author test altered',
                                                               rating= '10',
                                                               reviews= [],
                                                               link= 'www.testlinkaltered.com',
                                                               buy_link= 'www.testbuylinkaltered.com',
                                                               genre= 'test genre altered',
                                                               summary= 'test summary altered'))
        response = self.app.get("/")
        # Assert all relevent book information is present on view books page
        self.assertTrue(b'my test title altered' in response.data)
        self.assertTrue(b'Author Test Altered' in response.data)
        self.assertTrue(b'www.testlinkaltered.com' in response.data)
        self.assertTrue(b'www.testbuylinkaltered.com' in response.data)
        self.assertTrue(b'test summary altered' in response.data)

    def test_delete_book(self):
        # Test delete_book route deletes book with given _id
        bookId = get_id_from_cursor(add_book_return_cursor())  # Create a valid book and get _id
        books = mongo.db.books.count_documents({'_id': ObjectId(bookId)}) # Check book exists
        self.assertEqual(books, 1)
        self.app.get(f"/delete_book/{bookId}")
        books = mongo.db.books.count_documents({'_id': ObjectId(bookId)}) # Check book deleted
        self.assertEqual(books, 0)


class AppRouteTests(unittest.TestCase):
    # Test all app routes that only read from the database

    def setUp(self):
        self.app = app.test_client(self)

    def tearDown(self):
        # Remove all test database entries
        mongo.db.books.delete_many({})

    def test_view_books_page(self):
        # Check viewbooks.html loads with content
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Click a cover for more info' in response.data)

    def test_add_book_page(self):
        # Check addbook.html loads with content
        response = self.app.get("/add_book")
        self.assertEqual(response.status_code, 200)
        # Turn searched message into bytes literal and find in response
        self.assertTrue(b'Add a book' in response.data)

    def test_add_review_page(self):
        # Test add review fetches and presents book data from database _id
        bookId = get_id_from_cursor(add_book_return_cursor())
        response = self.app.get("/add_review/{}".format(bookId))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Write a review for' in response.data)
        self.assertTrue(b'My Test Title' in response.data)

    def test_edit_book(self):
        # Test editbook.html reads and presents correct data from database
        bookId = get_id_from_cursor(add_book_return_cursor())
        response = self.app.get("/edit_book/{}".format(bookId))
        self.assertEqual(response.status_code, 200)
        # Assert page title is present
        self.assertTrue(b'Update - My Test Title')
        # Assert book information has been autofilled into form
        self.assertTrue(b'My Test Title' in response.data)
        self.assertTrue(b'Author Test' in response.data)
        self.assertTrue(b'www.testlink.com' in response.data)
        self.assertTrue(b'www.testbuylink.com' in response.data)
        self.assertTrue(b'test summary' in response.data)



class TestReviewScoreValidation(unittest.TestCase):

    def test_score_too_high(self):
        result = appModule.check_review_score(90)
        self.assertEqual(result, 10)


def add_book_return_cursor():
    mongo.db.books.insert_one({'title': 'my test title',
                               'author': 'author test',
                               'rating': 0,
                               'link': 'www.testlink.com',
                               'buy_link': 'www.testbuylink.com',
                               'genre': 'test genre',
                               'summary': 'test summary',
                               'reviews': []})
    return mongo.db.books.find({'title': 'my test title'})[0]

def get_id_from_cursor(cursor):
    bookId = (cursor['_id'])
    return bookId

#Look inside database TEMP
#books = mongo.db.books.find()
#for each in books:
#    print(each)
#colls = mongo.db.list_collection_names()
#for each in colls:
#    print(each)
#print('')

if __name__ == "__main__":
    unittest.main