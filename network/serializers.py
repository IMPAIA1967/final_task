from rest_framework import serializers
from network.models import Network


class NetworkSerializer(serializers.ModelSerializer):
    # Долг нельзя менять через API
    debt = serializers.DecimalField(
        max_digits=15,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = Network
        # Поля которые отдаём в API
        fields = [
            'name',
            'email',
            'country',
            'city',
            'street',
            'house_number',
            'product_name',
            'product_model',
            'product_release_date',
            'supplier',
            'debt',
            'created_at'
        ]
