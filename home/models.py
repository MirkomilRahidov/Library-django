from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    pages = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    language = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
