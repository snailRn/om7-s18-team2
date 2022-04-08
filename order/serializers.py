from order.models import Order
from rest_framework import serializers

# Serializers define the API representation.
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at','end_at', 'plated_end_at']
