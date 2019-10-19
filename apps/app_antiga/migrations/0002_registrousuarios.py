# Generated by Django 2.2.4 on 2019-10-18 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_antiga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroUsuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'registro_usuarios',
            },
        ),
    ]
