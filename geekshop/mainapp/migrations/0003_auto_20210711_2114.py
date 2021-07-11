# Generated by Django 3.2.5 on 2021-07-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_specifications_for_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publisher',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='specifications',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='translator',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
