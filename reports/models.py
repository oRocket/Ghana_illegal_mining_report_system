from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=255)
    gps_coordinates = models.CharField(max_length=100)
    description = models.TextField()
    mining_type = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='reports_photos/', blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    reporter_contact = models.CharField(max_length=100, blank=True, null=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # Add this line

    def __str__(self):
        return f"{self.location} - {self.mining_type}"

class EducationalContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    images = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Adjust the upload_to path as needed
    categories = models.CharField(max_length=200, blank=True, null=True)  # Consider using a ManyToManyField for categories
    references = models.TextField(blank=True, null=True)
    summary = models.TextField()
    call_to_action = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title