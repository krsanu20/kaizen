# Generated by Django 3.0.8 on 2020-07-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oc', '0002_studentdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetail',
            name='phone_no',
            field=models.CharField(default='', max_length=256),
        ),
    ]
