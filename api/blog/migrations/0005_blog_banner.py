# Generated by Django 4.1.7 on 2023-04-04 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_options_remove_blog_banner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='banner',
            field=models.ImageField(default='banner.png', upload_to='uploads/% Y/% m/% d/'),
        ),
    ]
