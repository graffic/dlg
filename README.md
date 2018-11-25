# DLG Software Engineer Python Test

[![Build Status](https://travis-ci.org/graffic/dlg.svg?branch=master)](https://travis-ci.org/graffic/dlg)
[![codecov](https://codecov.io/gh/graffic/dlg/branch/master/graph/badge.svg)](https://codecov.io/gh/graffic/dlg)

The application endpoint is available here: http://dlgassignment.eu-gb.mybluemix.net/total

## Introduction

This repo contains the technical assigment for DLG using python.

This documents contains the assumptions and all the points I consider worth of notice with my take on them.

### Requirements

* Python 3.7 if you want to run or develop the app.
* Docker if you want just to run it.


### Building and running

Make sure you have python `3.7` installed in your system and `pipenv`. Then run `pipenv sync -d` from the root directory of the project. After that you can run the application with `pipenv run python -m app`. The endpoint will be available on http://localhost:5000/total

If you prefer to run the app in a container:

```
docker build -t dlg .
docker run --rm -it -p 5000:5000 dlg
```

## The service

Files are organized into two folders `app` with the application and `tests` for the tests of the application.

The application uses pipenv to manage dependencies as an better alternative to a `requirements.txt` file when developing applications.

### The service

The service provides an HTTP API using the `quart` framework. It is like `flask` but using asyncio.

Since there is only one endpoint some things are overengineered a bit:

* There is a `numbers_api` module assuming that a client for the real API providing the numbers would exist. It also simulates a delay of one second.
* The endpoint is in a blueprint (even if it is only one), to show a way to organice different endpoint groups in their own files.
* The app object creation it's in its in own file, even if it's only two lines.

#### The sum

Even if the service uses asyncio, the sum of a large amount of numbers as the one given in the example can take around `100ms`. During that CPU bound task the server wont be able to respond unless there is more than one worker.

Taking the CPU bound task into an external process using a `ProcessPoolExecutor()` and `loop.run_in_executor` adds around 2 seconds. So I chose to let it run in the event loop.


### Tests

There is code to test, although not much. The service has two kind of tests:

* Integration (`test_integration.py`): Test the entire application as a black box.
* Unit (`test_total.py`): There are unit tests only for the total module.