# Generated by Django 2.2.4 on 2019-11-06 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0012_remove_funcionario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
    ]
