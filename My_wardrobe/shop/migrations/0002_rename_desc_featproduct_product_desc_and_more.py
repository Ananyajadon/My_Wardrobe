# Generated by Django 4.1.5 on 2023-03-16 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featproduct',
            old_name='desc',
            new_name='product_desc',
        ),
        migrations.RenameField(
            model_name='featproduct',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='featproduct',
            old_name='price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='featproduct',
            old_name='pub_date',
            new_name='publish_date',
        ),
        migrations.RenameField(
            model_name='featproduct',
            old_name='subcategory',
            new_name='sub_category',
        ),
    ]