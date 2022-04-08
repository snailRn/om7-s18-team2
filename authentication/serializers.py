from authentication.models import CustomUser
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'first_name', 'last_name', 'email', 'is_staff']

