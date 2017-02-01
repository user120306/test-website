from django.db import models
from datetime import datetime, timedelta

class User(models.Model):
	fname = models.CharField(max_length=255)
	lname= models.CharField(max_length=255)
	email=models.EmailField(max_length=255)
	password = models.CharField(max_length=200)
	join_date=models.DateTimeField(editable=False,default=datetime.now())
	#profile_pic = models.ImageField(upload_to = 'user/',null=True)
	def __str__(self):
		return self.email

class Todo(models.Model):
    todo_job= models.TextField()
    user=models.ForeignKey('User')
    created_date=models.DateTimeField(editable=False,default=datetime.now())
    def __str__(self):
        return self.todo_job