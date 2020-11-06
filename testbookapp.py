import unittest
from app import app

# Set app to use local mongoDB database
app.config.update({
    'TESTING': True,
    'WTF_CSRF_ENABLED': False,
    'MONGO_URI': 'mongodb://localhost:27017/'})

print(app.config['MONGO_URI'])


class AppRouteTests(unittest.TestCase):

    def test_index(self):
        # Check index loads with content
        tester = app.test_client(self)
        response = tester.get("/")
        decoded = response.data.decode('utf-8')
        statuscode = response.status_code
        print(statuscode)
        self.assertEqual(statuscode, 200)
        assert 'Click a cover for more info' in decoded


class TestReviewScoreValidation(unittest.TestCase):

    def test_score_too_high(self):
        tooBig = app.test_client('/check_review_score/12')
        print(tooBig)
        #self.assertEqual(tooBig, 10)


if __name__ == "__main__":
    unittest.main
