# Generated by Django 5.1.2 on 2024-12-08 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_profiledata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledata',
            name='post',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='data.post'),
        ),
    ]