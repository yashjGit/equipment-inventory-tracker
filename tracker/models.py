from django.db import models

class Equipment(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active - In Use'),
        ('Maintenance', 'Needs Maintenance'),
        ('Retired', 'Retired/Out of Service'),
    )

    part_name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    last_inspected = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.part_name} ({self.status})"