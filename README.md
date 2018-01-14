# Open Street Map Router
[![Build Status](https://travis-ci.org/jhole89/osm-router.svg?branch=master)](https://travis-ci.org/jhole89/osm-router)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e2f1b820fcaf4d27937677fb28a8ab60)](https://www.codacy.com/app/jhole89/osm-router?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jhole89/osm-router&amp;utm_campaign=Badge_Grade)

This project is a simple example of building Dijkstra's shortest path algorithm using Open Street Map data, using only the standard Python library. The class `Graph` builds the directed graph by adding nodes and edges for each weighted edge between two nodes. The `get_shortest_path` method implements [Dikstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to find the distance of the shortest path.

## Getting Started

### Prerequisites

* [Python 3.6+](https://www.python.org/downloads/)

### Installation

1. Install Python 3.6 on your Operating System as per the Python Docs.
Continuum's Anaconda distribution is recommended.

2. Checkout the repo:
`git clone https://github.com/jhole89/osm-router`

3. Setup the project dependencies:
```
$ cd osm-router
$ export PYTHONPATH=$PYTHONPATH:$(pwd)
$ pip install -r requirements.txt
$ chmod +x run.sh
```

### Execution

A simple shell script `run.sh` has been provided to execute the program. This passes 3 arguements to the Python application
`./run.sh <path to graph> <from-osm-id> <to-osm-id>`.

#### Example
```
./run.sh citymapper-coding-test-graph.dat 316319897 316319936
121
```

## Test Coverage and Coding Style

This project uses [Travis-CI](https://travis-ci.org/jhole89/osm-router) for our CI/CD
to run style checks (pycodestyle) against every new commit and against the nightly 
CPython build to ensure we are always aligned with the latest CPython dev builds.
Build status is shown at the top of this README.

## TODO
* Test coverage - currently no unit or integration tests have been implemented, this should be rectified with a couple of simple tests using `pytest`
