# Generated by Django 5.0.1 on 2024-01-18 15:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet_clinic', '0008_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to=settings.AUTH_USER_MODEL),
        ),
    ]