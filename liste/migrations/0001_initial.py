# Generated by Django 2.0 on 2020-05-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20)),
                ('Prenom', models.CharField(max_length=20)),
                ('Profession', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
