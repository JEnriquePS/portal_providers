from rest_framework import serializers

from applications.custom_users.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_staff']

