from django.urls import path
from .views import init_view

urlpatterns = [
    path('<str>', init_view)
]