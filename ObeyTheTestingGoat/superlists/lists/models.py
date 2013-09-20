from django.db import models

class List(models.Model):
	name = models.CharField(max_length=64, default='')
    
class Item(models.Model):
	text = models.TextField()
	list = models.ForeignKey(List)
