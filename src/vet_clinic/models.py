from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Service(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='services/%Y/%m/%d/', blank=True, null=True, default=None)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-price']
        indexes = [
            models.Index(fields=['-price']),
        ]

    def get_absolute_url(self):
        return reverse("vet_clinic:service_detail", kwargs={"service_slug": self.slug})


class Testimonial(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    response = models.TextField(max_length=500, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['-publish_date']
        indexes = [
            models.Index(fields=['-publish_date']),
        ]

    def __str__(self):
        return self.name

