from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from network.models import Network
from network.serializers import NetworkSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    # Откуда брать данные
    queryset = Network.objects.all()
    # Какой сериализатор использовать
    serializer_class = NetworkSerializer
    # Права доступа только для сотрудников
    permission_classes = [IsAdminUser]
    # Фиотрация по стране
    filterset_fields = ['country']
