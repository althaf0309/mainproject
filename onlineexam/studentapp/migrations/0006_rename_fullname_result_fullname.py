# Generated by Django 4.2.4 on 2023-09-08 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_rename_fullname_result_fullname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='FullName',
            new_name='Fullname',
        ),
    ]
