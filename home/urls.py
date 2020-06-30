from django.urls import path
from .views import home, logout_system


urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_system, name='logout'),
]
