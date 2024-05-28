import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_navigate_posts(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        self.assertIn("JSONPlaceholder App", driver.title)
        posts_link = driver.find_element(By.LINK_TEXT, "Posts")
        posts_link.click()
        self.assertIn("Posts", driver.title)

    def test_navigate_comments(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        self.assertIn("JSONPlaceholder App", driver.title)
        comments_link = driver.find_element(By.LINK_TEXT, "Comments")
        comments_link.click()
        self.assertIn("Comments", driver.title)

    def test_navigate_albums(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        self.assertIn("JSONPlaceholder App", driver.title)
        albums_link = driver.find_element(By.LINK_TEXT, "Albums")
        albums_link.click()
        self.assertIn("Albums", driver.title)

    def test_navigate_photos(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        self.assertIn("JSONPlaceholder App", driver.title)
        photos_link = driver.find_element(By.LINK_TEXT, "Photos")
        photos_link.click()
        self.assertIn("Photos", driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
