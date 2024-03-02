from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True, null=True, default=None)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users_like', blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='post_category', null=True)

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
        return reverse("blog:blog_detail", kwargs={"blog_slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category_blog", kwargs={"category_blog_slug": self.slug})


class Comment(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_name')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    comm_content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
