# Generated by Django 2.1.7 on 2019-03-08 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190308_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcardnumber',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
