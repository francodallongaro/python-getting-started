# Generated by Django 3.1.5 on 2021-01-11 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='precio',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
