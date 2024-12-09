# Generated by Django 5.1.4 on 2024-12-08 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_activity_jobposting_payment_supportticket_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobposting',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='jobposting',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='jobposting',
            name='posted_by',
        ),
        migrations.AddField(
            model_name='jobposting',
            name='budget',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobposting',
            name='category',
            field=models.CharField(default='dev', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobposting',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='open', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]