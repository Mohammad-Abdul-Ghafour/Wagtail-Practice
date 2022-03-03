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

------------------------------------------

## How To Run Wagtail

1. First we have to migrate
    > python manage.py migrate
2. Then we should create the superuser
    > python manage.py createsuperuser
3. Then we can run the server
    > python manage.py runserver

------------------------------------------

## Install Django Debug Toolbar

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
