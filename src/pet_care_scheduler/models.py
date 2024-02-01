from django.conf import settings
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from vet_clinic.models import Service


class Schedule(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DRF', 'Draft'
        COMPLETE = 'CMP', 'Complete'
        CONFIRM = 'CNF', 'Confirm'
        DELAY = 'DLY', 'Delay'

    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_name')
    phone_number = PhoneNumberField()
    pet_info = models.CharField(max_length=50)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_name')
    order_date = models.DateTimeField(auto_now_add=True)
    date_for_visit = models.DateField()
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedule'
        ordering = ['-order_date']
        indexes = [
            models.Index(fields=['-order_date']),
        ]

    def get_absolute_url(self):
        return reverse("schedule:order_detail", kwargs={"order_id": self.id})

    def __str__(self):
        return f'Order by {self.name}'
