from django.db import models

class List(models.Model):
	name = models.CharField(max_length=64, default='')
    
class Item(models.Model):
	text = models.TextField()
	list = models.ForeignKey(List)
	
	class Meta:
		ordering = ('id',)
		unique_together = ('list', 'text')

	def __unicode__(self):
		return self.text
        
	def save(self, *args, **kwargs):
		self.full_clean()
		super(Item, self).save(*args, **kwargs)


