from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from applications.products.models import Favorite

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ForeignKey(Favorite, on_delete=models.CASCADE, blank=True, null=True)
    number = PhoneNumberField(unique=True)

    def __str__(self):
        return self.user.username
