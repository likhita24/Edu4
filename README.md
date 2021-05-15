# Edu4
Edu4 is a free-learning website providing courses of 4 streams on a single platform. It helps those people to learn just by signing in and providing free online courses. It also provides scholarship to the students who can excel in studies but can’t do because of lack of money.

Website : https://edu4.herokuapp.com

###Installation or SetUp of the project

- Python 3.7.7 runtime
- Django 3.2.0
- Other dependencies in `requirements.txt`

Procedure:

- Install [python](https://www.python.org/downloads/) in your environment(pre-installed on Ubuntu).
- Navigate to the cloned repository.
    ```
    cd <project_directory_name>     # edu4
    ```
- Create a virtual environment
    ```
    mkvirtualenv <virtual_env_name>   #windows
    ```
    To activate the virtual environment in deactivated state
    ```
    workon <virtual_env_name>   #windows
    ```
- Use pip to install other dependencies from `requirements.txt`
    ```
    pip install -r requirements.txt
    ```

- Make database migrations
    ``` 
    python manage.py makemigrations
    python manage.py migrate
    ```
    NOTE: If its your first time migrating, you may need to manually add migration module in each app.
    ```
    python manage.py makemigrations main
    python manage.py makemigrations authentication
    python manage.py migrate
    ```
- Create a superuser
    ```
    python manage.py createsuperuser 
    ```
- Run development server on localhost
    ```
    python manage.py runserver 
    ```

