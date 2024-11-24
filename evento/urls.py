from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ConciertoViewSet, ConferenciaViewSet

router = DefaultRouter()
router.register('api/conciertos', ConciertoViewSet)
router.register('api/conferencias', ConferenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas del enrutador
]
