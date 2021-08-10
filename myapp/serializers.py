from rest_framework import serializers
from .models import Place
from django.utils import timezone

class PlaceSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=30)
	address = serializers.CharField(max_length=30)


	def create(self, validated_data):
		return Place.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.address = validated_data.get('address', instance.address)
		instance.save()
		return instance

class PlaceModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		# fields = ['name', 'address']
		fields = '__all__'