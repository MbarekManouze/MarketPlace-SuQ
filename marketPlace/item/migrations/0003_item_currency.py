# Generated by Django 4.0 on 2024-05-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Currency',
            field=models.TextField(blank=True, null=True),
        ),
    ]