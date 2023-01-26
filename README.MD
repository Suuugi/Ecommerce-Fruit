# Getting Started
1. Clone the repository to the ecommerce folder

        git clone https://github.com/Suuugi/Ecommerce-Fruit.git ecommerce

2. Change directories to the ecommerce folder

        cd ecommerce

3. Install a virtual environment

        py -m venv venv

4. Allow the virtual environment process to activate

        Set-ExecutionPolicy Unrestricted -Scope Process

5. Activate the virtual environment

        ./venv/Scripts/activate.ps1

6. Install the required python packages to the virtual environment

        pip install -r requirements.txt

7. Create Django migrations for accounts app

        py manage.py makemigrations accounts

8. Create Django migrations for store app

        py manage.py makemigrations store

9. Migrate Django apps to create tables in database

        py manage.py migrate

10. Run server to deploy the application locally

        py manage.py runserver

# Coding conventions (Following PEP8 & PEP257)
- HTML use double quotes for values

        <link href="{% static 'fontawesomefree/css/solid.css' %}" rel="stylesheet" type="text/css">

- DJANGO content in HTML use single quotes

        {% extends 'base.html' %}

- DJANGO and PYTHON code use single quotes

        'helloworld'

- DJANGO and PYTHON docstring use double quotes

        """write it like this even if it's just one line"""
