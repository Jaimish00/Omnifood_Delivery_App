from django.db import transaction
from django.db.models.fields.related import ForeignKey
from django.forms import PasswordInput
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes 
from django.contrib.auth import get_user_model

from .models import User, Customer, HotelAdmin, DeliveryPerson

class UserSerializer(serializers.HyperlinkedModelSerializer):

    @transaction.atomic()
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = User.objects.create(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    @transaction.atomic()
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'phone', 'is_active', 'is_superuser', 'is_staff')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    # If we want to create customer using validated_data, use **validated_data because it is dictionary
    @transaction.atomic()
    def create(self, validated_data):
        # Getting the base user info first
        user_data = validated_data.pop('user')
        
        password = user_data.pop('password', None) # Fetching the password
        instance = User.objects.create(**user_data) # Creating base user
        if password is not None:
            instance.set_password(password) # Setting the password
        instance.save()

        customer = Customer.objects.create(user=instance, **validated_data) # Creating customer with the given customer info
        return customer
    
    @transaction.atomic()
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        # Updating the rest of the user data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Updating actual user data
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        return instance

    class Meta:
        model = Customer
        fields = ('user', 'address')

class HotelAdminSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    # If we want to create customer using validated_data, use **validated_data because it is dictionary
    @transaction.atomic()
    def create(self, validated_data):
        user_data = validated_data.pop('user') 
        
        password = user_data.pop('password', None)
        instance = User.objects.create(**user_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        
        hotel_admin = HotelAdmin.objects.create(user=instance, **validated_data)
        return hotel_admin
    
    @transaction.atomic()
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        # Updating the rest of the user data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Updating actual user data
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        return instance

    class Meta:
        model = HotelAdmin
        fields = ('user', 'hotel_name', 'hotel_address', 'hotel_description', 'hotel_email', 'hotel_phone', 'fssai_license')



class DeliveryPersonSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    @transaction.atomic()
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        
        password = user_data.pop('password', None)
        instance = User.objects.create(**user_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        
        delivery_person = DeliveryPerson.objects.create(user=instance, **validated_data)
        return delivery_person
    
    @transaction.atomic()
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        # Updating the rest of the user data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Updating actual user data
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        return instance

    class Meta:
        model = DeliveryPerson
        fields = ('user', 'preferred_location', 'date_of_birth', 'gender', 'license_plate_no', 'driving_license_number') 


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HotelAdmin
        fields = ('hotel_name', 'hotel_address', 'hotel_description', 'hotel_email', 'hotel_phone') 