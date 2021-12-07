from django.views.generic import TemplateView
# from django.contrib.auth import


class HomePageView(TemplateView):
    template_name = 'cart/home.html'


