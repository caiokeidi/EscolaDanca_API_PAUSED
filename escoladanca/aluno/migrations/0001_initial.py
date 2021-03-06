# Generated by Django 3.1.5 on 2021-03-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiroNome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=80)),
                ('dataNascimento', models.DateField()),
                ('rg', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
