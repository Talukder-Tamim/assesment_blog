# Generated by Django 4.1.6 on 2023-02-12 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='posts',
        ),
    ]
