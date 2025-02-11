from django.db import models


class Asset(models.Model):
    asset_name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('under_maintenance', 'Under Maintenance')])
    last_maintenance_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.asset_name} ({self.serial_number})"

# Define the Maintenance model
class Maintenance(models.Model):
    asset = models.ForeignKey(Asset, related_name='maintenances', on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    description = models.TextField()
    performed_by = models.CharField(max_length=255)
    next_due_date = models.DateField()
    
    def __str__(self):
        return f"Maintenance for {self.asset.asset_name} on {self.maintenance_date}"

# Define the Inventory model for spare parts
class Inventory(models.Model):
    part_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    supplier = models.CharField(max_length=255)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.part_name} ({self.quantity} available)"

class Category(models.Model):
    code = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.code