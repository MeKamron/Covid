# Generated by Django 3.2.6 on 2021-08-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.EmailField(default='kancelyariyaresdsenm@minzdrav.uz', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='manzil',
            field=models.CharField(default='Адрес: Tashkent city, Chilanzar district, Bunyodkor street, 46', max_length=355),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='telfon',
            field=models.CharField(default='+998712761606', max_length=255),
            preserve_default=False,
        ),
    ]