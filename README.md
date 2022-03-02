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