# Generated by Django 5.0.1 on 2024-03-02 12:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='posts/%Y/%m/%d/')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='post_category', to='blog.category')),
                ('users_like', models.ManyToManyField(blank=True, related_name='users_like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_name', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='blog.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-publish_date'], name='blog_post_publish_7e8b08_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['created'], name='blog_commen_created_0e6ed4_idx'),
        ),
    ]