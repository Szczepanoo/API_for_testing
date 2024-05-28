import unittest
import requests
from requests.exceptions import HTTPError, Timeout


class IntegrationTests(unittest.TestCase):

    def test_external_api_posts(self):
        try:
            response = (requests.get
                        ("https://jsonplaceholder.typicode.com/posts",
                         timeout=10))
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
        except HTTPError as http_err:
            self.fail(f"HTTP error occurred: {http_err}")
        except Timeout as timeout_err:
            self.fail(f"Timeout error occurred: {timeout_err}")

    def test_external_api_comments(self):
        try:
            response = (requests.get
                        ("https://jsonplaceholder.typicode.com/comments",
                         timeout=10))
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
        except HTTPError as http_err:
            self.fail(f"HTTP error occurred: {http_err}")
        except Timeout as timeout_err:
            self.fail(f"Timeout error occurred: {timeout_err}")

    def test_external_api_albums(self):
        try:
            response = (requests.get
                        ("https://jsonplaceholder.typicode.com/albums",
                         timeout=10))
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
        except HTTPError as http_err:
            self.fail(f"HTTP error occurred: {http_err}")
        except Timeout as timeout_err:
            self.fail(f"Timeout error occurred: {timeout_err}")

    def test_external_api_photos(self):
        try:
            response = (requests.get
                        ("https://jsonplaceholder.typicode.com/photos",
                         timeout=10))
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
        except HTTPError as http_err:
            self.fail(f"HTTP error occurred: {http_err}")
        except Timeout as timeout_err:
            self.fail(f"Timeout error occurred: {timeout_err}")


if __name__ == "__main__":
    unittest.main()
