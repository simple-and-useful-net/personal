# Generated by Django 4.2.5 on 2024-01-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0008_alter_personaldatamodel_prefecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldatamodel',
            name='prefecture',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='personaldatamodel',
            name='sex',
            field=models.TextField(),
        ),
    ]
