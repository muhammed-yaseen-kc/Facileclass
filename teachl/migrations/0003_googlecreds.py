# Generated by Django 3.2.5 on 2021-08-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachl', '0002_alter_roominfo_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='googlecreds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]