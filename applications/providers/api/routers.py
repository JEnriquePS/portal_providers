from rest_framework.routers import DefaultRouter
from .views import ProviderViewSet, PartnershipViewSet

provider_create = ProviderViewSet.as_view({'post': 'create'})

router = DefaultRouter()
router.register(r'', ProviderViewSet, basename='provider')
router.register(r'partnerships', PartnershipViewSet, basename='partnership')

