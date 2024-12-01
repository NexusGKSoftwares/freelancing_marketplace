# Generated by Django 4.2.4 on 2024-12-01 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total_earnings', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('available', 'Available'), ('ongoing', 'Ongoing'), ('completed', 'Completed')], default='available', max_length=10)),
                ('deadline', models.DateTimeField()),
                ('freelancer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='freelancer.freelancer')),
            ],
        ),
        migrations.AddField(
            model_name='freelancer',
            name='active_jobs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='active_jobs', to='freelancer.job'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='completed_jobs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='completed_jobs', to='freelancer.job'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='feedbacks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='freelancer_feedbacks', to='freelancer.feedback'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
