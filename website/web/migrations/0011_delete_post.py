# Generated by Django 5.0.2 on 2024-04-02 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_remove_image_uploaded_at_alter_image_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
