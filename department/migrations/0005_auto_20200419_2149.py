# Generated by Django 3.0.5 on 2020-04-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_auto_20200419_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='d_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Department'),
        ),
    ]