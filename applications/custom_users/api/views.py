from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from applications.custom_users.api.serializers import UserSerializer
from applications.custom_users.models import CustomUser


class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    @extend_schema(request=UserSerializer, responses={201: UserSerializer})
    def list(self, request):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)



