# Generated by Django 3.2.5 on 2022-05-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_template'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='template',
            options={'verbose_name': '생성된 템플릿'},
        ),
        migrations.AlterField(
            model_name='template',
            name='templateName',
            field=models.CharField(max_length=200),
        ),
    ]