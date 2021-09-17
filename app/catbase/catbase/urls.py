from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cat/', include('cat.urls')),
    path('admin/', admin.site.urls),
]
