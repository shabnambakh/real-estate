from rest_framework import serializers

from common.serializers import CitySerializer

from .models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Apartment
        fields = '__all__'


class OptionSerializer(serializers.Serializer):
    min_price = serializers.IntegerField()
    max_price = serializers.IntegerField()
    min_area = serializers.IntegerField()
    max_area = serializers.IntegerField()
    count = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
