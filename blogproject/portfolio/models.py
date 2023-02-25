from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title