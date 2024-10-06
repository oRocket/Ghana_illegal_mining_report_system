from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=255)
    gps_coordinates = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    landmarks = models.CharField(max_length=255, blank=True, null=True)  # Optional

    mining_type = models.CharField(max_length=100, blank=True, null=True)  # Optional
    scale = models.CharField(max_length=50)
    machinery_used = models.CharField(max_length=255, blank=True, null=True)  # Optional
    mining_method = models.CharField(max_length=100, blank=True, null=True)  # Missing field
    
    environmental_impact = models.CharField(max_length=255)
    # environmental_impact = models.CharField(max_length=255, blank=True, null=True)  # Missing field
    description = models.TextField()
    photo = models.ImageField(upload_to='reports_photos/', blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    
    suspected_individuals = models.CharField(max_length=255, blank=True, null=True)  # Missing field
    num_people_involved = models.IntegerField(blank=True, null=True)  # Missing field
    reporter_name = models.CharField(max_length=100, blank=True, null=True)  # Missing field
    reporter_contact = models.CharField(max_length=100, blank=True, null=True)  # Already exists
    additional_comments = models.TextField(blank=True, null=True)  # Missing field

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

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
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Store reference to User
    content = models.TextField()
    images = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Optional field for images
    categories = models.CharField(max_length=100, blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    call_to_action = models.TextField(blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f"{self.author.first_name} {self.author.last_name}"

    def __str__(self):
        return self.title