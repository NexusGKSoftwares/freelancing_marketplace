# Generated by Django 5.1.4 on 2024-12-06 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], default='Pending', max_length=10)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='freelancer.freelancer')),
            ],
        ),
    ]
