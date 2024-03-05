# CodeLeap Backend CRUD application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/lukasleonardo/codeleap-backend.git
$ cd codeleap-backend
```

```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/careers`. In order to test GET and Post Endpoints

In order to test Patch and Delete endpoints use the following URL,
`http://127.0.0.1:8000/api/careers/:id/` 

## Tests
To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test