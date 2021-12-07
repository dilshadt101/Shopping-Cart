from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path('user/', include('django.contrib.auth.urls')),
    path('', HomePageView.as_view(), name='home')
]
