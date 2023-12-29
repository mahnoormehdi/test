from django.urls import path
from .views import get

urlpatterns = [
    path('api/get_data/', get,),
]