from rest_framework import serializers
from authentication.models import CustomUser
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        # required=True,
        style={'input_type': 'password'} #, 'placeholder': 'Password'}
    )
    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'first_name', 'middle_name','last_name', 'email','password','role', 'is_active']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        print(validated_data)
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user