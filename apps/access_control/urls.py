from django.urls import path

from apps.access_control.views import (
    index_page_view,
    register_view,
)

app_name = 'apps.access_control'

urlpatterns = [
    path('', index_page_view, name="index"),
    path('register', register_view, name="register"),
]
