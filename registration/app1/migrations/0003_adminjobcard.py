# Generated by Django 4.1.7 on 2023-03-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_user_usermapping'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminJobCard',
            fields=[
                ('orderNo', models.AutoField(primary_key=True, serialize=False)),
                ('orderDate', models.DateField()),
                ('companyName', models.CharField(max_length=100)),
                ('gst', models.CharField(max_length=100)),
                ('quality', models.CharField(max_length=100)),
                ('ppc', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('deadline', models.DateField()),
                ('count', models.IntegerField()),
                ('construction', models.IntegerField()),
                ('lengthOfCloth', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
                ('target', models.CharField(max_length=100)),
            ],
        ),
    ]