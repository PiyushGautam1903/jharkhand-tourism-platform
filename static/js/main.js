// Main JavaScript for Jharkhand Tourism Platform

document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initializeAnimations();
    
    // Initialize responsive features
    initializeResponsiveFeatures();
    
    // Initialize smart features
    initializeSmartFeatures();
    
    // Initialize weather widget
    initializeWeatherWidget();
    
    // Initialize photo gallery
    initializePhotoGallery();
});

// Smart Tourism Features
function initializeSmartFeatures() {
    // Initialize search functionality
    initializeSearch();
    
    // Initialize rating system
    initializeRatingSystem();
    
    // Initialize booking system
    initializeBookingSystem();
    
    // Initialize itinerary planner
    initializeItineraryPlanner();
}

// Smart Search with Filters
function initializeSearch() {
    const searchInput = document.getElementById('place-search');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const placeCards = document.querySelectorAll('.place-card');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            filterPlaces(searchTerm);
        });
    }
    
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const filterType = this.getAttribute('data-filter');
            applyFilter(filterType);
            
            // Update active state
            filterButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });
}

// Rating System
function initializeRatingSystem() {
    const ratingStars = document.querySelectorAll('.rating-star');
    
    ratingStars.forEach(star => {
        star.addEventListener('click', function() {
            const rating = parseInt(this.getAttribute('data-rating'));
            updateRatingDisplay(rating, this.closest('.rating-container'));
        });
        
        star.addEventListener('mouseover', function() {
            const rating = parseInt(this.getAttribute('data-rating'));
            highlightRating(rating, this.closest('.rating-container'));
        });
    });
}

// Booking System
function initializeBookingSystem() {
    const bookingForms = document.querySelectorAll('.booking-form');
    
    bookingForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            handleBookingSubmission(this);
        });
    });
    
    // Date picker validation
    const checkInDates = document.querySelectorAll('input[name="check_in_date"]');
    const checkOutDates = document.querySelectorAll('input[name="check_out_date"]');
    
    checkInDates.forEach(input => {
        input.addEventListener('change', function() {
            const checkOutDate = this.closest('form').querySelector('input[name="check_out_date"]');
            if (checkOutDate) {
                checkOutDate.min = this.value;
            }
        });
    });
}

// Itinerary Planner
function initializeItineraryPlanner() {
    const addPlaceButtons = document.querySelectorAll('.add-to-itinerary');
    const itineraryContainer = document.getElementById('itinerary-container');
    
    addPlaceButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const placeId = this.getAttribute('data-place-id');
            const placeName = this.getAttribute('data-place-name');
            addToItinerary(placeId, placeName);
        });
    });
    
    // Drag and drop for itinerary reordering
    if (itineraryContainer) {
        initializeDragAndDrop(itineraryContainer);
    }
}

// Weather Widget
function initializeWeatherWidget() {
    const weatherWidgets = document.querySelectorAll('.weather-widget');
    
    weatherWidgets.forEach(widget => {
        const lat = widget.getAttribute('data-lat');
        const lon = widget.getAttribute('data-lon');
        const placeName = widget.getAttribute('data-place');
        
        if (lat && lon) {
            fetchWeatherData(lat, lon, placeName, widget);
        }
    });
}

// Photo Gallery
function initializePhotoGallery() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    const photoUploadForms = document.querySelectorAll('.photo-upload-form');
    
    // Initialize lightbox for gallery
    galleryItems.forEach((item, index) => {
        item.addEventListener('click', function() {
            openLightbox(index, galleryItems);
        });
    });
    
    // Handle photo uploads
    photoUploadForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            handlePhotoUpload(this);
        });
    });
}

// Get CSRF token
function getCsrfToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfToken ? csrfToken.value : '';
}

// Initialize animations
function initializeAnimations() {
    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.classList.add('fade-in');
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Initialize responsive features
function initializeResponsiveFeatures() {
    // Mobile menu handling
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', !isExpanded);
        });
    }

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (navbarCollapse && !navbarCollapse.contains(event.target) && 
            !navbarToggler.contains(event.target)) {
            const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                show: false
            });
        }
    });
}

// Utility functions
function showToast(message, type = 'success') {
    // Create toast element
    const toastContainer = document.getElementById('toast-container') || createToastContainer();
    
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;

    toastContainer.appendChild(toast);
    
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();

    // Remove toast element after it's hidden
    toast.addEventListener('hidden.bs.toast', function() {
        toast.remove();
    });
}

function createToastContainer() {
    const container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'position-fixed top-0 end-0 p-3';
    container.style.zIndex = '1055';
    document.body.appendChild(container);
    return container;
}

// Loading state management
function showLoading(element) {
    if (!element) return;
    
    const originalText = element.innerHTML;
    element.innerHTML = '<span class="loading"></span> Loading...';
    element.disabled = true;
    element.setAttribute('data-original-text', originalText);
}

function hideLoading(element) {
    if (!element) return;
    
    const originalText = element.getAttribute('data-original-text');
    if (originalText) {
        element.innerHTML = originalText;
        element.removeAttribute('data-original-text');
    }
    element.disabled = false;
}

// Form validation helpers
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePhone(phone) {
    const re = /^\+?[\d\s-()]+$/;
    return re.test(phone) && phone.replace(/\D/g, '').length >= 10;
}

// Image handling
function handleImageError(img) {
    img.src = '/static/images/placeholder.jpg';
    img.onerror = null;
}

// Copy to clipboard
function copyToClipboard(text) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(function() {
            showToast('Copied to clipboard!', 'success');
        }, function() {
            showToast('Failed to copy to clipboard', 'danger');
        });
    } else {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        try {
            document.execCommand('copy');
            showToast('Copied to clipboard!', 'success');
        } catch (err) {
            showToast('Failed to copy to clipboard', 'danger');
        }
        document.body.removeChild(textArea);
    }
}