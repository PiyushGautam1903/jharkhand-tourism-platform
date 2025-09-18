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
    path('chatbot/', views.chatbot, name='chatbot'),
    path('api/chatbot/', views.chatbot_api, name='chatbot_api'),
]