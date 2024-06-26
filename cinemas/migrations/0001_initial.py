# Generated by Django 5.0.4 on 2024-05-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Nome')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('district', models.CharField(max_length=50, verbose_name='Bairro')),
                ('street', models.CharField(max_length=50, verbose_name='Rua')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'verbose_name_plural': 'Cinemas',
                'ordering': ['name'],
            },
        ),
    ]
