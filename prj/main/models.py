from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=True)
    def __str__(self):
     return f"{self.name}({self.year})"
# Create your models here.