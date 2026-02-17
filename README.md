# recipe-app-api
Recipe API project

## use flake8 package
### NOTE: update to docker-compose.yml should execute below
```shl
docker-compose down -v
docker-compose up --build
```
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "python manage.py test"

## create django project
docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose up

## GITHUB ACTIONS
* for code linting and unit test in this class
* Triggers push to github 
* charged per minutes 2,000 free minutes


## TESTING DJANGO framework
* Based on the unittest library

### Mocking
* speed up test or prevent email to end user


## Create Databased
* race condition setting up database
```shl
docker-compose run --rm app sh -c "python manage.py startapp core" 
```

## TESTING

docker-compose run --rm app sh -c "python manage.py test"
docker-compose run --rm app sh -c "python manage.py wait_for_db"
docker-compose run --rm app sh -c "python manage.py test & flake8"

## ADMIN
### Creating Model to manage users
* create custom model for new projects - to not use default user model
    * AbstractBaseUser -- BaseUserMethod
    * PermissionsMixin
* do clear migration then setup user model

#### migrate User model 
docker-compose run --rm app sh -c "python manage.py makemigrations"
#### migrate model into volume -- need to make sure volume isn't created already
docker volume ls
docker compose down
docker volume rm recipe-app-api_dev-db-data
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

#### Start up for testing
* docker compose up

goto localhost:8000/admin
in terminal create superupser to login
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py createsuperuser"
clin@ccsf.edu - citycollege

### ADMIN OVERIVEW
* admin - create admin.py
    * for each model add admin.site.register (Recipe)
- https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#reversing-admin-urls

### API Documentation
#### Things to document
- available end points
- supported methods: GET, POST, PUT, PATCH, DELETE
- Format fo payloads
  - parm
  - post JSON format
- format of responses
  - response json format
- authentication process
#### Automated - API documentation
- doc strings
- add documentation for API
- use library drf-spectacular -
  - add to requirements.txt
  - docker compose build
  - setup in settings.py -- 
- https://drf-spectacular.readthedocs.io/en/latest/index.html
- swagger documentation too