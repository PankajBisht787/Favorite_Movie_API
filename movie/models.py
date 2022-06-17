from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField( null=False)
    ranking = models.IntegerField(null=True,blank=True)
    review = models.CharField(max_length=200)
    img_url = models.URLField(default="")
    
    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['rating']
        