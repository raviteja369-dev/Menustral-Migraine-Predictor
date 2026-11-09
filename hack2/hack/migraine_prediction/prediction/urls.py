from django.urls import path
from .views import predict_migraine

urlpatterns = [
    path('', predict_migraine, name='predict'),  # This will process POST requests
]
