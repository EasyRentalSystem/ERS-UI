# Generated by Django 3.1.3 on 2022-04-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_auto_20220402_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='email',
            field=models.EmailField(default='', max_length=128, verbose_name='이메일'),
        ),
    ]
