from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='accounts/%Y/%m/%d/', blank=True)
    send_mail = models.BooleanField(default=False)

    def __str__(self):
        return f'Profile of {self.user.username}'


class StaffProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'StaffProfile of {self.user.username}'


