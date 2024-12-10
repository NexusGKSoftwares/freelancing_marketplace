# Generated by Django 5.1.4 on 2024-12-10 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0010_systemsetting_alter_staticpage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='system_setting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.systemsetting'),
        ),
    ]
