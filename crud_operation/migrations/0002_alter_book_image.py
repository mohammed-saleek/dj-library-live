# Generated by Django 4.0.1 on 2022-04-07 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
