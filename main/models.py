from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TourismPlace(models.Model):
    PLACE_TYPES = [
        ('eco', 'Eco Tourism'),
        ('cultural', 'Cultural Tourism'),
        ('adventure', 'Adventure Tourism'),
        ('religious', 'Religious'),
        ('historical', 'Historical'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    place_type = models.CharField(max_length=20, choices=PLACE_TYPES)
    district = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    image = models.ImageField(upload_to='places/', blank=True, null=True)
    best_time_to_visit = models.CharField(max_length=200)
    how_to_reach = models.TextField()
    nearby_attractions = models.TextField(blank=True)
    entry_fee = models.CharField(max_length=100, blank=True)
    timings = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    preferred_places = models.ManyToManyField(TourismPlace, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Chat by {self.user.username} at {self.created_at}"
    
    class Meta:
        ordering = ['-created_at']
