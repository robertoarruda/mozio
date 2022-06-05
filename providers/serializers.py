from bson import ObjectId
from rest_framework import serializers
from rest_framework_mongoengine import fields

from providers.models import Provider, ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):
    location = fields.GeoJSONField(geo_type='Polygon')

    class Meta:
        model = ServiceArea
        fields = ['_id', 'provider_id', 'name', 'price', 'location']
        read_only_fields = ['_id']

    def create(self, validated_data):
        service_area = ServiceArea(
            provider_id=ObjectId(validated_data['provider_id']),
            name=validated_data['name'],
            price=validated_data['price'],
            location={'type': 'Polygon', 'coordinates': validated_data['location']},
        )
        service_area.save()
        return service_area

    def update(self, instance, validated_data):
        instance.provider_id = validated_data.get('provider_id', instance.provider_id)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.location = validated_data.get('location', instance.location)

        if not isinstance(instance.provider_id, ObjectId):
            instance.provider_id = ObjectId(instance.provider_id)

        instance.save()
        return instance


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['_id', 'name', 'email', 'phone_number', 'language', 'currency']
        read_only_fields = ['_id']
