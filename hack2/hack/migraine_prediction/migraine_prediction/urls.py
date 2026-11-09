from django.contrib import admin
from django.urls import path, include
from prediction.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Renders predict.html
    path('predict/', include('prediction.urls')),  # Handles predictions
]
