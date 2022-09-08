## Flask API Server

e-commerce [gomerce](https://github.com/Ajioz/gomerce_backend.git) enhanced with JWT authentication, SqlAlchemy, **SQLite** persistence and deployment scripts via Docker. It has all the ready-to-use bare minimum essentials.

<br />

> Features:

- `Up-to-date dependencies`
- [API Definition](https://docs.appseed.us/boilerplate-code/api-unified-definition) - the unified API structure implemented by this server
- Simple, intuitive codebase - can be extended with ease.
- `Flask-restX`, `Flask-jwt_extended`
- **Docker**, `Unitary tests`

## ✨ Quick Start in `Docker`

> Get the code

```bash
$ git clone https://github.com/Ajioz/gomerce_backend.git
$ cd gomerce_backend
```

> Start the app in Docker

```bash
$ docker-compose up --build
```

The API server will start using the PORT `5000`.

<br />

## ✨ Table of Contents

1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [Modules](#modules)
4. [Testing](#testing)

<br />

## ✨ How to use the code

> **Step #1** - Clone the project

```bash
$ git clone https://github.com/Ajioz/gomerce_backend.git
$ cd gomerce_backend
```

<br />

> **Step #2** - create virtual environment using python3 and activate it (keep it outside our project directory)

```bash
## Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$

##Virtualenv modules installation (Windows based systems starting from python 3)
Create a virtual environment by running "python -m venv env"
Activate the virtual environment by running: ". env/scripts/activate"
```

<br />

> **Step #3** - Install dependencies in virtual env

```bash
$ pip install -r requirements.txt <-- ### Mac users
Install the dependencies by running "pip install -r requirements.txt" <-- ### Windows users
```

<br />

> **Step #4** - setup `flask` command for our app

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

For **Windows-based** systems

```powershell
$ (Windows CMD) set FLASK_APP=run.py
$ (Windows CMD) set FLASK_ENV=development
$
$ (Powershell) $env:FLASK_APP = ".\run.py"
$ (Powershell) $env:FLASK_ENV = "development"
```

<br />

> **Step #5** - start test APIs server at `localhost:5000`

```bash
$ flask run
```

Use the API via `POSTMAN` or Swagger Dashboard.

![Flask API Server - Swagger Dashboard.](https://user-images.githubusercontent.com/51070104/141950891-ea315fca-24c2-4929-841c-38fb950a478d.png)

<br />

## ✨ Project Structure

```bash
api-server-flask/
├── api
│   ├── config.py
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── Dockerfile
├── README.md
├── requirements.txt
├── run.py
└── tests.py
```

<br />

## ✨ API

For a fast set up, use this `POSTMAN` file: attached in the root folder **api.postman_collection.json**

> **Register** - `api/users/register` (**POST** request)

```
POST api/users/register
Content-Type: application/json

{
    "username":"yourUsername",
    "password":"yourPassword",
    "email":"yourEmail"
}
```

<br />

> **Login** - `api/users/login` (**POST** request)

```
POST /api/users/login
Content-Type: application/json

{
    "password":"yourPassword",
    "email":"yourEmail"
}
```

<br />

> **Logout** - `api/users/logout` (**POST** request)

```
POST api/users/logout
Content-Type: application/json
authorization: JWT_TOKEN (returned by Login request)

{
    "token":"JWT_TOKEN"
}
```

<br />

## ✨ Testing

Run tests using `pytest tests.py`

<br />


## ✨ Contributors
> The Gomerce project won't be complete without these backend developers: <br /> 
<img src="https://img.shields.io/github/contributors/ajioz/gomerce_backend?style=plastic" alt="Contributors" /> <br />
<a href="https://github.com/Ajioz/gomerce_backend/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Ajioz/gomerce_backend" />
</a>

---
