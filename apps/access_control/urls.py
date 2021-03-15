from django.urls import path

from apps.access_control.views import (
    index_page_view,
)

app_name = 'apps.access_control'

urlpatterns = [
    path('', index_page_view, name="index"),
]
