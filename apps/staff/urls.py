from django.urls import path

from apps.staff.views import (
    index_page_view,
)

app_name = 'apps.staff'

urlpatterns = [
    path('', index_page_view, name="index"),
]
