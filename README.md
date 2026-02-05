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
