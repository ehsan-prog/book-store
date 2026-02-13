from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Kteb(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    touzihat = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to="cover/",blank=True )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_kteb", kwargs={"pk": self.pk})

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Kteb, on_delete=models.CASCADE,related_name="nazar")
    text = models.TextField()
    datetime = models.DateTimeField(  auto_now_add=True)
    publish = models.BooleanField(default=True)
    توصیه_میکنی_یا_نه = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.book.title} // {self.user.username}"