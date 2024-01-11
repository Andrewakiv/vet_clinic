# Generated by Django 5.0.1 on 2024-01-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet_clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('position', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='team/%Y/%m/%d/')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
                'ordering': ['-publish_date'],
                'indexes': [models.Index(fields=['-publish_date'], name='vet_clinic__publish_6c2f64_idx')],
            },
        ),
    ]