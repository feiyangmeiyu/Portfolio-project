from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=225)
	pub_date = models.DateTimeField()
	body = models.TextField(max_length=1000)
	image = models.ImageField(upload_to='images/')
# Create a blog model
# title
# pub_date
# body
#


# Add the Blog app to the settings

#Create a migration

#Migrate

#Add to the admin
