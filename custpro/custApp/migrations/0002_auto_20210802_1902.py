# Generated by Django 2.2.3 on 2021-08-02 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='customerQuery',
            new_name='customer_query',
        ),
        migrations.AlterModelTable(
            name='customer_query',
            table='customer_query',
        ),
    ]