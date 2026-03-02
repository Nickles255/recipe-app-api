# recipe-app-api
Recipe API project
## 
- clin@ccsf.edu - citycollege - b2090df6c8eb17248384340c93417d354edde2e8
- nickles255@gmail.com testuser123
- user2@example.com - password - 95dd5fccd6d1e0885e8bcdd987d0671afb20d2b2
{
  "title": "Cream",
  "time_minutes": 4,
  "price": "2.99",
  "link": "missing",
  "tags": [
    {
      "name": "dessert"
    }
  ],
  "ingredients": [
    {
      "name": "cream"
    }
  ],
  "description": "whipped cream"
}

{
  "title": "Soup",
  "time_minutes": 30,
  "price": "2.99",
  "link": "missing",
  "tags": [
    {
      "name": "appetizer"
    }
  ],
  "ingredients": [
    {
      "name": "tomatoes"
    },

    {
      "name": "onions"
    }
  ],
  "description": "warm soup for cold days"
}
## use flake8 package
### NOTE: update to docker-compose.yml should execute below
```shl
docker-compose down -v
docker-compose up --build
```
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "black"
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
  - response json forma
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

### USER API creation
* user/create
```shl
docker-compose run --rm app sh -c "python manage.py startapp user" 
```
* testing public and private endpoints

## User Authentication
* Basic - send username and password with each request (client stores username and password)
* Token - send token with each request **USE**
* JWT (JSON Web Token) - refresh token 
* Session - use cookies to store user info

* Token [token]

### Recipe API design
- /recipes/
  - GET - list all recipes
  - POST - create recipe
- /recipes/<recipe_id>
  - GET - view details of recipe
  - PUT/PATCH - Update recipe
  - DELETE - delete recipe in system
* user/create
```shl
docker-compose run --rm app sh -c "python manage.py makemigrations" 
docker-compose run --rm app sh -c "python manage.py startapp recipe"
```

```shl
docker-compose up
```

## Create TAG
- add tags API
  - /api/recipe/tags
    - POST - create tag
    - PUT/PATCH - Update tags
    - DELETE - Remove tag
    - GET - list available tags
  
### Steps
- create tag test
- in core 
  - models.py - create class Tag
  - admin.py - register Tag
  - docker-compose run --rm app sh -c "python manage.py makemigrations" 
- docker-compose run --rm app sh -c "python manage.py startapp tags"
- in recipe
  - create tags_api test 
  - searializers.py - add tag serializer
  - views.py create TagViewSet
  - urls.py - register router
  - create recipe_api test
- final testing and flake8 check
  - docker-compose run --rm app sh -c "black . --exclude migrations"
  - docker-compose run --rm app sh -c "flake8"
  - docker-compose run --rm app sh -c "python manage.py test"

## Nexted serializers
- serializer within serializer
- read only in rested serializer
- custom logic to make writable

## Ingredients Model
- name - of ingredient
- user - user who owns ingredients
- end point
  - api/recipe/ingredients/
    - GET - List ingredients
  - api/recipe/ingredients/<id>
    - GET - View ingredient details
    - PUT/PATCH - Update ingredient
    - DELETE - Delete ingredient 
  - /api/recipe/
    - POST - create ingredients part of recipe
  - /api/recipe/<id>/
    - PUT/PATCH - create or update recipe ingredients 

## Image Model
- image - image of recipe
- user - user who owns image
- end point 
  - api/recipe/<id>/upload-images/
    - POST - Upload image  
  - api/recipe/images/
    - GET - List images
  - api/recipe/images/<id>
    - GET - View image details
    - PUT/PATCH - Update image
    - DELETE - Delete image 
### Images
- Configuration - in settings.py
  - STATIC_URL - /static/static/ -- static files base URL
  - MEDIA_URL - /static/media/ -- media files base URL
  - MEDIA_ROOT - /vol/web/media/ -- where media files are stored in file system
  - STATIC_ROOT - /vol/web/static/ -- where static files are stored in file system
-require using multipart/form-data - options
  - "http://localhost:8000/static/media/uploads/recipe/f5c59a49-ccc9-4245-91d1-5472ddccc6aa.png
### Docker Volume - storing persistent data
- /vol/web - store

## gathering static files
- python manage.py collectstatic

## Dockerfile change - rebuild
docker-compose build --no-cache app

## Database remains - remove
docker-compose down -v
docker-compose up --build
docker-compose run --rm app sh -c "python manage.py migrate"
