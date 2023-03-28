# Generated by Django 4.1.7 on 2023-03-21 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_weaving'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repairing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('repairingMachine', models.CharField(max_length=100)),
                ('worker', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='warping',
            name='orderNo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app1.adminjobcard'),
        ),
        migrations.AddField(
            model_name='winding',
            name='orderNo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app1.adminjobcard'),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='orderNo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app1.adminjobcard', unique=True),
        ),
        migrations.CreateModel(
            name='Checking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('loom', models.IntegerField()),
                ('worker', models.CharField(max_length=100)),
                ('defectInMeters', models.IntegerField()),
                ('points', models.CharField(max_length=100)),
                ('repairable', models.BooleanField()),
                ('orderNo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app1.adminjobcard')),
            ],
        ),
    ]