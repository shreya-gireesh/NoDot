# Generated by Django 5.1.2 on 2024-10-24 05:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_servicemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPostModel',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('responsibilities', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('requirements', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('desirable_skills', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('education', models.CharField(max_length=255)),
                ('job_type', models.CharField(choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('contract', 'Contract'), ('internship', 'Internship')], max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('experience_required', models.CharField(max_length=100)),
            ],
        ),
    ]
