from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TourismPlace, UserProfile, ChatMessage
import json

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
    places = TourismPlace.objects.all()[:6]  # Featured places
    context = {
        'places': places,
        'user': request.user
    }
    return render(request, 'main/dashboard.html', context)

@login_required
def places_list(request):
    """List all tourism places"""
    places = TourismPlace.objects.all()
    place_type = request.GET.get('type')
    district = request.GET.get('district')
    
    if place_type:
        places = places.filter(place_type=place_type)
    if district:
        places = places.filter(district__icontains=district)
    
    context = {
        'places': places,
        'place_types': TourismPlace.PLACE_TYPES,
    }
    return render(request, 'main/places_list.html', context)

@login_required
def place_detail(request, place_id):
    """Detailed view of a specific place"""
    place = get_object_or_404(TourismPlace, id=place_id)
    context = {
        'place': place
    }
    return render(request, 'main/place_detail.html', context)

@login_required
def chatbot(request):
    """Chatbot interface"""
    messages = ChatMessage.objects.filter(user=request.user)[:10]
    return render(request, 'main/chatbot.html', {'messages': messages})

@csrf_exempt
@login_required
def chatbot_api(request):
    """API endpoint for chatbot responses"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip().lower()
            
            # Simple chatbot responses for Jharkhand tourism
            responses = {
                'hello': 'Hello! Welcome to Jharkhand Tourism. How can I help you today?',
                'hi': 'Hi there! I\'m here to help you explore the beautiful state of Jharkhand.',
                'places': 'Jharkhand has amazing places like Ranchi, Jamshedpur, Deoghar, Netarhat, Betla National Park, and many more!',
                'ranchi': 'Ranchi is the capital city of Jharkhand, known for its waterfalls like Hundru Falls, Dassam Falls, and Rock Garden.',
                'deoghar': 'Deoghar is famous for the Baidyanath Temple, one of the twelve Jyotirlingas. It\'s a major pilgrimage destination.',
                'netarhat': 'Netarhat is known as the "Queen of Chhota Nagpur" for its scenic beauty and pleasant climate.',
                'betla': 'Betla National Park is famous for its wildlife including elephants, tigers, leopards, and various bird species.',
                'culture': 'Jharkhand has rich tribal culture with festivals like Sarhul, Karma, and Sohrai. The state is home to many tribal communities.',
                'food': 'Try local dishes like Litti Chokha, Rugra, Bamboo Shoot curry, and various tribal delicacies.',
                'weather': 'Best time to visit Jharkhand is from October to March when the weather is pleasant.',
                'how to reach': 'Jharkhand is well connected by air, rail, and road. Ranchi and Jamshedpur have airports.',
            }
            
            # Find appropriate response
            response = "I'm here to help you with information about Jharkhand tourism. You can ask about places to visit, culture, food, weather, or how to reach various destinations."
            
            for key, value in responses.items():
                if key in user_message:
                    response = value
                    break
            
            # Save chat message
            chat_message = ChatMessage.objects.create(
                user=request.user,
                message=user_message,
                response=response
            )
            
            return JsonResponse({
                'success': True,
                'response': response
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
