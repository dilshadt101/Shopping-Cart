from django.urls import path, include


urlpatterns = [
    path('user/', include('django.contrib.auth.urls')),
]