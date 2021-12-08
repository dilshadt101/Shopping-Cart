from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    remove_from_cart,
    reduce_quantity_item,
    add_to_cart,
    HomePageView,
    OrderSummaryView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
