from rest_framework import serializers
from .models import Concierto, Conferencia

class ConciertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concierto
        fields = ('id', 'nombre', 'fecha', 'lugar', 'artista', 'duracion', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at',)

class ConferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferencia
        fields = ('id', 'nombre', 'fecha', 'lugar', 'tema', 'orador', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at',)
