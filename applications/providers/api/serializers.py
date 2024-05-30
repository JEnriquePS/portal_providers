from rest_framework import serializers

from applications.providers.models import Provider, Partnership


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'address', 'contact']


class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ['request_placer', 'provider']
        depth = 1
