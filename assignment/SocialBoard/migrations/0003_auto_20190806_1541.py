# Generated by Django 2.2.4 on 2019-08-06 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBoard', '0002_auto_20190806_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]