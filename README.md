# Wagtail Practice

## Wagtail Installation

1. First let's make a new directory for our project:
    > mkdir Websites

2. Then to install Wagtail
    1. In our project **`only`**
        > pip install wagtail
    2. To install it on your device **`Globally`** just type the same code in your terminal in the **`Root`**

3. To start your first wagtail project
    > wagtail start mysite

    mysite here is the name of your project

4. Then cd to the project

5. Then enter the shell
    > pipenv shell

6. Then type the following code to extract your dependency to the requirements file for the docker
    > pip install -r requirements.txt

### Add New App To The Project

1. To add new app to the project
    > python manage.py startapp myapp

    Then add the app name to the **`INSTALLED_APPS`** in **`base.py`** file

------------------------------------------

## How To Run Wagtail

1. First we have to migrate
    > python manage.py migrate
2. Then we should create the superuser
    > python manage.py createsuperuser
3. Then we can run the server
    > python manage.py runserver

------------------------------------------

## Install Django Debug Toolbar & Django Shell + Ipython

### Django Debug Toolbar

1. To install Django Debug Toolbar to your project type in the terminal the following code
    > pip install django-debug-toolbar
2. Then in your project folder then settings go to **`dev.py`** file cause this gonna be in the development stage only and add the following to the end of the file

    ```python
        INSTALLED_APPS = INSTALLED_APPS + [
            "debug_toolbar",
        ]
    ```

3. Then in your project folder go to **`urls.py`** and add the following path to the urlpatterns
    > path('__debug__/', include('debug_toolbar.urls'))
4. Then we have to add the following to our middleware in the **`dev.py`**

    ```python
        MIDDLEWARE = MIDDLEWARE + [
            "debug_toolbar.middleware.DebugToolbarMiddleware",
        ]
    ```

5. Last thing we have to add our internal ips also to **`dev.py`**

    ```python
        INTERNAL_IPS = ("127.0.0.1")
    ```

### Django Shell Extension

1. On your terminal tyoe the following
    > pip install django-extensions
2. Then go to **`dev.py`** and just add it to the **`INSTALLED_APPS`**

    ```python
        INSTALLED_APPS = INSTALLED_APPS + [
            "django_extensions",
        ]
    ```

3. Then to enter the shell just run the following on the terminal
    > python manage.py shell_plus

#### Importent Codes

* **`__dict__`** : This will give us a dictionary of everything available.

### Ipython

1. On your terminal tyoe the following
    > pip install ipython

2. Then to enter the shell just run the following on the terminal
    > python manage.py shell_plus --ipython

------------------------------------------

## How To Set Site Settings

1. We gonna use **`BaseSetting`** for our class to inherit from.
2. And then we gonna use **`register_setting`** before our class to register it in the settings.

    ```python
    @register_setting(icon="media")
    class SocialMediaSettings(BaseSetting):
        ...
        ...
        ...
        panels = [
            ...
        ]
    ```

3. Then we have to enable the setting so we can get into there from **`base.py`** we go to **`TEMPLATES`** inside **`OPTIONS`** add to the **`context_processors`** the following
    > 'wagtail.contrib.settings.context_processors.settings',
4. Then in **`INSTALLED_APPS`** add the following
    > 'wagtail.contrib.settings',

------------------------------------------

## Routable Page

1. First we have to enable Routable Page from the **`settings`** **`INSTALLED_APPS`**
    > 'wagtail.contrib.routable_page',

2. In the page you needed the route you have to import **`RoutablePageMixin`** & **`route`** from **`wagtail.contrib.routable_page.models`**

------------------------------------------

## Sitemaps

1. First we have to enable Sitemaps from the **`settings`** **`INSTALLED_APPS`** for **`django`** and **`wagtail`**

    ```python
        'wagtail.contrib.sitemaps',
        'django.contrib.sitemaps',
    ```

2. Then we have to import wagtail sitemaps views to our project **`urls.py`**
    > from wagtail.contrib.sitemaps.views import sitemap

3. Then add our url to **`urlpatterns`**

    ```python
        path(r'^sitemap.xml$', sitemap)
    ```

------------------------------------------

## Wagtail Imports

```python
# Models
from wagtail.core import blocks
from wagtail.core.models import (
    Page,
    Orderable,
)
# Fields
from wagtail.core.fields import (
    RichTextField,
    StreamField,
)
from modelcluster.fields import (
    ParentalKey,
    ParentalManyToManyField,
)
# Admin Panels
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
    InlinePanel,
)
# Images
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
# Site Settings Models
from wagtail.contrib.settings.models import (
    BaseSetting,
    register_setting,
)
# Routable Page
from wagtail.contrib.routable_page.models import (
    RoutablePageMixin,
    route,
)
# Snippets
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
# Model Admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
# Django Imports
from django.db import models
from django.shortcuts import render
from django import forms
```
