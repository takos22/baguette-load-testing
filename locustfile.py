from locust import HttpUser, TaskSet, task


class Tasks(TaskSet):
    @task
    def index(self):
        with self.client.get(
            "/" + self.user.name.lower(), catch_response=True
        ) as response:
            if response.status_code != 200 or response.text != "Hello, World!":
                response.failure(
                    "{}: Expected: {} {}; got: {} {}".format(
                        self.user.name,
                        200,
                        "Hello, World!",
                        response.status_code,
                        response.text,
                    )
                )


class BaguetteUser(HttpUser):
    tasks = [Tasks]
    host = "http://127.0.0.1:8000"
    name = "Baguette"


class FastAPIUser(HttpUser):
    tasks = [Tasks]
    host = "http://127.0.0.1:8001"
    name = "FastAPI"


class FlaskAsyncUser(HttpUser):
    tasks = [Tasks]
    host = "http://127.0.0.1:8002"
    name = "Flask-Async"


class FlaskUser(HttpUser):
    tasks = [Tasks]
    host = "http://127.0.0.1:8003"
    name = "Flask"


class QuartUser(HttpUser):
    tasks = [Tasks]
    host = "http://127.0.0.1:8004"
    name = "Quart"


class QuartUvicornUser(HttpUser):
    tasks = [Tasks]
    host = "http://127.0.0.1:8005"
    name = "Quart-Uvicorn"
