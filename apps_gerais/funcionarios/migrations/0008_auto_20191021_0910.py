# Generated by Django 2.2.4 on 2019-10-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0007_funcionario_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(default=1, max_length=11, unique=True, verbose_name='CPF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='de_ferias',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='idade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='telefone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]