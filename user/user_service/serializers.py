from rest_framework import serializers
from .models import User, FullName, Address


class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['no_house', 'street', 'district', 'city']

class UserSerializer(serializers.ModelSerializer):
    fullname = FullNameSerializer()
    address = AddressSerializer()

    class Meta:
        model = User
        fields = ["id", "email", "password", "fullname", "address"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')

        fullname = FullName.objects.create(**fullname_data)
        address = Address.objects.create(**address_data)

        user = User.objects.create(
            email=validated_data['email'],
            fullname=fullname,
            address=address
        )
        if password is not None:
            user.set_password(password)
        user.save()
        return user