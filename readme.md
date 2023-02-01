# TradeAndCode

### Setup For Dev Environment

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Teamexe/TradeAndCode
$ cd TradeAndCode
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages venv
$ source venv/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt    # Install all requirements
(env)$ python manage.py makemigrations    # Make Database Migrations
(env)$ python manage.py migrate           # Migrate Changes
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py runserver
```
Voila app is up and running.
