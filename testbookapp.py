import unittest
import app as appModule
from flask_pymongo import PyMongo

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

    def setUp(self):
        self.app = app.test_client(self)
        mongo.db.books.delete_many({})


    def test_insert_book(self):
        # Test when book inserted its contents appears on viewbooks.html
        self.app.post('insert_book', follow_redirects=True, data=dict(title= 'Title Test',
                                                               author= 'Author Test',
                                                               rating= '5',
                                                               reviews= [],
                                                               link= 'www.testlink.com',
                                                               buy_link= 'www.testbuylink.com',
                                                               genre= 'test genre',
                                                               summary= 'test summary'))
        response = self.app.get("/")
        self.assertTrue(b'Title Test' in response.data)
        self.assertTrue(b'Author Test' in response.data)
        self.assertTrue(b'www.testlink.com' in response.data)
        self.assertTrue(b'www.testbuylink.com' in response.data)
        self.assertTrue(b'test summary' in response.data)


class AppRouteTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    def test_index_page(self):
        # Check index loads with content
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        # Turn searched message into bytes literal and find in response
        self.assertTrue(b'Click a cover for more info' in response.data)

    def test_add_book_page(self):
        # Check index loads with content
        response = self.app.get("/add_book")
        self.assertEqual(response.status_code, 200)
        # Turn searched message into bytes literal and find in response
        self.assertTrue(b'Add a book' in response.data)

   ''' def test_add_review_page(self):
        # Check index loads with content
        response = self.app.get("/add_review")
        self.assertEqual(response.status_code, 200)
        # Turn searched message into bytes literal and find in response
        self.assertTrue(b'Write a review for' in response.data)
'''

class TestReviewScoreValidation(unittest.TestCase):

    def test_score_too_high(self):
        result = appModule.check_review_score(90)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main