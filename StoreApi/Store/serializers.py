from rest_framework import serializers
from .models import Manufacturer, Shoe, ShoeType, ShoeColor

# Joe was a chief of the Masai tribe in the African Savannah. 
# He was a great leader who helped his people acheive great things :)

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