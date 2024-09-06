from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    editor = models.CharField(max_length=50, blank=False, default='')
    publish = models.CharField(max_length=50, blank=False, default='')
    category = models.CharField(max_length=50, blank=False, default='')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('id',)
