# Generated by Django 3.0.14 on 2021-06-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subapp01', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Loan',
            field=models.CharField(max_length=20),
        ),
    ]