import unittest
from main import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to JSONPlaceholder App', response.data)

    def test_get_posts(self):
        response = self.app.get('/posts')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Posts', response.data)

    def test_get_comments(self):
        response = self.app.get('/comments')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comments', response.data)

    def test_get_albums(self):
        response = self.app.get('/albums')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Albums', response.data)

    def test_get_photos(self):
        response = self.app.get('/photos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Photos', response.data)

    def test_set_display_limit_valid(self):
        response = self.app.post('/set_display_limit', json={'limit': 10})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Display limit set to 10', response.data)

    def test_set_display_limit_invalid(self):
        response = self.app.post('/set_display_limit', json={'limit': -1})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid display limit', response.data)

    def test_search_posts(self):
        response = (self.app.post
                    ('/search_posts', json={'min_length': 10, 'max_length': 100}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Searching posts with character length', response.data)


if __name__ == "__main__":
    unittest.main()
