# backend-collection-python-1

### Version: release-1.0 (2023-01-08)

### Summary:
This is Python backend number 1 from my backend collection project. This backend is a REST API for CRUD post data build with FastAPI framework, PostgreSQL, and Alembic/SQLAlchemy ORM, also tested with Starlette framework built-in FastAPI.

### Requirements:
1. python (tested: v3.11.0)
2. postgresql (tested: v13.8)

### Steps to run the backend server:
1. install all requirements
2. clone repository with command `git clone https://github.com/reyhanfikridz/backend-collection-python-1` at directory `$GOPATH/src/github.com/reyhanfikridz/`
3. at repository root directory, which is `$GOPATH/src/github.com/reyhanfikridz/backend-collection-python-1`:
    1. switch to branch release-1.0 with command `git checkout release-1.0`
    2. create python virtual environment with command `python -m venv pyenv`
    3. use virtual environment with command `source pyenv/Scripts/activate` for windows, command `source pyenv/bin/activate` for linux
    4. download and install required python modules to the virtual environment with command `pip install -r required_modules.txt`
    5. create .env file with contents:
        ```
        DB_URI="postgresql://<dbuser>:<dbpassword>@<dbhost>/<dbname>"
        DB_TEST_URI="postgresql://<dbuser>:<dbpassword>@<dbhost>/<dbtestname>"

        APP_HOST="<app_host>"
        APP_PORT=<app_port>

        PROJECT_ENV="<dev or production or test>"
        ```

        Example of .env file:
        ```
        DB_URI="postgresql://postgres:somepassword@localhost/backend_collection_python_1"
        DB_TEST_URI="postgresql://postgres:somepassword@localhost/backend_collection_python_1_test"
        
        APP_HOST="127.0.0.1"
        APP_PORT=8000

        PROJECT_ENV="dev"
        ```

    6. create pytest.ini file with contents:
        ```
        [pytest]
        ; custom env for testing
        env =
            DB_TEST_URI=postgresql://<dbuser>:<dbpassword>@<dbhost>/<dbtestname>
            APP_HOST=<app_host>
            APP_PORT=<app_port>
            PROJECT_ENV=test

        ;filter deprecation warning for now
        filterwarnings =
            ignore::DeprecationWarning
        ```

        Example of pytest.ini file:
        ```
        [pytest]
        ; custom env for testing
        env =
            DB_TEST_URI=postgresql://postgres:somepassword@localhost/backend_collection_python_1_test
            APP_HOST=127.0.0.1
            APP_PORT=8000
            PROJECT_ENV=test

        ;filter deprecation warning for now
        filterwarnings =
            ignore::DeprecationWarning
        ```

    7. create postgresql database and testing database with name same as in .env file
    8. migrate database and testing database tables first with command `python migrate.py`
    9. test server first with command `pytest`
    10. run server with command `python main.py`

### API collection:
1. Go to https://www.postman.com/reyhanfikri/workspace/backend-collection-python-1/overview
2. Choose `release-1.0` collection

### License:
This project is MIT license, so basically you can use it for personal or commercial use as long as the original LICENSE.md included in your project.
