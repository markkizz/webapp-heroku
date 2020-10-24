# Python Webapp Demo

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```bash
$ git clone https://github.com/markkizz/webapp-heroku.git
$ cd webapp-heroku

$ python3 -m venv webapp-heroku
$ pip install -r requirements.txt

$ gunicorn --config gunicorn-cfg.py run:app
or
$ export FLASK_APP=run.py
$ flask run
$ heroku local
```

Your app should now be running on [localhost:5005](http://localhost:5005/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)