# Generated by Django 2.2.4 on 2019-11-06 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0011_auto_20191028_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='password',
        ),
    ]
