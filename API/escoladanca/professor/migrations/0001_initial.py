# Generated by Django 3.1.5 on 2021-03-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=50)),
                ('nomeCompleto', models.CharField(max_length=110)),
                ('descricao', models.TextField(max_length=500)),
            ],
        ),
    ]
