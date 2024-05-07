from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_comments(self):
        self.client.get("/comments")

    @task
    def get_albums(self):
        self.client.get("/albums")

    @task
    def get_photos(self):
        self.client.get("/photos")

    @task
    def set_display_limit(self):
        self.client.post("/set_display_limit", json={"limit": 10})