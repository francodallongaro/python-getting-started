# Generated by Django 3.1.5 on 2021-01-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_faqs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('precio', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Pack',
                'verbose_name_plural': 'Packs',
            },
        ),
    ]
