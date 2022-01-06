from django.contrib import admin
from django.urls import include, path

from app.catbase.auth.views import GoogleLogin

urlpatterns = [
    path('api/cat/', include('cat.urls')),
    path('api/admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/login/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/auth/accounts', include("allauth.urls")),
]
