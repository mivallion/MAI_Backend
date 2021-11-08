from django.urls import path

from . import views

urlpatterns = [
    path('', views.CatView.as_view()),
    path('users', views.UserView.as_view()),
    path('reviews', views.ReviewView.as_view()),
]
