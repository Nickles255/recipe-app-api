# recipe-app-api
Recipe API project

## use flake8 package
### NOTE: update to docker-compose.yml should execute below
```shl
docker-compose down
docker-compose build
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
