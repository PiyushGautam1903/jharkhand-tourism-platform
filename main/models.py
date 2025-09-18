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
        ('wildlife', 'Wildlife'),
        ('waterfall', 'Waterfall'),
        ('hill_station', 'Hill Station'),
        ('lake', 'Lake'),
        ('tribal', 'Tribal Culture'),
    ]
    
    DIFFICULTY_LEVELS = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('difficult', 'Difficult'),
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
    altitude = models.IntegerField(blank=True, null=True, help_text="Altitude in meters")
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS, blank=True)
    activities = models.TextField(blank=True, help_text="Activities available at this place")
    local_food = models.TextField(blank=True, help_text="Local food specialties")
    accommodation = models.TextField(blank=True, help_text="Accommodation options")
    weather_info = models.TextField(blank=True, help_text="Weather information")
    safety_tips = models.TextField(blank=True, help_text="Safety tips for visitors")
    historical_significance = models.TextField(blank=True)
    cultural_importance = models.TextField(blank=True)
    photography_tips = models.TextField(blank=True)
    contact_info = models.CharField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.0)
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
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    interests = models.CharField(max_length=500, blank=True, help_text="Comma-separated interests")
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class PlacePhoto(models.Model):
    place = models.ForeignKey(TourismPlace, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='place_photos/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Photo of {self.place.name}"
    
    class Meta:
        ordering = ['-uploaded_at']

class PlaceReview(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    place = models.ForeignKey(TourismPlace, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=200)
    review_text = models.TextField()
    visit_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)
    helpful_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.title} - {self.place.name}"
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['place', 'user']  # One review per user per place

class TravelItinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    places = models.ManyToManyField(TourismPlace, through='ItineraryPlace')
    start_date = models.DateField()
    end_date = models.DateField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"
    
    class Meta:
        ordering = ['-created_at']

class ItineraryPlace(models.Model):
    itinerary = models.ForeignKey(TravelItinerary, on_delete=models.CASCADE)
    place = models.ForeignKey(TourismPlace, on_delete=models.CASCADE)
    day_number = models.IntegerField()
    visit_time = models.TimeField(blank=True, null=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Day {self.day_number}: {self.place.name}"
    
    class Meta:
        ordering = ['day_number', 'visit_time']

class AccommodationBooking(models.Model):
    BOOKING_STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(TourismPlace, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=200)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests_count = models.IntegerField()
    contact_phone = models.CharField(max_length=15)
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='pending')
    booking_reference = models.CharField(max_length=20, unique=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.booking_reference:
            import uuid
            self.booking_reference = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Booking {self.booking_reference} - {self.place.name}"
    
    class Meta:
        ordering = ['-created_at']

