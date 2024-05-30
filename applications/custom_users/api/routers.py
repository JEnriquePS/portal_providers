from rest_framework.routers import DefaultRouter

from applications.custom_users.api.views import UserViewSet


router = DefaultRouter()
router.register(r'', UserViewSet, basename='user_list')
