from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q, Avg
import json
from .models import TourismPlace, UserProfile, PlacePhoto, PlaceReview, TravelItinerary, AccommodationBooking

def home(request):
    """Home page with login/register options"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'main/home.html')

def login_view(request):
    """User login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'main/login.html')

def register_view(request):
    """User registration view"""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'main/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'main/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'main/register.html')
        
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Create user profile
        UserProfile.objects.create(
            user=user,
            phone_number=phone,
            address=address
        )
        
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')
    
    return render(request, 'main/register.html')

def logout_view(request):
    """User logout view"""
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    """Main dashboard after login"""
    # Get featured places
    featured_places = TourismPlace.objects.filter(is_featured=True).order_by('-rating')[:6]
    
    # Get user statistics
    user_reviews_count = PlaceReview.objects.filter(user=request.user).count()
    user_bookings_count = AccommodationBooking.objects.filter(user=request.user).count()
    user_itineraries_count = TravelItinerary.objects.filter(user=request.user).count()
    
    # Get recent reviews
    recent_reviews = PlaceReview.objects.filter(is_verified=True).order_by('-created_at')[:3]
    
    # Get place statistics
    total_places = TourismPlace.objects.count()
    place_types_count = TourismPlace.objects.values('place_type').distinct().count()
    
    context = {
        'featured_places': featured_places,
        'user': request.user,
        'user_reviews_count': user_reviews_count,
        'user_bookings_count': user_bookings_count,
        'user_itineraries_count': user_itineraries_count,
        'recent_reviews': recent_reviews,
        'total_places': total_places,
        'place_types_count': place_types_count,
    }
    return render(request, 'main/dashboard.html', context)

@login_required
def places_list(request):
    """Enhanced list view with search and filtering"""
    places = TourismPlace.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        places = places.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(district__icontains=search_query) |
            Q(activities__icontains=search_query)
        )
    
    # Filter by place type
    place_type = request.GET.get('type')
    if place_type:
        places = places.filter(place_type=place_type)
    
    # Filter by district
    district = request.GET.get('district')
    if district:
        places = places.filter(district=district)
    
    # Filter by difficulty
    difficulty = request.GET.get('difficulty')
    if difficulty:
        places = places.filter(difficulty_level=difficulty)
    
    # Sort options
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'rating':
        places = places.order_by('-rating')
    elif sort_by == 'name':
        places = places.order_by('name')
    elif sort_by == 'district':
        places = places.order_by('district', 'name')
    
    # Pagination
    paginator = Paginator(places, 12)  # Show 12 places per page
    page_number = request.GET.get('page')
    page_places = paginator.get_page(page_number)
    
    # Get filter options
    districts = TourismPlace.objects.values_list('district', flat=True).distinct().order_by('district')
    
    context = {
        'places': page_places,
        'place_types': TourismPlace.PLACE_TYPES,
        'difficulty_levels': TourismPlace.DIFFICULTY_LEVELS,
        'districts': districts,
        'current_search': search_query,
        'current_type': place_type,
        'current_district': district,
        'current_difficulty': difficulty,
        'current_sort': sort_by,
    }
    return render(request, 'main/places_list.html', context)

@login_required
def place_detail(request, place_id):
    """Enhanced detailed view of a specific place"""
    place = get_object_or_404(TourismPlace, id=place_id)
    
    # Get place photos
    photos = PlacePhoto.objects.filter(place=place, is_approved=True)
    
    # Get place reviews
    reviews = PlaceReview.objects.filter(place=place, is_verified=True).order_by('-created_at')
    user_review = None
    if request.user.is_authenticated:
        user_review = PlaceReview.objects.filter(place=place, user=request.user).first()
    
    # Calculate average rating
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    # Get similar places (same type, different places)
    similar_places = TourismPlace.objects.filter(
        place_type=place.place_type
    ).exclude(id=place.id)[:4]
    
    # Get nearby places (same district)
    nearby_places = TourismPlace.objects.filter(
        district=place.district
    ).exclude(id=place.id)[:4]
    
    context = {
        'place': place,
        'photos': photos,
        'reviews': reviews,
        'user_review': user_review,
        'avg_rating': avg_rating,
        'similar_places': similar_places,
        'nearby_places': nearby_places,
    }
    return render(request, 'main/place_detail.html', context)

# Smart Feature Views

@login_required
def add_review(request, place_id):
    """Add or update a review for a place"""
    place = get_object_or_404(TourismPlace, id=place_id)
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        title = request.POST.get('title')
        review_text = request.POST.get('review_text')
        visit_date = request.POST.get('visit_date')
        
        review, created = PlaceReview.objects.update_or_create(
            place=place,
            user=request.user,
            defaults={
                'rating': rating,
                'title': title,
                'review_text': review_text,
                'visit_date': visit_date,
            }
        )
        
        if created:
            messages.success(request, 'Review added successfully! It will be visible after verification.')
        else:
            messages.success(request, 'Review updated successfully!')
        
        return redirect('place_detail', place_id=place_id)
    
    return redirect('place_detail', place_id=place_id)

@login_required
def create_booking(request, place_id):
    """Create accommodation booking for a place"""
    place = get_object_or_404(TourismPlace, id=place_id)
    
    if request.method == 'POST':
        hotel_name = request.POST.get('hotel_name')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        guests_count = request.POST.get('guests_count')
        contact_phone = request.POST.get('contact_phone')
        special_requests = request.POST.get('special_requests', '')
        
        booking = AccommodationBooking.objects.create(
            user=request.user,
            place=place,
            hotel_name=hotel_name,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            guests_count=guests_count,
            contact_phone=contact_phone,
            special_requests=special_requests
        )
        
        messages.success(request, f'Booking request created successfully! Your booking reference is {booking.booking_reference}')
        return redirect('user_bookings')
    
    context = {'place': place}
    return render(request, 'main/create_booking.html', context)

@login_required
def user_bookings(request):
    """List user's accommodation bookings"""
    bookings = AccommodationBooking.objects.filter(user=request.user).order_by('-created_at')
    context = {'bookings': bookings}
    return render(request, 'main/user_bookings.html', context)

@login_required
def create_itinerary(request):
    """Create a new travel itinerary"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        is_public = request.POST.get('is_public') == 'on'
        
        itinerary = TravelItinerary.objects.create(
            user=request.user,
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            is_public=is_public
        )
        
        messages.success(request, 'Itinerary created successfully!')
        return redirect('itinerary_detail', itinerary_id=itinerary.id)
    
    return render(request, 'main/create_itinerary.html')

@login_required
def itinerary_detail(request, itinerary_id):
    """View and manage itinerary details"""
    itinerary = get_object_or_404(TravelItinerary, id=itinerary_id)
    
    # Check if user owns the itinerary or if it's public
    if itinerary.user != request.user and not itinerary.is_public:
        messages.error(request, 'You do not have permission to view this itinerary.')
        return redirect('dashboard')
    
    itinerary_places = itinerary.itineraryplace_set.all().order_by('day_number', 'visit_time')
    context = {
        'itinerary': itinerary,
        'itinerary_places': itinerary_places
    }
    return render(request, 'main/itinerary_detail.html', context)

@csrf_exempt
@login_required
def weather_api(request):
    """API endpoint to get weather data for a location"""
    if request.method == 'POST':
        data = json.loads(request.body)
        lat = data.get('lat')
        lon = data.get('lon')
        
        # Mock weather data - in real implementation, call weather API
        weather_data = {
            'temperature': '25°C',
            'condition': 'Partly Cloudy',
            'humidity': '65%',
            'wind_speed': '12 km/h',
            'icon': 'partly-cloudy'
        }
        
        return JsonResponse({
            'success': True,
            'weather': weather_data
        })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required
def upload_photo(request, place_id):
    """Upload photo for a place"""
    place = get_object_or_404(TourismPlace, id=place_id)
    
    if request.method == 'POST' and request.FILES.get('photo'):
        photo = PlacePhoto.objects.create(
            place=place,
            image=request.FILES['photo'],
            caption=request.POST.get('caption', ''),
            uploaded_by=request.user
        )
        
        messages.success(request, 'Photo uploaded successfully! It will be visible after approval.')
        return redirect('place_detail', place_id=place_id)
    
    return redirect('place_detail', place_id=place_id)

