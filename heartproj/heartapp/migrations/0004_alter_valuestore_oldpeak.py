# Generated by Django 4.2 on 2023-05-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartapp', '0003_remove_valuestore_prediction_alter_valuestore_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valuestore',
            name='oldpeak',
            field=models.DecimalField(decimal_places=1, max_digits=1),
        ),
    ]
