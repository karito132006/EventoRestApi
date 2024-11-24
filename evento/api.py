from rest_framework import viewsets, permissions
from .models import Concierto, Conferencia
from .serializers import ConciertoSerializer, ConferenciaSerializer

class ConciertoViewSet(viewsets.ModelViewSet):
    queryset = Concierto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ConciertoSerializer

class ConferenciaViewSet(viewsets.ModelViewSet):
    queryset = Conferencia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ConferenciaSerializer
