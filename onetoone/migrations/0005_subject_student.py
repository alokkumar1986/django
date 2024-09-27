# Generated by Django 5.0.8 on 2024-09-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onetoone', '0004_colour_flower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('subject', models.ManyToManyField(to='onetoone.subject')),
            ],
        ),
    ]
