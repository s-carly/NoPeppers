from django.db import models
from django.shortcuts import get_object_or_404, render

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Not specified")
    cuisine = models.CharField(max_length=50)
    capacity = models.IntegerField(default=0)
    seated = models.IntegerField(default=0)

    def check_cuisine(self, cuisine):
        if self.cuisine == cuisine:
            return True
        return False

    def get_cuisine(self):
        return self.cuisine

    def __str__(self):
        return self.name


class Post(models.Model):
    restaurant = models.ForeignKey(Restaurant,
        on_delete=models.CASCADE)

    content = models.CharField(max_length=500)
    image = models.ImageField(upload_to='posts')
    pub_date = models.DateTimeField('date published')

    context_object_name = "posts_list"

    def __str__(self):
        return f"{self.restaurant.name}: {self.content[:20]}"



class Comment(models.Model):
    post = models.ForeignKey(Post,
        on_delete=models.CASCADE)

    comment = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

