from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


#model for Bids
#class Category(models.Model):
#    type = models.CharField(max_length=64)

#model for auction listings
class Listing(models.Model):
    CATEGORY_CHOICES = {
        ("Fashion", "Fashion"),
        ("Toys", "Toys"),
        ("Electronics", "Electronics"),
        ("Home", "Home"),
        ("Clothing", "Clothing")
    }
    name = models.CharField(max_length=64)
    comment = models.CharField(max_length=250)
    price = models.IntegerField()
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default="Fashion",)

    def __str__(self):
        return f"{self.name} : {self.price}"



#model for Bids
#class Bid(models.Model):
#    pass

#model for Comments made on auction listings
#class Comment(models.Model):
    pass