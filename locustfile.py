from locust import HttpLocust
from locust import TaskSet
from locust import task


def login(l):
    l.client.post("/login", {"username": "Alexander.Loechel", "password": ""})


class UserBehavior(TaskSet):

    def on_start(self):
        """on_start is called when a Locust start before any task is scheduled.

        Classical Test setup step.
        """
        login(self)

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/profile")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
