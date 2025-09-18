// Main JavaScript for Jharkhand Tourism Platform

document.addEventListener('DOMContentLoaded', function() {
    // Chatbot widget functionality
    initializeChatbot();
    
    // Initialize animations
    initializeAnimations();
    
    // Initialize responsive features
    initializeResponsiveFeatures();
});

// Chatbot Widget
function initializeChatbot() {
    const chatbotToggle = document.getElementById('chatbot-toggle');
    const chatbotPopup = document.getElementById('chatbot-popup');
    const chatbotClose = document.getElementById('chatbot-close');
    const chatInput = document.getElementById('chat-input');
    const sendMessage = document.getElementById('send-message');
    const voiceInput = document.getElementById('voice-input');
    const chatMessages = document.getElementById('chat-messages');

    if (!chatbotToggle) return;

    // Toggle chatbot popup
    chatbotToggle.addEventListener('click', function() {
        const isVisible = chatbotPopup.style.display !== 'none';
        chatbotPopup.style.display = isVisible ? 'none' : 'block';
        
        if (!isVisible) {
            chatInput.focus();
            scrollChatToBottom();
        }
    });

    // Close chatbot
    if (chatbotClose) {
        chatbotClose.addEventListener('click', function() {
            chatbotPopup.style.display = 'none';
        });
    }

    // Send message on Enter
    if (chatInput) {
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                sendChatMessage();
            }
        });
    }

    // Send message on button click
    if (sendMessage) {
        sendMessage.addEventListener('click', sendChatMessage);
    }

    // Voice input
    if (voiceInput && 'webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        voiceInput.addEventListener('click', function() {
            recognition.start();
            this.innerHTML = '<i class="fas fa-stop text-danger"></i>';
            this.classList.add('btn-outline-danger');
            this.classList.remove('btn-outline-primary');
        });

        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            chatInput.value = transcript;
            sendChatMessage();
        };

        recognition.onend = function() {
            voiceInput.innerHTML = '<i class="fas fa-microphone"></i>';
            voiceInput.classList.remove('btn-outline-danger');
            voiceInput.classList.add('btn-outline-primary');
        };
    } else if (voiceInput) {
        voiceInput.style.display = 'none';
    }

    // Send chat message function
    function sendChatMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message to chat
        addChatMessage(message, true);

        // Show typing indicator
        showTypingIndicator();

        // Send to API
        fetch('/api/chatbot/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            hideTypingIndicator();
            if (data.success) {
                addChatMessage(data.response, false);
            } else {
                addChatMessage('Sorry, I encountered an error. Please try again.', false);
            }
        })
        .catch(error => {
            hideTypingIndicator();
            addChatMessage('Sorry, I am unable to respond right now. Please try again.', false);
        });

        chatInput.value = '';
    }

    // Add message to chat
    function addChatMessage(message, isUser) {
        if (!chatMessages) return;

        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'} mb-2`;
        
        const time = new Date().toLocaleTimeString('en-US', { 
            hour: '2-digit', 
            minute: '2-digit',
            hour12: false 
        });

        if (isUser) {
            messageDiv.innerHTML = `
                <div class="text-end">
                    <div class="bg-primary text-white p-2 rounded d-inline-block" style="max-width: 80%;">
                        ${message}
                    </div>
                    <div><small class="text-muted">${time}</small></div>
                </div>
            `;
        } else {
            messageDiv.innerHTML = `
                <div>
                    <div class="bg-light p-2 rounded d-inline-block" style="max-width: 80%;">
                        ${message}
                    </div>
                    <div><small class="text-muted">${time}</small></div>
                </div>
            `;
        }

        chatMessages.appendChild(messageDiv);
        scrollChatToBottom();
    }

    // Show typing indicator
    function showTypingIndicator() {
        if (!chatMessages) return;

        const typingDiv = document.createElement('div');
        typingDiv.id = 'typing-indicator';
        typingDiv.className = 'message bot-message mb-2';
        typingDiv.innerHTML = `
            <div>
                <div class="bg-light p-2 rounded d-inline-block">
                    <div class="typing">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>
            </div>
        `;

        chatMessages.appendChild(typingDiv);
        scrollChatToBottom();
    }

    // Hide typing indicator
    function hideTypingIndicator() {
        const typing = document.getElementById('typing-indicator');
        if (typing) {
            typing.remove();
        }
    }

    // Scroll chat to bottom
    function scrollChatToBottom() {
        if (chatMessages) {
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    }
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