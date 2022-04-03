# Generated by Django 3.1.3 on 2022-04-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_auto_20220401_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='email',
            field=models.EmailField(default='', max_length=128, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/', verbose_name='이미지'),
        ),
    ]