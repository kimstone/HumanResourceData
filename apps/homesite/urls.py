from django.urls import path

from apps.homesite.views import (
    about_page_view,
    contact_page_view,
    home_page_view,
)

app_name = 'apps.homesite'

urlpatterns = [
    path('', home_page_view, name="home"),
    path('about', about_page_view, name="about"),
    path('contact', contact_page_view, name="contact"),
]
