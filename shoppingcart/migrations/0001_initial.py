# Generated by Django 2.1.3 on 2018-12-03 01:18
import csv

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('upc12', models.PositiveIntegerField()),
                ('upc14', models.PositiveIntegerField()),
                ('brand', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),

    ]

    def seedDatabase():
        csv_data = csv.reader(file(products.csv))
