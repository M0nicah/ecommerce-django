# Generated by Django 4.1.3 on 2022-12-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
    ]