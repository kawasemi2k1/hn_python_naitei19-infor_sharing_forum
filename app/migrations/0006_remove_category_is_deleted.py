# Generated by Django 4.2.5 on 2023-10-02 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_deleted',
        ),
    ]