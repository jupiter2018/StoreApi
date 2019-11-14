from rest_framework import serializers
from .models import Manufacturer, Shoe, ShoeType, ShoeColor

#Learn about Joe's fascinating life growing up in the African Savannah :)

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['url', 'name', 'website']


class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['url', 'style']

class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['url', 'color_name']


class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = '__all__'