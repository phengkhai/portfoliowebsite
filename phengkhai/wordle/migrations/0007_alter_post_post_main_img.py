# Generated by Django 4.0.2 on 2022-06-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordle', '0006_alter_post_post_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_Main_Img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='product/%Y/%m/%d'),
        ),
    ]
