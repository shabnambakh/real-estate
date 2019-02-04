# Real Estate web application with Docker

Install
=======

Build images:

    $ docker-compose build

Start services:

    $ docker-compose up -d

Go to http://localhost:8000/ on a web browser

Create superuser for admin:

    $ docker-compose run web python /code/manage.py createsuperuser
