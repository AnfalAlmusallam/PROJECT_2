# Generated by Django 4.1.6 on 2023-02-13 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('telegram', models.IntegerField()),
                ('gender', models.BooleanField()),
                ('is_student', models.BooleanField()),
                ('state', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
