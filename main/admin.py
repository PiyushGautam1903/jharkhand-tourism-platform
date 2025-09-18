from django.contrib import admin
from .models import TourismPlace, UserProfile, PlacePhoto, PlaceReview, TravelItinerary, AccommodationBooking

@admin.register(TourismPlace)
class TourismPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'place_type', 'district', 'rating', 'is_featured', 'created_at')
    list_filter = ('place_type', 'district', 'is_featured', 'difficulty_level', 'created_at')
    search_fields = ('name', 'description', 'district', 'activities')
    ordering = ('name',)
    list_editable = ('is_featured', 'rating')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'place_type', 'district', 'is_featured', 'rating')
        }),
        ('Location', {
            'fields': ('latitude', 'longitude', 'altitude')
        }),
        ('Visit Information', {
            'fields': ('best_time_to_visit', 'entry_fee', 'timings', 'difficulty_level')
        }),
        ('Detailed Information', {
            'fields': ('how_to_reach', 'nearby_attractions', 'activities', 'local_food', 
                     'accommodation', 'weather_info', 'safety_tips', 'photography_tips')
        }),
        ('Cultural & Historical', {
            'fields': ('historical_significance', 'cultural_importance')
        }),
        ('Contact & Media', {
            'fields': ('contact_info', 'website', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        })
    )
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'date_of_birth', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone_number')
    list_filter = ('created_at',)
    
@admin.register(PlacePhoto)
class PlacePhotoAdmin(admin.ModelAdmin):
    list_display = ('place', 'caption', 'uploaded_by', 'is_approved', 'uploaded_at')
    list_filter = ('is_approved', 'uploaded_at', 'place__district')
    search_fields = ('place__name', 'caption', 'uploaded_by__username')
    list_editable = ('is_approved',)
    
@admin.register(PlaceReview)
class PlaceReviewAdmin(admin.ModelAdmin):
    list_display = ('place', 'user', 'rating', 'title', 'is_verified', 'created_at')
    list_filter = ('rating', 'is_verified', 'created_at', 'place__district')
    search_fields = ('place__name', 'user__username', 'title', 'review_text')
    list_editable = ('is_verified',)
    
@admin.register(TravelItinerary)
class TravelItineraryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start_date', 'end_date', 'is_public', 'created_at')
    list_filter = ('is_public', 'created_at', 'start_date')
    search_fields = ('title', 'user__username', 'description')
    
@admin.register(AccommodationBooking)
class AccommodationBookingAdmin(admin.ModelAdmin):
    list_display = ('booking_reference', 'user', 'place', 'hotel_name', 'check_in_date', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'check_in_date', 'place__district')
    search_fields = ('booking_reference', 'user__username', 'hotel_name', 'place__name')
    list_editable = ('status',)
    readonly_fields = ('booking_reference', 'created_at')
