# Generated by Django 4.0.5 on 2022-06-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_customuser_activationtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='activationtoken',
            field=models.CharField(default='H44HSrtzCwuWczbs2zoDVKMqxHb9vaJv', max_length=255),
        ),
    ]
