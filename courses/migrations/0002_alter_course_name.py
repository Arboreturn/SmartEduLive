# Generated by Django 4.1 on 2022-09-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(help_text='write the course name', max_length=200, unique=True, verbose_name='Course Name'),
        ),
    ]
