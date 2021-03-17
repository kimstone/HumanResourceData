from django.urls import path

from apps.access_control.views import (
    edit_profile_view,
    index_page_view,
    login_view,
    logout_view,
    register_view,
    view_account_view,
)

app_name = 'apps.access_control'

urlpatterns = [
    path('', index_page_view, name="index"),
    path('<user_id>/', view_account_view, name="show"),
    path('<user_id>/edit', edit_profile_view, name="edit"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('register', register_view, name="register"),
]
