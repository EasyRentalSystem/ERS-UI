# Generated by Django 3.2.5 on 2022-05-15 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_auto_20220402_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('templateName', models.CharField(default='', max_length=128, verbose_name='템플릿명')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '템플릿',
                'db_table': 'Template',
            },
        ),
    ]