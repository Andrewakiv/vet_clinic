# Generated by Django 5.0.1 on 2024-01-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet_clinic', '0005_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('response', models.TextField(blank=True)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
