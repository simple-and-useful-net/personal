# Generated by Django 4.2.5 on 2024-01-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0020_alter_personaldatamodel_hobby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldatamodel',
            name='food',
            field=models.JSONField(default=list),
        ),
    ]
