from django.contrib import admin
from django.urls import path,include
from api.views import CityViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cities', CityViewSet)

urlpatterns = [
    path('',include(router.urls))
]