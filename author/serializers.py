from author.models import Author
from rest_framework import serializers

# Serializers define the API representation.
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'url', 'name', 'surname','patronymic']