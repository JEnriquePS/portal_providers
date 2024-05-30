from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProviderSerializer, PartnershipSerializer
from ..models import Provider, Partnership


class ProviderViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    @extend_schema(responses={200: ProviderSerializer(many=True)})
    def list(self, request):
        queryset = Provider.objects.all()
        serializer = ProviderSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(request=ProviderSerializer, responses={201: ProviderSerializer})
    def create(self, request):
        if request.user.role == 'AP':
            return Response({"detail": "Los usuarios con rol 'aprobador' no pueden crear un proveedor"},
                            status=status.HTTP_403_FORBIDDEN)
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=ProviderSerializer, responses={200: ProviderSerializer})
    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Provider, pk=pk)
        serializer = ProviderSerializer(queryset)
        return Response(serializer.data)


class PartnershipViewSet(viewsets.ViewSet):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='request_placer',
                location=OpenApiParameter.QUERY,
                description='ID of Request Placer',
                type=str,
            ),
            OpenApiParameter(
                name='provider',
                location=OpenApiParameter.QUERY,
                description='ID of Provider',
                type=str,
            ),
        ],
        responses={200: OpenApiResponse(description='Check if partnership exist')}
    )
    @action(detail=False, methods=['get'], url_path='exists')
    def check_exists(self, request):
        request_placer_id = request.query_params.get('request_placer')
        provider_id = request.query_params.get('provider')
        exists = self.queryset.filter(request_placer_id=request_placer_id, provider_id=provider_id).exists()
        return Response({'exists': exists}, status=status.HTTP_200_OK)

