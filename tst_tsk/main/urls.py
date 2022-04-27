from django.urls import path
from .views import init_view

urlpatterns = [
    path('', init_view)
]