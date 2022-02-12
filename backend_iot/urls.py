from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from data.api.viewsets import DataViewSet
from iot.api.viewsets import IotViewSet

router = routers.DefaultRouter(trailing_slash=False)

#endpoint Khomp
router.register('api/v1_2/json/itg', DataViewSet, basename='data')
router.register('iot', IotViewSet, basename='iot')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

#scheduler
from scheduler import scheduler
scheduler.start()
