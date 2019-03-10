# MYDOO

## Table of Content
* [About Todo Server](#about-server)
* [Install Todo Server](#install-server)

## About Server

Server is designed with Django Rest Framework (DRF). There are only two models i.e. TodoList and Tags where tags have manytomany relationship with TodoList using default intermediary model.

[Django Tinymce](https://github.com/aljosa/django-tinymce) is used in TodoList description field for the purpose of using django feature if UI is built with django template.

MYDOO REST API [Documentation]()

## Install Todo Server
If you have [Docker](https://docs.docker.com) and [Docker Compose](https://docs.docker.com/compose/) installed. Just run below command and the server is ready to access through [http://localhost:8000](http://localhost:8000).
```docker
docker-compose up -d
```