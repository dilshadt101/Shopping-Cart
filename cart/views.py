from django.views.generic import ListView

from .models import Item


class HomePageView(ListView):
    model = Item
    template_name = 'cart/home.html'
    context_object_name = 'items'

