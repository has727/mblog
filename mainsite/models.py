from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField(default=datetime.now)
	
	class Meta:
		ordering = ('-pub_date',)
		
	def __str__(self):
		return self.title
	
	
