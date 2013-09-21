from django.db import models

class List(models.Model):
	name = models.CharField(max_length=64, default='')
    
class Item(models.Model):
	text = models.TextField()
	list = models.ForeignKey(List)

	def save(self, *args, **kwargs):
		self.full_clean()
		super(Item, self).save(*args, **kwargs)


