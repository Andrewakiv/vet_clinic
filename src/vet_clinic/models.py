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


class Team(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/%Y/%m/%d/', blank=True, null=True, default=None)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'
        ordering = ['-publish_date']
        indexes = [
            models.Index(fields=['-publish_date']),
        ]


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True, null=True, default=None)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_likes', blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='rubric', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-publish_date']
        indexes = [
            models.Index(fields=['-publish_date']),
        ]

    def get_absolute_url(self):
        return reverse("vet_clinic:blog_detail", kwargs={"blog_slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vet_clinic:category_blog", kwargs={"category_blog_slug": self.slug})


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


class Order(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DRF', 'Draft'
        COMPLETE = 'CMP', 'Complete'
        CONFIRM = 'CNF', 'Confirm'
        DELAY = 'DLY', 'Delay'

    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='names', null=True, blank=True)
    phone_number = PhoneNumberField()
    pet_info = models.CharField(max_length=50)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service', null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    date_for_visit = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-order_date']
        indexes = [
            models.Index(fields=['-order_date']),
        ]

    def get_absolute_url(self):
        return reverse("vet_clinic:order_detail", kwargs={"order_id": self.id})

    def __str__(self):
        return f'Order by {self.name}'


class Comment(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comm_name')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comm_post')
    comm_content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
