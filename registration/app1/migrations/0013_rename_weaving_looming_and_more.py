# Generated by Django 4.1.7 on 2023-03-21 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_remove_winding_id_winding_defects_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Weaving',
            new_name='Looming',
        ),
        migrations.RemoveField(
            model_name='warping',
            name='buttonToReportToSupervisor',
        ),
    ]