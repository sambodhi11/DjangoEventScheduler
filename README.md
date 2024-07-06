# DjangoEventScheduler
In this Django project we are going to connect the data that is added ,updated or deleted to the database which is db sql lite viewer.
Adding the urls in urls.py as the path, creating functions in the views.py and creating templates of html files to add access through the urls.
In urls.py the urls consists of path of the templates that we create.
In view.py we create functions to perform operations.
In models.py we use the syntax 
from django.db import models
  class class_name(models.Model):
The attributes are added to the database.
The command python manage.py makemigrations is part of Django's database migration framework.
It is used to create new migrations based on the changes you have made to your models and then python manage.py migrate to will help to add the models to the database.
The command python manage.py runserver helps to run the  http://127.0.0.1:8000/ .
