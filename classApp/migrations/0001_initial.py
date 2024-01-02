# Generated by Django 4.2.5 on 2023-12-31 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('sex', models.TextField(choices=[('男', '男'), ('女', '女')], default='女')),
                ('prefecture', models.TextField(blank=True, choices=[('北海道', '北海道'), ('東京都', '東京都'), ('大阪府', '大阪府')], default='大阪府')),
                ('hobby', models.JSONField()),
                ('food', models.JSONField()),
            ],
        ),
    ]
