# Generated by Django 5.0.3 on 2024-03-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0004_alter_studentrank_date_of_report_generation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrank',
            name='date_of_report_generation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
