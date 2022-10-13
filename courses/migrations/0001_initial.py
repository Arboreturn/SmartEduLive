# Generated by Django 4.1 on 2022-09-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kurs adınız yazınız', max_length=200, unique=True, verbose_name='Kurs Adı')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='courses/default_course_image.jpg', upload_to='courses/%Y/%m/%d/')),
                ('date', models.DateField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
