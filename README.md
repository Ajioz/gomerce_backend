# Gomerce Backend Service

This is the backend for and open source ALX-T Udacity full-stack developer graduate project.
It is the backend API for a B2C e-commerce web application

# Collaboration

Our Pledge
In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

We appreciate your time and effort made to support this project and so we have set out some guidelines to make this community effort worthwhile.

Informations on how best to contribute to this initiative can be found at the [CONTRIBUTING.md](./CONTRIBUTING.md)

# Requirements

```
Python 3.9 or higher
PostgreSQL 13.* or higher - recommended
```

# Setup

## Virtual environment

How to setup a python virtual environment

- Create the virtual environment, `python -m venv .venv`
- Activate the virtual environment
  - for windows `.venv\Scripts\activate`
  - for Linux / macOS `source .venv/bin/activate`
- Deactivate the virtual environment when you need to, `deactivate`

## Install requirements

For local development
`pip install -r requirements.txt`
For production
`pip install -r requirements-prod.txt`

## Set environment variables

Make a copy of the `example.env` file, and rename it to `.env`

Update the values of the variables in the `.env` file to suite your system environment.

## Datebase setup

### Create databases

Create a Postgres database with the name matching what you have on the `.env` file for `DB_NAME` and `TEST_DB_NAME`. For example:

```
createdb gomerce
createdb gomerce-test
```

### Create database tables from migrations
