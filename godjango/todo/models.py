from django.db import models
from django.template.defaultfilters import slugify

class Task(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    priority = models.TextField(blank=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Task, self).save(*args, **kwargs)
