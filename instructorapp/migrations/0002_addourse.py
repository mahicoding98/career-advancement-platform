# Generated by Django 5.0.2 on 2024-02-22 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('course_image', models.ImageField(upload_to='course_images/')),
                ('course_category', models.CharField(max_length=100)),
                ('course_language', models.CharField(max_length=100)),
                ('course_description', models.TextField()),
                ('video_url', models.URLField()),
                ('duration_weeks', models.IntegerField()),
                ('price', models.CharField(max_length=10)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructorapp.instructorregmodel')),
            ],
            options={
                'db_table': 'Courses_details',
            },
        ),
    ]
