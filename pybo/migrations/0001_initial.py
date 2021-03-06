# Generated by Django 3.1.3 on 2022-04-01 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_auto_20220330_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('user', models.ForeignKey(db_column='account_useremail', on_delete=django.db.models.deletion.CASCADE, related_name='account', to='account.account')),
            ],
            options={
                'verbose_name': '이미지업로드',
                'verbose_name_plural': '이미지업로드',
                'db_table': 'image',
            },
        ),
    ]
