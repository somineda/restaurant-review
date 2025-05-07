from django.db import models
from config.models import BaseModel
from users.models import User
from restaurants.models import Restaurant

class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.nickname}'s review of {self.restaurant.name}"
from django.db import models

# Create your models here.
