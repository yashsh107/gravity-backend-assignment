from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customers')

urlpatterns = [
    path('', include(router.urls)),
]
