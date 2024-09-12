from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    editor = models.CharField(max_length=50, blank=False, default='')
    publish = models.CharField(max_length=50, blank=False, default='')
    STATUS_CHOICES = [
        ('C','童書'),
        ('D', '偵探小說'),
        ('S','自然科學'),
        ('N','文學小說'),
        ('F','財經'),
    ]
    category = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('id',)

class BookDetail(models.Model):
    model_Book = models.ForeignKey(Books, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self) -> str:
        return self.model_Book.name
