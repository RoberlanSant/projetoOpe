# Generated by Django 2.2.4 on 2019-10-18 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0006_remove_funcionario_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='imagem',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
