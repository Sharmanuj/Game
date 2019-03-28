# Generated by Django 2.1.7 on 2019-03-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_remove_staticschedule_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='staticschedule',
            name='room',
        ),
        migrations.RemoveField(
            model_name='staticschedule',
            name='slot',
        ),
        migrations.DeleteModel(
            name='StaticSchedule',
        ),
    ]
