import unittest
from unittest.mock import patch
from main import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_favicon(self):
        response = self.app.get('/favicon.ico')
        self.assertEqual(response.status_code, 302)

    def test_css(self):
        response = self.app.get('/static/style.css')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('main.requests.get')
    def test_get_posts_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'title': 'Test Post'}]
        response = self.app.get('/posts')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Post', response.data)

    @patch('main.requests.get')
    def test_get_posts_failure(self, mock_get):
        mock_get.return_value.status_code = 500
        response = self.app.get('/posts')
        self.assertEqual(response.status_code, 500)

    @patch('main.requests.get')
    def test_set_display_limit(self, mock_get):
        mock_get.return_value.status_code = 200
        response = self.app.post('/set_display_limit', json={'limit': 10})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Display limit set to 10', response.data)

    @patch('main.requests.get')
    def test_search_posts(self, mock_get):
        mock_get.return_value.status_code = 200
        response = self.app.post('/search_posts', json={'min_length': 5,
                                                        'max_length': 10})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Searching posts with character '
                      b'length between 5 and 10', response.data)

    def test_handle_error(self):
        with patch('main.requests.get') as mock_get:
            mock_get.side_effect = Exception('Test Error')
            response = self.app.get('/posts')
            self.assertEqual(response.status_code, 500)
            self.assertIn(b'An unexpected error occurred', response.data)


class TestContract(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('main.requests.get')
    def test_get_posts_integration(self, mock_get):
        # Przygotowanie fałszywej odpowiedzi od zewnętrznego API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'title': 'Test Post'}]

        # Wywołanie endpointu /posts w aplikacji
        response = self.app.get('/posts')

        # Sprawdzenie, czy odpowiedź od zewnętrznego API jest przetwarzana i zwracana poprawnie
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Post', response.data)

    @patch('main.requests.post')
    def test_set_display_limit_integration(self, mock_post):
        # Przygotowanie fałszywej odpowiedzi od zewnętrznego API
        mock_post.return_value.status_code = 200

        # Wywołanie endpointu /set_display_limit w aplikacji
        response = self.app.post('/set_display_limit', json={'limit': 10})

        # Sprawdzenie, czy odpowiedź od zewnętrznego API jest przetwarzana i zwracana poprawnie
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Display limit set to 10', response.data)


if __name__ == '__main__':
    unittest.main()
