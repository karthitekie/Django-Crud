# Generated by Django 5.1.4 on 2024-12-18 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=255)),
                ('asset_type', models.CharField(max_length=255)),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('purchase_date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('under_maintenance', 'Under Maintenance')], max_length=50)),
                ('last_maintenance_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('supplier', models.CharField(max_length=255)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField()),
                ('description', models.TextField()),
                ('performed_by', models.CharField(max_length=255)),
                ('next_due_date', models.DateField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenances', to='assets.asset')),
            ],
        ),
    ]
