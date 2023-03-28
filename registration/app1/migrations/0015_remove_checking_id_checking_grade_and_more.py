# Generated by Django 4.1.7 on 2023-03-22 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_remove_looming_id_remove_looming_supervisor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checking',
            name='id',
        ),
        migrations.AddField(
            model_name='checking',
            name='grade',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='checking',
            name='orderNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app1.adminjobcard'),
        ),
    ]