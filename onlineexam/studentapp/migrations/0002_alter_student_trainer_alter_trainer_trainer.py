# Generated by Django 4.2.4 on 2023-08-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Trainer',
            field=models.CharField(choices=[('Rohini', 'Rohini')], max_length=50),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='trainer',
            field=models.CharField(choices=[('Rohini', 'Rohini')], max_length=50),
        ),
    ]