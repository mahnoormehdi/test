from rest_framework import serializers
from api.models import Cities


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Cities
        fields="__all__"

