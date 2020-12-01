from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,null = True)
	post = models.TextField()
	timestamp = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.post

class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name = "comment")
	comment = models.TextField()
	timestamp = models.DateTimeField(default = timezone.now)
	user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE, null = True)

	def __str__(self):
		return self.comment

class Image(models.Model):
    post_image= models.ImageField(upload_to='upload/')

