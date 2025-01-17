# Generated by Django 5.1.4 on 2024-12-09 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0002_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('comment', models.TextField()),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='freelancer.freelancer')),
            ],
        ),
    ]
