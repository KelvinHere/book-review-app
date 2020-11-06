import unittest
import app as appModule
from flask_pymongo import PyMongo

# Create app instance
app = appModule.app

# Set app to use local mongoDB database
app.config.update({
    'TESTING': True,
    'WTF_CSRF_ENABLED': False,
    'MONGO_URI': 'mongodb://localhost:27017/'})

mongo = PyMongo(app)


class TestReviewScoreValidation(unittest.TestCase):

    def test_score_too_high(self):
        tooBig = app.check_review_score(12)
        self.assertEqual(tooBig, 10)

    def test_score_too_low(self):
        tooLow = app.check_review_score(-20)
        self.assertEqual(tooLow, 0)

    def test_score_correct(self):
        correct = app.check_review_score(3)
        self.assertEqual(correct, 3)

    def test_score_string_passed(self):
        string = app.check_review_score('2')
        self.assertEqual(string, 2)
