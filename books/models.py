from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    source_web = models.CharField(max_length=100)

class Order(models.Model):
    title = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    source_web = models.CharField(max_length=100)
    repo_name = models.CharField(max_length=50)
    book_id = models.CharField(max_length=50)
    user_id = models.IntegerField(default=0)