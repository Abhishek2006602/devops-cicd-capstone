# Flask CI/CD Capstone Service

A small Flask microservice built to demonstrate a complete CI/CD pipeline: GitHub Actions for automated lint/test, Tekton tasks for pipeline-based build/test, and deployment to an OpenShift cluster.

## Features

- Simple Flask web service (`app.py`) listening on port 8000
- Automated linting with flake8
- Automated unit testing with nose
- Tekton pipeline tasks for cleanup and testing (`.tekton/tasks.yml`)
- GitHub Actions workflow that lints and tests on every push (`.github/workflows/workflow.yml`)

## Getting started

```bash
pip install -r requirements.txt
python app.py
```

The service starts on `http://0.0.0.0:8000` and logs `SERVICERUNNING` once it's up.

## Running tests locally

```bash
pip install -r requirements_test.txt
flake8 .
nosetests tests/
```
