# Generated by Django 4.2.5 on 2025-04-03 01:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scheduling', '0002_scheduling_created_at_scheduling_updated_at'),
        ('users', '0002_alter_clienteprofile_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('stars', models.PositiveSmallIntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='users.clienteprofile')),
                ('scheduling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='scheduling.scheduling')),
            ],
        ),
    ]
