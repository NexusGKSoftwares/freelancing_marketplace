# Generated by Django 5.1.4 on 2024-12-09 05:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_jobposting_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobposting',
            name='created_at',
        ),
        migrations.AddField(
            model_name='jobposting',
            name='current_applicants',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobposting',
            name='max_applicants',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='tags',
            field=models.ManyToManyField(blank=True, to='admin_panel.tag'),
        ),
    ]
