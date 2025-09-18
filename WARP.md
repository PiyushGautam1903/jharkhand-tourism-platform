# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview
Jharkhand Tourism Platform is a Django web application that promotes eco and cultural tourism in Jharkhand, India. The platform features user authentication, tourism place database, interactive maps, and an AI chatbot with voice input support.

## Development Commands

### Environment Setup
```bash
# Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Create and activate virtual environment (Linux/Mac)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Database Operations
```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Populate sample tourism data (12 pre-configured places)
python manage.py populate_sample_data

# Create admin user
python manage.py createsuperuser
```

### Development Server
```bash
# Run development server
python manage.py runserver

# Access application at http://127.0.0.1:8000/
```

### Testing and Development
```bash
# Run tests
python manage.py test

# Django shell for debugging
python manage.py shell

# Collect static files for production
python manage.py collectstatic
```

## Architecture Overview

### Core Models Architecture
- **TourismPlace**: Central model storing place data with geographic coordinates, categorization (eco/cultural/religious/adventure/historical), and detailed information
- **UserProfile**: Extends Django's User model with tourism-specific fields (phone, address, preferred places)
- **ChatMessage**: Stores user-chatbot interactions with response history

### URL Structure & Views
The application uses a simple URL pattern rooted at the main app:
- Authentication flow: `home` → `login/register` → `dashboard`
- Tourism features: `places/` (list with filtering) → `places/<id>/` (detail with maps)
- Interactive feature: `chatbot/` (interface) + `api/chatbot/` (JSON API)

### Frontend Integration Points
- **Google Maps API**: Integrated in place detail views using lat/lng from TourismPlace model
- **Web Speech API**: Voice-to-text functionality in chatbot interface
- **Bootstrap 5**: Responsive design framework with custom CSS in `static/css/style.css`

### Sample Data Management
The `populate_sample_data` management command creates 12 tourism places covering major Jharkhand destinations including Hundru Falls, Baidyanath Temple, Netarhat, Betla National Park, etc. This command is idempotent and safe to run multiple times.

### Chatbot Logic
Simple keyword-based chatbot in `views.chatbot_api()` with predefined responses for tourism queries. Responses cover places, culture, food, weather, and transportation. All conversations are stored in ChatMessage model for history.

## Key Technical Considerations

### Django App Structure
Single-app architecture with `main/` containing all business logic. Templates are organized in `templates/main/` with a shared base template. Static files use standard Django static files handling.

### Authentication Flow
Django's built-in authentication with custom UserProfile model. Login redirects to dashboard, logout redirects to home. All tourism features require authentication.

### Database Schema
Uses SQLite for development (production-ready for PostgreSQL). Geographic data stored as DecimalField coordinates. Image handling through Django's ImageField with Pillow.

### API Design
RESTful approach with CSRF-exempted chatbot API endpoint. JSON request/response format for chatbot interactions. Error handling returns JSON error responses.

## Development Workflow

When working with tourism places:
1. Use Django admin at `/admin/` for content management
2. New places automatically appear in filtering and map systems
3. Chatbot responses are keyword-based and may need manual updates for new content

When modifying the chatbot:
1. Update response dictionary in `views.chatbot_api()`
2. Consider adding new keywords for better matching
3. Test voice input functionality across different browsers

When adding new features:
1. Authentication is required for all main features except home/login/register
2. Use existing model relationships (UserProfile.preferred_places ManyToMany)
3. Follow the established URL pattern in `main/urls.py`