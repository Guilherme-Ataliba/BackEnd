This chapter will be dedicated on how to work with apps

# 🔵 Views
Inside every app there's a file `views.py`. This file controls all the visualization promoted by that app, so how and what to display on screen, etc.

Views work by answering HTTP requests. Thus, to show something / control what is shown or will be, you must catch and answer a HTTP request.

## 🔷 Starting and Organization
To start a web page you'll need the `HttpReponse` method
```python 
from django.http import HttpResponse
```

As industry standard, just as you have multiple html files for different pages, you should **create a different function for every different page** in django. 

### 🔹 Linking Requisitions
Once you've created a function representing an html file you must link that function to an URL pattern. This means that, for some HTTP request that happens in this page, call this function.

#### 🟢 First Code
A "hello world", so to speak, page could be create by setting the `views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse
  
def index(request):
    return HttpResponse("<h1>Alura Space</h1>")
```

And then adding this function to the `urlpatterns` inside `urls.py` from the project dir.
```python
from django.contrib import admin
from django.urls import path
from galeria.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),  # When the main page gets a request call the function index
]
```

And to `INSTALLED_APPS` by referencing the file `apps.py` created by django:
```python
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "galeria.apps.GaleriaConfig",
]
```

### 🔹 Structuring Requisitions
As standard, it is not good to import every web page in the `urlpatterns` from the main project. Every page should have it's own `urls.py` file that controls its own requisitions and connections. 

To do it
1. Create an `urls.py` file in your app
2. Add the function to a path as you would
```python
from django.urls import path
from galeria.views import index

urlpatterns = [
    path("", index),  # When the main page gets a request call the function index
]
```
3. Import this `url` file to the project's main `url` file
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("galeria.urls"))
]
```

## 🔷 HTML Page - Templates
Django uses the concept of **templates** as a way to store html files.

### 🔹 Setup
To setup a template you must add the directory in which you'll store the different pages to the `DIRS` list inside the `TEMPLATES` variable in `settings.py` using `path.join` like so
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],   # <-----
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

### 🔹 Loading Templates
Once your directory is correctly setup, you can use the render method to render html pages inside the function we've talked previously. So, your `views.py` should look something like this

```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "galeria/index.html")
```
- Notice that there is a directory before the file name. This is industry standard, every html page should be in a directory with the application's name

## 🔷 Static Files
In a web project, static files usually refer to assets and styles (CSS files). To be able to work with static files as you please, you must first set it up in `settings.py` following some steps

1. Create a directory `static` inside `setup`
2. In `settings.py` add the following code bellow STATIC_URL which should already be there.
```python
STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "setup/static")
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
```
3. Put your static files inside `setup/static` following the pattern `assets/` and `styles/`
4. Run the following command so that django can link all static files to the page
```python
python manage.py collectstatic
```

In every html file that utilizes static files you must add the following line of code, so that django knows that it must manipulate that file:
```python
{% load static %} # <-------
<!DOCTYPE html>
...
```

### 🔹 Embedding
Embedding is a django feature that allows you to use python code inside an html file. The pattern for embedding is
```python
{% --python code-- %}
```
Everything that's inside that structure will be manipulated as python code.

To link css files to the html page you must add the following embedding to the `href` property of link:
```python
<link rel="stylesheet" href="{% static '/styles/style.css' %}">
```


## 🔷 Navigation
Navigation between different html files will also not work by default, since the html file sends a request to a different page than the one we set using django.

To fix this, you'll need to add a name to `path` you've have set in `urls.py`. This way you can reference it inside the html file.

1. Add name to `urls.py`
```python 
from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path("", index, name="index"),
    path("imagem/", imagem, name="imagem")
]
```
2. Change every link from `page.html` to `{% url 'page' %}`, where `page` is the name you've given. Example:

```python
<a href="{% url 'imagem' %}">
```