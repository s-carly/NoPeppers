from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
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
	image = models.ImageField()
	pub_date = models.DateTimeField('date published')

class Comment(models.Model):
	post = models.ForeignKey(Post,
		on_delete=models.CASCADE)

	comment = models.CharField(max_length=500)
	image = models.ImageField()
	pub_date = models.DateTimeField('date published')