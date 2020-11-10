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

mongo = PyMongo(app)  # Setup mongoDB with Flaskapp
appModule.mongo = mongo  # Inject this new database into app.py


###Commands to check test database is working
#mongo.db.books.insert_one({'TestTitle': 'TitleContent'})
#books = mongo.db.books.find()
#for each in books:
#    print(each)
#colls = mongo.db.list_collection_names()
#for each in colls:
#    print(each)


class MongoDbTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)
        mongo.db.books.delete_many({})


    def test_insert_book(self):
        response = self.app.post('insert_book', follow_redirects=True, data=dict(title= 'Title Test',
                                                               author= 'Author Test',
                                                               rating= '5',
                                                               reviews= [],
                                                               link= 'www.testlink.com',
                                                               buy_link= 'www.testbuylink.com',
                                                               genre= 'test genre',
                                                               summary= 'test summary'))
        print(response)

    def test_index(self):
        # Check index loads with content
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        # Turn searched message into bytes literal and find in response
        self.assertTrue(b'Click a cover for more info' in response.data)


class AppRouteTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    def test_index(self):
        # Check index loads with content
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        # Turn searched message into bytes literal and find in response
        self.assertTrue(b'Click a cover for more info' in response.data)


class TestReviewScoreValidation(unittest.TestCase):

    def test_score_too_high(self):
        result = appModule.check_review_score(90)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main