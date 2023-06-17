# Generated by Django 3.2.5 on 2023-04-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20230406_0741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('guest_number', models.IntegerField()),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
    ]
