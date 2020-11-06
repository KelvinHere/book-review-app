import unittest
import app as appModule

app = appModule.app

# Set app to use local mongoDB database
app.config.update({
    'TESTING': True,
    'WTF_CSRF_ENABLED': False,
    'MONGO_URI': 'mongodb://localhost:27017/'})

print(app.config['MONGO_URI'])


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
