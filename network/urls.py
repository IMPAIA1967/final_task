from django.urls import include, path
from rest_framework.routers import DefaultRouter
from network.views import NetworkViewSet


# Создаём роутер
router = DefaultRouter()
router.register(r'network', NetworkViewSet, basename='network')

# Подключаем роутер к urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
