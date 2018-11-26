# DLG Software Engineer Python Test

[![Build Status](https://travis-ci.org/graffic/dlg.svg?branch=master)](https://travis-ci.org/graffic/dlg)
[![codecov](https://codecov.io/gh/graffic/dlg/branch/master/graph/badge.svg)](https://codecov.io/gh/graffic/dlg)

The application endpoint is available here: http://dlgassignment.eu-gb.mybluemix.net/total

## Introduction

This repository is the python technical assignment for DLG. The README contains the assumptions and all the points I consider worth of notice with my take on them. 

Given that these assignments take some of my free time, I usually try to learn something new. For this one I wanted to try: [pipenv dependency manager](https://pipenv.readthedocs.io/en/latest/), [quart web framework](https://gitlab.com/pgjones/quart), and (IBM Cloud)[https://www.ibm.com/cloud/]

### Requirements

* Python 3.7 if you want to run or develop the app.
* Docker if you want just to run it.

### Building and running

The easiest way is using the currently deployed container and run it locally: `docker run --rm -it -p 5000:5000 docker.io/graffic/dlg`

If you prefer to build the container first:

```
docker build -t dlg .
docker run --rm -it -p 5000:5000 dlg
```

Last but not least, for a development environment make sure you have python `3.7` and `pipenv` installed in your system. Then run `pipenv sync -d` from the root directory of the project. After that you can run the application with `pipenv run python -m app`. The endpoint will be available on http://localhost:5000/total


## The service

Files are organized into two directories `app` with the application and `tests` for the tests of the application.

The application uses `pipenv` to manage dependencies as a better alternative to a `requirements.txt` file when developing applications.

### The service

The service provides an HTTP API using the `quart` framework. It is like `flask` but using asyncio.

Since there is only one endpoint some things might seem overengineered a bit:

* There is a `numbers_api` module assuming that a client for the real API providing the numbers would exist. It also simulates a delay of one second.
* The endpoint is in a blueprint (even if it is only one), to show a way to organize different endpoint groups in their own files.
* The app object creation has its own file, even if it is only two lines.

#### The sum

Even if the service uses asyncio, the sum of a large number of elements as the one given in the example can take around `100ms`. During that CPU bound task, the server won't be able to respond unless there is more than one worker.

Taking the CPU bound task into an external process using a [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor) and `loop.run_in_executor` adds around `2 seconds`. So I chose to let it run in the event loop.


### Tests

There is code to test, although not much. The service has two kind of tests:

* Integration (`test_integration.py`): Test the entire application as a black box.
* Unit (`test_total.py`): There are unit tests only for the total module.

### Deploy

The app is deployed into Bluemix Cloud Foundry (IBM Cloud) as a container using travis-ci.

Since I'm using the free tier, I reduced the amount of numbers generated (removed one zero from the number), not to hit memory limits.

### Missing

There are some things that didn't make it into the assignment due to time constraints.

* Telemetry, so we can monitor if the app performance and if it is working. Here using a 3rd party library would be really useful to get timers and histograms easily. For `quart` we could use this helper: https://github.com/claws/aioprometheus
* [API Blueprint](https://apiblueprint.org) of the endpoint.