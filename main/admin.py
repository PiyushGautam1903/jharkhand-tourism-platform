from django.contrib import admin
from .models import TourismPlace, UserProfile, ChatMessage

@admin.register(TourismPlace)
class TourismPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'place_type', 'district', 'created_at')
    list_filter = ('place_type', 'district', 'created_at')
    search_fields = ('name', 'description', 'district')
    ordering = ('name',)
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone_number')
    
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'message', 'response')
    readonly_fields = ('created_at',)
