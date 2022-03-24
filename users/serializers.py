from rest_framework import serializers
from users import models


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'name', 'password', 'gender', 'phone', 'address')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        
        user = models.CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            gender=validated_data['gender'],
            phone=validated_data['phone'],
            address=validated_data['address']
        )

        return user





