from django.db import models

# Create your models here.

class Link(models.Model):
	url = models.URLField(null = False)
	shortner = models.CharField(max_length = 10, null = False)

		