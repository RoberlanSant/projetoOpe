# Generated by Django 2.2 on 2019-09-23 03:59

from django.db import migrations, models
import apps_gerais.produto.models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.PositiveIntegerField(verbose_name='estoque atual'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='ncm',
            field=models.CharField(max_length=8, unique=True, validators=[apps_gerais.produto.models.validate_even], verbose_name='NCM'),
        ),
    ]
