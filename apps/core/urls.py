# django
from django.urls import path

# local files
from .views import (
    home_view,
)


app_name = 'core'

urlpatterns = [
    path('', home_view, name='home'),
]