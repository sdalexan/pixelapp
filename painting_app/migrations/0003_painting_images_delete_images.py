# Generated by Django 4.0.1 on 2022-02-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painting_app', '0002_images_delete_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Painting_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
