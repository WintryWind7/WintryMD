from django.db import models

# Create your models here.
class MDdb(models.Model):
    family = models.CharField(max_length=200)
    dirname = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title