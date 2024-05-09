# serializers.py
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from .models import FullName, Address, Account

class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['no_house', 'street', 'district', 'city']

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = Account
        fields = ['email', 'password']

    def create(self, validated_data):
        account = Account(email=validated_data['email'])
        account.set_password(validated_data['password'])
        account.save()
        return account

class UserSerializer(serializers.ModelSerializer):
    fullname = FullNameSerializer()
    address = AddressSerializer()
    account = AccountSerializer()

    class Meta:
        model = User
        fields = ['id', 'fullname', 'address', 'account']

    def create(self, validated_data):
        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')
        account_data = validated_data.pop('account')

        fullname = FullName.objects.create(**fullname_data)
        address = Address.objects.create(**address_data)

        account = Account.objects.create(email=account_data['email'])
        account.set_password(account_data['password'])
        account.save()

        user = User.objects.create(
            fullname=fullname,
            address=address,
            account=account
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
