from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/cat/', include('cat.urls')),
    path('api/admin/', admin.site.urls),
]
