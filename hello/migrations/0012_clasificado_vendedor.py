# Generated by Django 3.1.5 on 2021-01-21 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0011_clasificado_pack'),
    ]

    operations = [
        migrations.AddField(
            model_name='clasificado',
            name='vendedor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario', to='hello.usuario'),
        ),
    ]
