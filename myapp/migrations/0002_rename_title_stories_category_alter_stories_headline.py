# Generated by Django 4.0.5 on 2022-06-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stories',
            old_name='title',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='stories',
            name='headline',
            field=models.CharField(max_length=150),
        ),
    ]
