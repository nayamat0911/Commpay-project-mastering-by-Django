# Generated by Django 3.1.7 on 2021-03-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_slider_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='our_client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='clints/')),
            ],
        ),
    ]
