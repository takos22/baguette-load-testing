# Baguette load testing

Comparing baguette to other popular web frameworks: [Flask](https://flask.palletsprojects.com/),
[Quart](https://pgjones.gitlab.io/quart/) and [FastAPI](https://fastapi.tiangolo.com/).

This is using the [locust](https://locust.io/) module for load testing.

## Configuration

You need to install the requirements from [requirements.txt](./requirements.txt) in a virtual
environment, then install `locust` in another virtualenv because locust uses flask 1 and the
servers run flask 2.

You need to open a terminal for each server then run them with `py baguette_server.py`,
then open a new terminal and start locust with `locust --web-host=127.0.0.1 --web-port 8080`.
Then you can open http://127.0.0.1:8080 and start the swarming.

## My results

Your results may vary because you don't have the same hardware as me.

| Framework                 | Average request time (ms) | Requests/second |
|---------------------------|--------------------------:|----------------:|
| FastAPI                   | 12                        | 71.6            |
| Baguette                  | 13                        | 71.2            |
| Quart with Uvicorn server | 13                        | 66.1            |
| Quart                     | 14                        | 65.6            |
| Flask                     | 20                        | 44.2            |
| Flask async               | 22                        | 42.1            |
