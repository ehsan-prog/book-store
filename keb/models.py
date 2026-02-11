from django.db import models

class Kteb(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    touzihat = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to="cover/",blank=True )

    