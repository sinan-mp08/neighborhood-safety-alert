

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Alert(models.Model):
    CATEGORY_CHOICES = [
        ('Fire', 'Fire'),
        ('Theft', 'Theft'),
        ('Accident', 'Accident'),
        ('Disaster', 'Natural Disaster'),
        ('Suspicious', 'Suspicious Activity'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_official = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    
    
# Additional model for user reports
class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=20, default='Pending')
    date_reported = models.DateTimeField(auto_now_add=True) # Pending / Approved / Rejected

    def __str__(self):
        return f"{self.title} by {self.reporter.username}"



from django.db import models

class Incident(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
