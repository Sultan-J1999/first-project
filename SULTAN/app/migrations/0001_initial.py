# Generated by Django 4.2.3 on 2023-07-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Location', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
