# Generated by Django 4.2.3 on 2023-08-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_comments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(choices=[('N', 'No category'), ('F', 'Fasion'), ('T', 'Toys'), ('E', 'Electronics'), ('H', 'Home'), ('HW', 'Hardware')], default='', max_length=200),
        ),
    ]
