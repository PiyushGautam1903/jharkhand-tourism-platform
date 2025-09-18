# Jharkhand Tourism Platform 🏔️

A comprehensive Smart Digital Platform to Promote Eco & Cultural Tourism in Jharkhand, built with Django and modern web technologies.

## Features ✨

- **User Authentication**: Complete registration and login system
- **Tourism Places Database**: Comprehensive information about tourist destinations in Jharkhand
- **Interactive Maps**: Google Maps integration for directions and location viewing
- **AI Chatbot**: Intelligent tourism assistant with voice input support
- **Voice-to-Text**: Web Speech API integration for hands-free interaction
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **Place Categories**: Eco tourism, cultural sites, religious places, adventure spots, and historical locations
- **Advanced Filtering**: Search and filter places by type, district, and other criteria

## Technology Stack 🛠️

- **Backend**: Django 5.2.6
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production ready)
- **APIs**: Web Speech API, Google Maps API
- **UI/UX**: Font Awesome icons, custom CSS animations
- **Image Handling**: Pillow for image processing

## Installation & Setup 🚀

### Prerequisites
- Python 3.8 or higher
- Git

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd jharkhand-tourism-platform
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Populate sample data
python manage.py populate_sample_data
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## Project Structure 📁

```
jharkhand-tourism-platform/
├── main/                          # Main Django app
│   ├── migrations/               # Database migrations
│   ├── management/              # Custom management commands
│   │   └── commands/
│   │       └── populate_sample_data.py
│   ├── models.py                # Database models
│   ├── views.py                 # View functions
│   ├── urls.py                  # URL patterns
│   ├── admin.py                 # Admin interface configuration
│   └── apps.py                  # App configuration
├── templates/                    # HTML templates
│   ├── base.html               # Base template
│   └── main/                   # App-specific templates
│       ├── home.html           # Landing page
│       ├── login.html          # Login page
│       ├── register.html       # Registration page
│       ├── dashboard.html      # User dashboard
│       ├── places_list.html    # Places listing
│       ├── place_detail.html   # Place detail view
│       └── chatbot.html        # Chatbot interface
├── static/                      # Static files
│   ├── css/
│   │   └── style.css           # Custom styles
│   └── js/
│       └── main.js             # JavaScript functionality
├── media/                       # User uploads
├── tourism_platform/           # Django project settings
├── requirements.txt             # Python dependencies
├── manage.py                   # Django management script
└── README.md                   # Project documentation
```

## Key Features Walkthrough 🌟

### 1. User Authentication
- **Registration**: Users can create accounts with email verification
- **Login/Logout**: Secure authentication system
- **User Profiles**: Extended user information storage

### 2. Tourism Places
- **Comprehensive Database**: 12+ pre-populated famous destinations
- **Detailed Information**: Description, timings, entry fees, best time to visit
- **Geographic Data**: Latitude/longitude for accurate mapping
- **Categorization**: Eco, cultural, religious, adventure, historical

### 3. Interactive Maps
- **Google Maps Integration**: Click any place to get directions
- **Location Visualization**: Interactive maps on place detail pages
- **Real-time Navigation**: Direct integration with Google Maps

### 4. AI Tourism Chatbot
- **Natural Language Processing**: Understands tourism-related queries
- **Voice Input**: Web Speech API for voice commands
- **Contextual Responses**: Information about places, culture, food, weather
- **Chat History**: Persistent conversation history per user

### 5. Responsive Design
- **Mobile-First**: Optimized for all device sizes
- **Modern UI**: Clean, professional design with smooth animations
- **Accessibility**: WCAG compliant with proper ARIA labels

## Sample Tourist Places Included 🏞️

1. **Hundru Falls** (Eco) - 98m waterfall near Ranchi
2. **Baidyanath Temple, Deoghar** (Religious) - Sacred Jyotirlinga
3. **Netarhat** (Eco) - "Queen of Chhota Nagpur" hill station
4. **Betla National Park** (Eco) - Tiger reserve and wildlife sanctuary
5. **Rock Garden, Ranchi** (Eco) - Popular family destination
6. **Jonha Falls** (Eco) - Religious significance with natural beauty
7. **Jagannath Temple, Ranchi** (Religious) - Famous for Rath Yatra
8. **Jamshedpur** (Cultural) - India's first planned industrial city
9. **Hazaribagh National Park** (Eco) - Wildlife photography destination
10. **Ranchi Hill (Pahari Mandir)** (Religious) - Hilltop temple
11. **Dassam Falls** (Eco) - Spectacular 44m waterfall
12. **Palamu Tiger Reserve** (Eco) - Tiger conservation area

## API Endpoints 🔗

- `/` - Home page
- `/login/` - User login
- `/register/` - User registration
- `/logout/` - User logout
- `/dashboard/` - User dashboard (login required)
- `/places/` - Places listing with filters
- `/places/<id>/` - Place detail view
- `/chatbot/` - Chatbot interface
- `/api/chatbot/` - Chatbot API endpoint
- `/admin/` - Django admin panel

## Chatbot Capabilities 🤖

The AI tourism assistant can help with:
- Information about tourist places
- Cultural attractions and festivals
- Local food and cuisine recommendations
- Best time to visit suggestions
- Transportation and how to reach destinations
- General tourism queries about Jharkhand

### Sample Chatbot Queries:
- "Tell me about places to visit in Jharkhand"
- "How to reach Ranchi?"
- "What is the best time to visit Netarhat?"
- "Tell me about local food in Jharkhand"
- "Information about Baidyanath Temple"

## Customization 🎨

### Adding New Places
1. Access Django admin at `/admin/`
2. Add new tourism places with complete information
3. Include coordinates for map integration

### Extending Chatbot
1. Modify the `chatbot_api` view in `main/views.py`
2. Add new response patterns in the responses dictionary
3. Integrate with external APIs for more sophisticated responses

### Styling
1. Modify `static/css/style.css` for visual changes
2. Update Bootstrap classes in templates
3. Add custom animations and effects

## Production Deployment 🚀

### Environment Variables
Create a `.env` file with:
```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgres://user:pass@localhost/db
GOOGLE_MAPS_API_KEY=your-google-maps-key
```

### Database Configuration
For production, configure PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tourism_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files
Configure for production:
```bash
python manage.py collectstatic
```

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security Features 🔒

- CSRF protection on all forms
- SQL injection prevention through Django ORM
- XSS protection with template auto-escaping
- Secure password hashing
- Session security
- Input validation and sanitization

## Performance Features ⚡

- Efficient database queries with select_related
- Static file compression
- Image optimization with Pillow
- Lazy loading for images
- Responsive images for different screen sizes

## Browser Compatibility 🌐

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+
- Mobile browsers (iOS Safari, Chrome Mobile)

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Support 💬

For support and questions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation

---

**Built with ❤️ for promoting the beautiful tourism destinations of Jharkhand, India**