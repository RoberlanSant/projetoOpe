# Generated by Django 2.2.4 on 2019-11-16 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20191115_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(help_text='nome da empresa', max_length=100),
        ),
    ]
