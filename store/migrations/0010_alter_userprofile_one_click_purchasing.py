# Generated by Django 4.0.4 on 2022-06-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_userprofile_one_click_purchasing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='one_click_purchasing',
            field=models.BooleanField(),
        ),
    ]