from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Good(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=70)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    good = models.ForeignKey(Good, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
