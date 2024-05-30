from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from applications.orders.models import Order
from .serializers import OrderSerializer
from applications.custom_users.api.permissions import IsAP


class OrderViewSet(viewsets.ViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def check_object_permissions(self, request, obj):
        if self.action == "update" or self.action == "partial_update":
            permission_classes = (IsAuthenticated, IsAP)
        else:
            permission_classes = (IsAuthenticated,)

        for permission_class in permission_classes:
            if not permission_class().has_object_permission(request, self, obj):
                self.permission_denied(request)

    def get_object(self, pk):
        return get_object_or_404(Order, pk=pk)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        order = self.get_object(kwargs['pk'])
        serializer = self.serializer_class(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




