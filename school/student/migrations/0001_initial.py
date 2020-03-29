# Generated by Django 2.2.6 on 2020-03-18 10:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40)),
                ('grade', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_num', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=120)),
                ('class_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ClassRoom')),
            ],
        ),
    ]
