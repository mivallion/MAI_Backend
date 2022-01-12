from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
from reviews import views

router = DefaultRouter()
# router.register(r'', views.ReviewView)

# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('search/', views.SearchView.as_view()),
]