# Generated by Django 2.2.4 on 2019-10-19 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_auto_20190923_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueitens',
            name='saldo',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
