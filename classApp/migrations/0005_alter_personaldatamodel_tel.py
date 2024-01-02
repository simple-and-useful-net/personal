# Generated by Django 4.2.5 on 2023-12-31 05:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0004_personaldatamodel_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldatamodel',
            name='tel',
            field=models.CharField(default='', max_length=11, validators=[django.core.validators.RegexValidator(message="電話番号は数字で入力してください 例: '09012340001'", regex='^[0-9]+$'), django.core.validators.MinLengthValidator(11)], verbose_name='電話番号'),
        ),
    ]
