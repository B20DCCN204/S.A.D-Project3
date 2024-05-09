from rest_framework import serializers
from .models import User, FullName, Address, Account


class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['no_house', 'street', 'district', 'city']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'password']
        extra_kwargs = {"password": {"write_only": True}}

class UserSerializer(serializers.ModelSerializer):
    fullname = FullNameSerializer()
    address = AddressSerializer()
    account = AccountSerializer()

    class Meta:
        model = User
        fields = ["id", "fullname", "address", "account"]

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        password = account_data.pop('password')

        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')

        fullname = FullName.objects.create(**fullname_data)
        address = Address.objects.create(**address_data)

        account = Account.objects.create(email=account_data['email'])
        account.set_password(password)
        account.save()

        user = User.objects.create(
            fullname=fullname,
            address=address,
            account=account
        )
        return user
