# Generated by Django 3.2.7 on 2021-12-26 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConnectToHealMain', '0003_bookappointmentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointmentmodel',
            name='therapistName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
