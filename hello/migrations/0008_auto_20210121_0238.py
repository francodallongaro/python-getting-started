# Generated by Django 3.1.5 on 2021-01-21 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_auto_20210117_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqs',
            name='respuestas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faqs',
            name='respuesta',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
