from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Organization, Subscription


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'email', 'password', 'company_name', 'is_active', 'is_staff')
        read_only_fields = ('id', 'is_active', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        organization = Organization.objects.create(**validated_data)
        return organization

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.password = make_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
