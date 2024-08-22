
# 🔵 Initial Setup
To start a Django server you must install django via `pip`, and then run the following commands:

1. Create a django project
```python
django-admin startproject setup .
```

2. Start a Django serve
```python
python manage.py runserver
```
- The URL for the website will be shown at the command line


## 🔷 Initial Settings
Django has created a `settings.py` file that controls the settings for the whole application. 
- If you want to change something take will have global effect you must add it to `settings.py`

Some initial setups can be done here:
1. `LANGUAGE_CODE`: pt-br.
2. `TIME_ZONE`: America/Sao_Paulo

## 🔷 Common Practices
Django has a secret key for administrator access, and this secret key should not be uploaded to any remote repository. To solve this problem we'll the python package `python-dotenv`.

With this library we can create environment variables in a separate file and then access those variables using `os` inside the `settings.py`. Then, it's just a matter of setting up the `.gitignore`.


1. Install `python-dotenv`
2. Create a `.env` file and add the secret key like so:
```python
SECRET_KEY = django-insecure-%$8pbyin7fpj9ob04xn8f$ty(pqn%ijxf=9&x5l-8u$0je$pzl
```
3. Add the missing lines in you `settings.py`
```python
from pathlib import Path, os
from dotenv import load_dotenv

load_dotenv()

  
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

  
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv("SECRET_KEY"))
```


# 🔵 Apps and Projects
A Django project is your web application, it with all of it's functionalities is called an application. 

Now, a django application is composed of multiple **apps**, these apps are responsible for controlling specific parts of the web application. Usually a project has multiple apps.

Since you start you django project creating a project, we'll now see how to create and link new apps:

1. Create an app with
```python
python manage.py startapp --appname--
```
2. Add the app name in the project's `settings.py` under the `INSTALLED_APPS` list