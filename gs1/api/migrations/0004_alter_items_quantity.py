# Generated by Django 5.1.3 on 2024-11-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]