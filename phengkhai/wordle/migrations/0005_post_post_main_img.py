# Generated by Django 4.0.2 on 2022-05-31 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordle', '0004_remove_post_hotel_main_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_Main_Img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
