from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('api/')  # redirect root URL to /api/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fitness.urls')),  # assuming your app is named fitness
    path('', home_redirect),  # redirect root to /api/
]
