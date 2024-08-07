## GETTING STARTED

### DJANGO AT A GLANCE

#### DESIGN YOUR MODEL

- Django ORM:
  - ORMs map classes to database tables, objects to rows in the table, and 
    properties of the object to columns in the table
  - ORMs translate the developers' interaction with database into equivalent 
    SQL queries for CRUD (create, read, update, delete) operations
  - ORMs provide a layer of abstraction from the database system used, which 
    makes interacting with them and switching between different systems easier
```python
# mysite/news/models.py

from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=90)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```

#### INSTALL IT

- Run the command line utilities to create the database tables automatically:
```bash
python manage.py makemigrations
python manage.py migrate 
```
- `makemigrations` looks at all your available models and creates migrations 
  for whichever tables don't already exist
- `migrate` runs the migrations and creates tables in your database

#### ENJOY THE FREE API

- To access your data use the Python API
```bash
from news.models import Article, Reporter

# Get all reporters in the database
Reporter.objects.all()                              # <QuerySet []> 

# Create a new Reporter
r = Reporter(full_name = "John Smith")  
# Save the object into the database
r.save()                                
# Saving an objects grants it an ID
r.id                                                # 1             

Reporter.objects.all()                              # <QuerySet [<Reporter: John Smith>]>

# Fields are represented as attributes on the Python object
r.full_name                                         # "John Smith"  

# Django's lookup API
Reporter.objects.get(id=1)                          # <Reporter: John Smith>
Reporter.objects.get(full_name__startswith="John")  # <Reporter: John Smith>
Reporter.objects.get(full_name__contains="mith")    # <Reporter: John Smith>
Reporter.object.get(id=2)                           # invalid - DoesNotExist

# Create an Article
from datetime import date
a = Article(pub_date = date.today(), headline = "Django is cool", content = 
"Yeah", reporter = r)
a.save()

Article.objects.all()                               # <QuerySet [<Article: Django is cool>]>

# Article objects gets API access to related Reporter objects
r = a.reporter
r.full_name                                         # "John Smith"

# And vice-versa
r.article_set.all()                                 # <QuerySet [<Article: Django is cool>]>

# The API follows relationships as far as you need, performing efficient JOINS
# Find all articles by a reporter whose name starts with "John"
Article.objects.filter(reporter__full_name__startswith="John")  # <QuerySet [<Article: Django is cool>]>

# Change an attribute by altering its attributes and calling save()
r.full_name = "Billy Goat"
r.save()

# Delete an object with delete()
r.delete()
```

#### A DYNAMIC ADMIN INTERFACE

- Once models are created Django can create an administrative website that 
  lets authenticated users add, change, and delete objects. The only step 
  required is to register your model in the admin site
- WORKFLOW - Creating Django apps to create models and get the admin sites 
  up and running so that clients can start populating data. Then, develop 
  the way data is presented to the public
```python
# mysite/news/admin.py
from django.contrib import admin
from . import models

admin.site.register(models.Article)
```

#### DESIGN YOUR URLs

- Create `URLconf` Python module for mapping URL pattern to views (Python 
  callback functions). This helps decouple URLs from Python code
```python
# mysite/news/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<int:pk>/", views.article_detail),
]
```
- The path strings use parameter tags to capture values from the URLs. When a 
  user requests a page, Django runs through each path, in order, and stops 
  at the first one that matches the requested URL (if none of them matches, 
  Django calls a special-case 404 view)
- The paths are compiled into regular expressions at load time, so this is fast
- Once one of the URL patterns matches, Django calls the given view, which 
  is a Python function. Each view gets passed a request object - which 
  contains request metadata and the values captured in the pattern

#### WRITE YOUR VIEWS

- Each view is responsible for either returning an `HttpResponse` object 
  containing the content for the requested page, or raising an exception 
  such as `Http404`. It retrieves data according to the parameters, loads  
  template and renders the template with the retrieved data:
```python
# mysite/news/views.py

from django.shortcuts import render
from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    content = {"year":year, "article_list": a_list}
    return render(request, "news/year_archive.html", context)
```

#### DESIGN YOUR TEMPLATES

- In your Django settings you can specify a list of directories to check for 
  templates with `DIRS`. This allows to reduce redundancy among templates
```html
<!--mysite/news/templates/news/year_archive.html-->
{% extends "base.html" %}
{% block title %}Articles for {{ year }}{% endblock title %}

{% block content %}
    <h1>Articles for {{ year }}</h1>

    {% for article in articles_list %}
        <p>{{ article.headline }}</p>
        <p>By {{ article.reporter.full_name }}</p>
        <p>Publised {{ article.pub_date|date:"F j, Y" }}</p>
    {% endfor %}
{% endblock content %}
```
- `{{ article.headline }}` means output the value of article's headline 
  attribute
- `{{ article.pub_date|date:"F j, Y" }}` is called a template filter using a 
  pipe character (`|`). Chaining these can be taken to any level
- You can write custom template filters and custom template tags which run 
  custom Python code behind the scenes
- `{% extends "base.html" %}` uses the concept of template inheritance. It 
  means "First load the template called base, which has defined a bunch of 
  blocks, and fill the blocks with the following blocks". This reduces 
  redundancy as each template has to define only what's unique to that template
  - The base template defines the look-and-feel of the site and provides 
    holes for child templates to fill. This means that a site redesign can 
    be done by changing a single file - the base template
- You are free to not use Django's templating system, or Django's database 
  API, or simply read files off disk. Each piece of Django - models, views, 
  and templates, is decoupled from the next
```html
<!-- mysite/templates/base.html -->
{% load static %}
<html>
<head>
    <title>{% block title %}{% endblock title %}</title>
</head>
<body>
    <img src="{% static 'images/sitelogo.png' %}" alt="Logo" />
    {% block content %}{% endblock content %}
</body>
</html>
```

### QUICK INSTALL GUIDE

#### INSTALL PYTHON

- Install a Python version with a supported Django version
- Python includes a database called SQLite so no need to set up a database

#### SET UP A DATABASE

- Only if you would like to work with a large database

#### INSTALL DJANGO

- Official release

#### VERIFYING

- Enter a Python shell and try to import Django
```bash
# inside python shell
import django
print(django.get_version())   # 5.0 

# from bash
python -m django --version
```


### WRITING YOUR FIRST DJANGO APP PART-1

#### CREATING A PROJECT

```bash
django-admin startproject mysite
```

- This will create the following directory structure
[Directory Structure](./images/Screenshot%202024-08-06%20225004.png)
- The outer `mysite` root directory is a container for your project
- `manage.py` - Command line utility for interacting with project
- The inner `mysite/` directory is the actual Project package for your 
  project. Its name is the Python package name you'll need to use to import 
  anything inside it (`mysite.urls`)
- `mysite/__init__.py` - An empty file that tells Python that this directory 
  should be considered as a Python package
- `mysite/settings.py` - Settings/configuration for this Django project
- `mysite/urls.py` - The URL declarations for this Django project
- `mysite/asgi.py` - An entry point for ASGI-compatible web server to serve 
  your project
- `mysite/wsgi.py` - An entry point for WSGI-compatible web server to serve 
  your project

#### THE DEVELOPMENT SERVER

- Change into the `mysite` directory and run `python manage.py runserver`
- Django comes with a lightweight web server for development purposes 
  without having to deal with configuring a production server (such as Apache)

#### CREATING THE POLLS APP

- An app is a web application that does something. For e.g., a blog system. 
  A project is a collection of configuration and apps for a particular 
  website. A project can contain multiple apps. An app can be in multiple 
  projects
- The apps can live anywhere in Python path. But putting them in the same 
  directory as `manage.py` file allows us to import it as own top-level 
  module
- To create your app type - `python manage.py startapp polls`
[App Directory Structure](./images/django_app.png)

#### WRITE YOUR FIRST VIEW

- To access a view via the browser we need to map it to a URL - and for this 
  we need to define a URL configuration inside each app with a file named 
  `urls.py`
```python
# polls/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index")

# polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

- Next we need to configure the global URLconf in the `mysite` project to 
  include the URLconf in `polls.urls`. The `include()` function allows 
  referencing other URLconfs. Django chops off whatever part of URL matched 
  upto that point and sends the remaining string to the included URLconf for 
  further processing
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

- `path()` takes 4 arguments
  - `route` - mandatory; it is a string that contains a URL pattern. Django 
    starts at the first pattern in `urlpatterns` and makes it way down the 
    list comparing the requested URL against each pattern until it finds one 
    that matches. Patterns don't search GET and POST parameters or the 
    domain name (`https://www.example.com/myapp/?page=3`, the URLconf will 
    look for `myapp/`)
  - `view` - mandatory; When Django finds a matching pattern it calls the 
    specified view function with an `HttpRequest` object as the first 
    parameter, and any captured values from the route as keyword arguments
  - `kwargs` - optional; Arbitrary keyword arguments can be passed in a 
    dictionary to the target view
  - `name` - optional; Naming your URL lets you refer to it from anywhere in 
    Django (such as templates). This allows us to make global changes to URL 
    patterns of your project while only touching a single file (by just 
    renaming a different pattern with the same name)

## 