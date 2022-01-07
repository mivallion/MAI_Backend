from django.contrib import admin
from django.urls import include, path

from auth.views import GoogleLogin

urlpatterns = [
    path('api/cats/', include('cat.urls')),
    path('api/users/', include("users.urls")),
    path('api/reviews/', include("reviews.urls")),
    
    path('api/admin/', admin.site.urls),

    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/login/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/auth/accounts', include("allauth.urls")),
]
