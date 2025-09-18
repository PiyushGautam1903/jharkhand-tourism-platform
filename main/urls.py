from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('places/', views.places_list, name='places_list'),
    path('places/<int:place_id>/', views.place_detail, name='place_detail'),
    
    # Smart Features
    path('places/<int:place_id>/review/', views.add_review, name='add_review'),
    path('places/<int:place_id>/booking/', views.create_booking, name='create_booking'),
    path('places/<int:place_id>/upload-photo/', views.upload_photo, name='upload_photo'),
    path('bookings/', views.user_bookings, name='user_bookings'),
    path('itinerary/create/', views.create_itinerary, name='create_itinerary'),
    path('itinerary/<int:itinerary_id>/', views.itinerary_detail, name='itinerary_detail'),
    
    # APIs
    path('api/weather/', views.weather_api, name='weather_api'),
]
