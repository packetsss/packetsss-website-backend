# Generated by Django 3.2.7 on 2021-10-04 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211003_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
