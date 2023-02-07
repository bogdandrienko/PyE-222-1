from django.db import models


# Create your models here.

class Fruit(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    count = models.IntegerField()
    # ...

    def __str__(self):
        return f"{self.title} ({self.count}) [{self.price}] {self.id}"
