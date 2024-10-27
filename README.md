<h3 align="center">School Management Application API</h3>

<div align="center">

  ![Status](https://img.shields.io/badge/status-active-success.svg)
  ![GitHub issues](https://img.shields.io/github/issues/TMCreme/salcon-school-app?color=yellow)
  ![GitHub pull requests](https://img.shields.io/github/issues-pr/TMCreme/salcon-school-app?color=success)
  [![License](https://img.shields.io/badge/license-Proprietary-blue.svg)](/LICENSE)


</div>

---

<p align="center"> Backend API for Salcon School Application
    <br> 
</p>

## 📝 Table of Contents
- [TODO](#todo)
- [About](#about)
- [Getting Started](#getting_started)
- [Running the tests](#tests)
- [Project Structure](#structure)
- [Contributing](#contributing)
- [Usage](#usage)
- [Built Using](#built_using)
- [Team](#team)

## Todo <a name = "todo"></a>
See [TODO](./docs/TODO.md)

## About <a name = "about"></a>
This is a school management application for managing student data, library access and controls, financials, etc

## 🏁 Getting Started <a name = "getting_started"></a>
These are the instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites
- PIP: Dependency manager for Python.
- Postgres: A relational database.
- Python 3.12^: The Python programming language.
- Flake8: An auto-formatter for Python code.


### Setting up a development environment
### Step 1: Clone the repository

```bash
https://github.com/TMCreme/salcon-school-app.git
```

or with GithubCLI
  
```bash
gh repo clone TMCreme/salcon-school-app
```

### step 2: Create a virtual environment

```bash
virtualenv schoolenv
```
OR by using the virtualenvwrapper
```bash
  mkvirtualenv schoolenv
```
Activate the virtual environment with 
```bash
  source schoolenv/bin/activate
```

#### Step 3: Install dependencies

```
pip install -r requirements.txt
```

> Note to add a package to the project, run

```bash
pip install <package-name>
```

#### Step 4: Create a `.env` file in the project's root directory and add the following environment variables, replacing the placeholders with your specific values:

```bash
POSTGRES_USER=<pg_user>
POSTGRES_PASSWORD=<pg_pass>
POSTGRES_SERVER=<pg_server>
POSTGRES_PORT=<pg_port OR 5432>
POSTGRES_DB=<pg_db_name>
POSTGRES_TEST_DB=
DATABASE_URL=
SECRET=
REFRESH_SECRET=
PRODUCTION_ENV=
REFRESH_TOKEN_EXPIRE_MINUTES=
ACCESS_TOKEN_EXPIRE_MINUTES=
ALGORITHM=
BASE_URL=
EMAIL_SERVER=
EMAIL_PORT=
EMAIL_SENDER=
EMAIL_PASSWORD=
URL_PATH=/users/reset-password/new-password
```

#### Step 5: Create a `test.env` file in the root directory and add the following environment variables

```bash
POSTGRES_USER= #e.g postgres
POSTGRES_PASSWORD= #e.g password123
POSTGRES_SERVER= #e.g localhost
POSTGRES_PORT= #e.g 5432
POSTGRES_DB= #e.g pg_db_name
```

#### Step 6: Start the uvicorn server

```bash
uvicorn app:app --reload
```

### Step 7: Interact with the Database
To interact with the database, you can use tools like psql, pgAdmin or any database client that supports PostgreSQL. Here are some basic commands:

- Connect to the database:

```bash
psql -U postgres -d <pg_db_name>
```

- List all tables:

```bash
\d
```

- Execute SQL queries:

```bash
SELECT * FROM table_name;
```


## 🔧 Running the tests <a name = "tests"></a>
To ensure the code is functioning correctly, you can run tests by executing the following command:

```bash
pytest
```

> Make sure your `test.env` file is correctly configured with test-specific environment variables.

## Running the project in Docker-Compose
* Clone the project and from the main, create your feature branch if you are about to make changes. Else stay on the main branch
* From the `.env.sample` create a `.env` file with the correct credentials
* Ensure you have docker and docker compose installed on your local system
* To build the docker image use
```bash
  docker-compose build
```
* To start the services
```bash
  doker-compose up
```
* A combination of build and start command is 
```bash
  docker-compose up --build
```
* To run tests 
```bash
  docker-compose run --rm app sh -c "python -m pytest test"
```
## ⚙️ Project Structure <a name = "structure"></a>
```s
│   app.py
│   Dockerfile
│   README.md
│   test_app.py
│   __init__.py
│
├───.github
│   └───workflows
│           build.yml
│           deploy.yml
│
├───Alembic
│   │   env.py
│   │   README
│   │   script.py.mako
│
├───api
│   │   __init__.py
│   │
│   ├───api_models
│   │   │   user.py
│   │
│   ├───routes
│   │   │   auth.py
│   │   │   profile_page.py
│   │   │   __init__.py
│
├───core
│   │   config.py
│   │   exceptions.py
│
├───db
│   │   database.py
│   │   __init__.py
│   ├───models
│   │    users.py
│   └───repository
│        users.py
├───docs
│       TODO.md
│
├───test
│   │   conftest.py
│   │   test_auth.py
│   │   test_profile_page.py
│   │   test_users.py
│   │   utils_test.py
│   │   __init__.py
│
└───utils
    │   oauth2.py
    │   permissions.py
    │   utils.py
    │   __init__.py


```

## ✏️ Contributing <a name = "contributing"></a>
This is a private project hence reach out to any of the contributors for your contributions

### Coding Standards
- Follow the PEP 8 coding style for Python.
- Ensure your code is well-documented with clear comments and docstrings.
- Use meaningful variable and function names.

### Branch Naming Conventions
**Create a new branch for your feature or bug fix using the format below.**
```bash
git checkout -b <initials/issue_no/feature> eg. # RG/121/Fixed-login-page
```

### Pull Requests
- Commit your changes to your branch with a clear and descriptive commit message:
```bash
git add .
git commit -m "Made this in this file"
```
- Push your branch to the repository on GitHub:
```bash
git push -u origin <name-of-branch>
```
- Open a pull request in the original repository, providing a detailed description of your changes and any relevant information.

> please try building the project on your local machine to confirm everything works before pushing...Thanks

## 🎈 Usage <a name="usage"></a>
API documentation will be available online soon


## ⛏️ Built Using <a name = "built_using"></a>
- [FastAPI](https://fastapi.tiangolo.com/) - Python Framework
- [Postgres](https://www.postgresql.org/) - Database
- [Docker](https://www.docker.com/) - Containerization
- [SqlAlchemy](https://www.sqlalchemy.org/) - ORM
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) - Database Migration
- [Pytest](https://docs.pytest.org/en/6.2.x/) - Testing Framework

## ✍️ Team <a name = "team"></a>
- [@Tonny-Bright](https://github.com/TMCreme)