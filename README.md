# jobSearchIK

This is an automation framework with a job service running which takes filter selected by student as input and returns the list of jobs selected. The job's selected is a union of all the filters to make it more selective. The logic can be changed to intersection as well.
The automation suite works on top of that. It includes unit tests, contract tests and functional tests in TDD format.
It is also integrated with CI and tests run on any commit to main branch
Ci link: https://app.circleci.com/pipelines/github/bhuvanwy/jobSearchIK/

# dependencies: 
- pytest~=6.2.3
- virtualenv
- flask
- requests~=2.25.1
- jsonschema~=3.2.0

# Steps: 
- Install from requirements.txt
- run flask app using flask run
- run oytest for the tests

# Structure

## data
It contains any redundant data that can be shared across classes like base url for service. This also includes pre seeded data for running the suite.

## utility
It has all the utilities like building requests, geting json from file.

## helper
It has pages corresponding to each endpoint in a service

## tests
It has tests that consumes from helper and run using pytest

