[![Run tests](https://github.com/MaastrichtU-IDS/python-template/workflows/Run%20tests/badge.svg)](https://github.com/MaastrichtU-IDS/python-template/actions?query=workflow%3A%22Run+tests%22)

## Tidal Connector

## Prerequisites

* Python 3.6 or higher, with [pip](https://pip.pypa.io/en/stable/)
* Docker (optional)

## Installation

## Usage

## Test and Publish

### Continuous Integration

This repository uses [GitHub Actions](/actions) to:

* Automatically run tests at each push to the `master` branch
* Publish the package to [PyPI](https://pypi.org) when a release is created (N.B.: the version of the package needs to be increased in [setup.py](/blob/master/setup.py#L6) before).

> You will need to provide your login credentials using [secrets in the repository settings](/settings/secrets) to publish to [PyPI](https://pypi.org): `PYPI_USERNAME` and `PYPI_PASSWORD`

### Test locally

## Docker 🐳

Checkout the `Dockerfile` to see how the image is built, and run it with the `docker-compose.yml`:

```bash
docker-compose up -d --build
```

Or build and run with docker:

```bash
docker build -t rdflib-endpoint .
```

Run on http://localhost:8080

```bash
docker run -p 8080:80 rdflib-endpoint
```
