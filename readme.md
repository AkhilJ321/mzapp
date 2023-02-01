# M-ZAP
M-Zap is a mosquito-borne disease eradication system.It leverages the power of AI and deep learning and built using microsoft azure services.


### Setup For Dev Environment

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ADITYA97-CODER/mzapp
$ cd mzapp
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




## Authors

* **Aditya Kumar** - *Initial work* - [ADITYA97-CODER](https://github.com/ADITYA97-CODER)

See also the list of [contributors](https://github.com/ADITYA97-CODER/mzapp/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ADITYA97-CODER/mzapp/blob/master/LICENSE) file for details.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


