# Generated by Django 3.2.7 on 2021-12-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConnectToHealMain', '0004_alter_bookappointmentmodel_therapistname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointmentmodel',
            name='sessionstatus',
            field=models.BooleanField(default=False),
        ),
    ]
