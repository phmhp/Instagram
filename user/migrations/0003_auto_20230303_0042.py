# Generated by Django 3.2.18 on 2023-03-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=24, unique=True),
        ),
    ]
